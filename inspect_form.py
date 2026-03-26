from playwright.sync_api import sync_playwright
import json

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScIFtXUK85JgKEB3VeG9hpAu_wOTN3Yf-5dV4ae3LuRLmFNWw/viewform?usp=sharing&ouid=106047623805805335793"

def inspect_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(FORM_URL)
        
        # Select Customer to see Customer questions
        page.locator('[data-value="Customer McDonald’s"]').click()
        page.get_by_role('button', name='繼續').click()
        
        # Wait for Section B
        page.wait_for_timeout(2000)
        
        # Fill Section B (Personal Info) to proceed
        page.evaluate('''() => {
            const groups = document.querySelectorAll('[role="radiogroup"]');
            groups.forEach(g => {
                const radios = g.querySelectorAll('[role="radio"]');
                if (radios.length > 0) radios[0].click();
            });
        }''')
        
        page.get_by_role('button', name='繼續').click()
        
        # Wait for Section C
        page.wait_for_timeout(2000)
        
        # Get all radiogroup labels (questions)
        questions = page.evaluate('''() => {
            const groups = document.querySelectorAll('[role="radiogroup"]');
            return Array.from(groups).map(g => {
                const labelId = g.getAttribute('aria-labelledby');
                if (labelId) {
                    const label = document.getElementById(labelId.split(' ')[0]); // Take first ID usually
                    return label ? label.innerText : g.getAttribute('aria-label');
                }
                return g.getAttribute('aria-label');
            });
        }''')
        
        print("Customer Questions found:")
        for q in questions:
            print(f"- {q}")
            
        browser.close()

if __name__ == "__main__":
    inspect_form()
