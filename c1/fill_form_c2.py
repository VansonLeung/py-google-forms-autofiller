import json
import time
from playwright.sync_api import sync_playwright

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScIFtXUK85JgKEB3VeG9hpAu_wOTN3Yf-5dV4ae3LuRLmFNWw/viewform?usp=sharing&ouid=106047623805805335793"
TEST_MODE = False  # Set to False to submit responses

def fill_form():
    with open('c1/responses_c2.json', 'r') as f:
        responses = json.load(f)

    if TEST_MODE:
        responses = responses[:1]
        print("Running in TEST MODE (1 response, no submit)")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        for i, response in enumerate(responses):
            print(f"Filling response {i+1}/{len(responses)}: {response['role']}")
            try:
                page.goto(FORM_URL)
                page.wait_for_load_state('networkidle')
                
                # Section A: Role
                role = response['role']
                page.locator(f'[data-value="{role}"]').click()
                page.get_by_role('button', name='繼續').click()
                
                if role == "Employee McDonald’s":
                    # Section B: Personal Information (Employee)
                    page.locator(f'[data-value="{response["gender"]}"]').click()
                    page.locator(f'[data-value="{response["age"]}"]').click()
                    
                    # Education Level
                    try:
                        page.locator(f'[data-value="{response["education"]}"]').click()
                    except:
                        print(f"Could not find option for education: {response['education']}")
                        
                    page.locator(f'[data-value="{response["experience"]}"]').click()
                    page.locator(f'[data-value="{response["employment_type"]}"]').click()
                    
                    page.get_by_role('button', name='繼續').click()
                    
                    # Section C: Employee Motivation
                    questions = [
                        "I feel free to undertake tasks and decisions independently at work.",
                        "I feel very happy regarding pay wages compared to workload.",
                        "I believe that everyone on the staff is treated equally at McDonald’s irrespective of their cast, creed, region, and religion.",
                        "I can put McDonald’s on Higher ranking regarding the safety and security of staff while working at McDonald’s.",
                        "My workplace is the best example of work–life balance.",
                        "Working at McDonald’s is a wonderful and interesting experience."
                    ]
                    
                    for j, q in enumerate(questions):
                        val = str(response[f"q{j+1}"])
                        # Find the radiogroup by question text (substring match)
                        # Then find the radio button by value (1-5)
                        page.get_by_role('radiogroup', name=q).get_by_role('radio', name=val).click()

                    page.get_by_role('button', name='繼續').click()
                                            
                else:
                    # Customer
                    # Section B: Personal Information (Customer)
                    page.locator(f'[data-value="{response["gender"]}"]').click()
                    page.locator(f'[data-value="{response["age"]}"]').click()
                    page.locator(f'[data-value="{response["employment_status"]}"]').click()
                    page.locator(f'[data-value="{response["education"]}"]').click()
                    page.locator(f'[data-value="{response["frequency"]}"]').click()
                    
                    page.get_by_role('button', name='繼續').click()
                    
                    # Section C: Customer Satisfaction
                    questions = [
                        "The prices at McDonald‘s are fair.",
                        "McDonald‘s food tastes good.",
                        "McDonald‘s meals are served quickly.",
                        "McDonald‘s restaurants are clean and well taken care of.",
                        "McDonalds restaurants have an appealing interior design.",
                        "McDonald‘s restaurants are a comfortable place to eat in."
                    ]
                    
                    for j, q in enumerate(questions):
                        val = str(response[f"q{j+1}"])
                        page.get_by_role('radiogroup', name=q).get_by_role('radio', name=val).click()

                    page.get_by_role('button', name='繼續').click()

                # Submit
                if not TEST_MODE:
                    page.wait_for_selector('text=提交')
                    page.locator('text=提交').click()
                    
                    # Wait for confirmation page
                    page.wait_for_selector('text=提交其他回應')
                    page.locator('text=提交其他回應').click()
                    print(f"Submitted response {i+1}")
                else:
                    print(f"Test mode: Filled response {i+1} but did not submit.")
                    input("Press Enter to close browser...")
                
            except Exception as e:
                print(f"Error filling response {i+1}: {e}")
                # Take screenshot for debugging
                page.screenshot(path=f"c1/error_{i+1}.png")
                continue
                
            except Exception as e:
                print(f"Error filling response {i+1}: {e}")
                # Take screenshot for debugging
                page.screenshot(path=f"c1/error_{i+1}.png")
                continue

        browser.close()

if __name__ == "__main__":
    fill_form()
