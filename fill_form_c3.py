import json
import time
import re
import sys
from playwright.sync_api import sync_playwright

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeW3-3oal_q10NCTjCgZRGIy_Xi2S3n6VXW-6_W7cavJvJ6Kg/viewform"
TEST_MODE = False  # Set to False to submit responses

likert_reverse_map = {
    "1": "Strongly Disagree",
    "2": "Disagree",
    "3": "Neutral",
    "4": "Agree",
    "5": "Strongly Agree"
}

def normalize_text(text):
    if not text: return ""
    # Remove * and extra spaces, convert to lower, normalize quotes
    text = text.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    return " ".join(text.replace("*", "").split()).lower()

def get_label(page, rg):
    label = rg.get_attribute('aria-label')
    if not label:
        labelledby = rg.get_attribute('aria-labelledby')
        if labelledby:
            ids = labelledby.split()
            texts = []
            for id in ids:
                try:
                    text = page.evaluate(f'document.getElementById("{id}")?.innerText')
                    if text: texts.append(text)
                except:
                    pass
            label = " ".join(texts)
    return label or ""

def fill_form():
    input_file = 'c3/responses.json'
    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        responses = json.load(f)

    if TEST_MODE:
        responses = responses[:1]
        print("Running in TEST MODE (1 response, no submit)")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        for i, response in enumerate(responses):
            if i != 95:
                continue  # Skip already submitted entries
            print(f"Filling response {i+1}/{len(responses)}: {response['role']}")
            try:
                page.goto(FORM_URL)
                page.wait_for_load_state('networkidle')
                
                # Section A: Role
                role = response['role']
                page.locator(f'[data-value="{role}"]').click(force=True)
                page.get_by_role('button', name='繼續').click()
                page.wait_for_load_state('networkidle')
                
                # Section B: Demographics
                try:
                    page.wait_for_selector('[role="radiogroup"]', timeout=5000)
                except:
                    print("Warning: No radiogroups found on Demographics page immediately.")
                
                demographics_map = {}
                if role == "Employee McDonald’s":
                    demographics_map = {
                        "gender": "Gender",
                        "age": "Age Range",
                        "education": "Education Level",
                        "experience": "Working Experience",
                        "employment_type": "Employment Type"
                    }
                else:
                    demographics_map = {
                        "gender": "Gender",
                        "age": "Age Range",
                        "employment_status": "Employment status",
                        "education": "Education Level",
                        "frequency": "How often do you eat McDonald’s?"
                    }
                
                # Fill Demographics
                radiogroups = page.get_by_role('radiogroup').all()
                
                rg_labels = []
                for rg in radiogroups:
                    lbl = get_label(page, rg)
                    norm = normalize_text(lbl)
                    rg_labels.append((rg, norm, lbl))

                for key, label_part in demographics_map.items():
                    if key in response:
                        val = str(response[key])
                        found = False
                        norm_target = normalize_text(label_part)
                        
                        for rg, rg_norm, rg_raw in rg_labels:
                            if norm_target in rg_norm:
                                try:
                                    rg.locator(f'[data-value="{val}"]').click(force=True)
                                    found = True
                                    break
                                except Exception as e:
                                    print(f"Error clicking demographic '{val}' for '{key}': {e}")
                        
                        if not found:
                            print(f"Warning: Could not find demographic '{key}' (Target: '{norm_target}')")
                
                page.get_by_role('button', name='繼續').click()
                page.wait_for_load_state('networkidle')
                
                # Section C+: Questions
                page_num = 1
                while True:
                    time.sleep(1) # Wait a bit for animations
                    try:
                        page.wait_for_selector('[role="radiogroup"]', timeout=2000)
                    except:
                        pass 

                    radiogroups = page.get_by_role('radiogroup').all()
                    
                    for rg in radiogroups:
                        label = get_label(page, rg)
                        norm_label = normalize_text(label)
                        
                        matched_key = None
                        for q_key in sorted(response.keys(), key=len, reverse=True):
                            if q_key in demographics_map or q_key == "role":
                                continue
                            
                            norm_key = normalize_text(q_key)
                            if norm_key in norm_label:
                                matched_key = q_key
                                break
                        
                        if matched_key:
                            val = str(response[matched_key])
                            try:
                                # Check if value exists
                                if rg.locator(f'[data-value="{val}"]').count() > 0:
                                    rg.locator(f'[data-value="{val}"]').click(force=True)
                                elif val in likert_reverse_map and rg.locator(f'[data-value="{likert_reverse_map[val]}"]').count() > 0:
                                    rg.locator(f'[data-value="{likert_reverse_map[val]}"]').click(force=True)
                                else:
                                    # Try finding by aria-label if data-value fails (sometimes values are different)
                                    # But data-value is usually reliable for Google Forms
                                    print(f"Warning: Option '{val}' not found for '{matched_key}'")
                            except Exception as e:
                                print(f"Error clicking value '{val}' for '{matched_key}': {e}")
                    
                    # Check for navigation
                    next_btn = page.locator('div[role="button"]').filter(has_text="繼續").first
                    submit_btn = page.locator('div[role="button"]').filter(has_text="提交").first
                    
                    if next_btn.count() > 0 and next_btn.is_visible():
                        next_btn.click()
                        page.wait_for_load_state('networkidle')
                        page_num += 1
                    elif submit_btn.count() > 0 and submit_btn.is_visible():
                        if not TEST_MODE:
                            submit_btn.click()
                            try:
                                page.wait_for_selector('text=提交其他回應', timeout=10000)
                                print(f"Submitted response {i+1}")
                            except:
                                print(f"Submitted {i+1}, but confirmation not detected.")
                        else:
                            print(f"Test mode: Ready to submit response {i+1}")
                        break
                    else:
                        if page.locator('.freebirdFormviewerViewItemsItemErrorMessage').count() > 0:
                            print(f"Validation error on page {page_num}. Skipping response.")
                            break
                        
                        if page.get_by_role('button', name='繼續').is_visible():
                             page.get_by_role('button', name='繼續').click()
                             page.wait_for_load_state('networkidle')
                             page_num += 1
                             continue
                        
                        if page.get_by_role('button', name='提交').is_visible():
                             if not TEST_MODE:
                                page.get_by_role('button', name='提交').click()
                                print(f"Submitted response {i+1}")
                             break

                        print("Stuck: Neither Next nor Submit button found.")
                        break

            except Exception as e:
                print(f"Error filling response {i+1}: {e}")
                continue

        browser.close()

if __name__ == "__main__":
    fill_form()
