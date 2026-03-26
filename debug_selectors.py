from playwright.sync_api import sync_playwright
import time

def debug_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://docs.google.com/forms/d/e/1FAIpQLScIFtXUK85JgKEB3VeG9hpAu_wOTN3Yf-5dV4ae3LuRLmFNWw/viewform?usp=sharing&ouid=106047623805805335793")
        page.wait_for_load_state('networkidle')
        
        # Select Employee
        page.locator('[data-value="Employee McDonald’s"]').click()
        page.get_by_role('button', name='繼續').click()
        page.wait_for_load_state('networkidle')
        
        # Page 2: Employee Demographics
        radiogroups = page.get_by_role('radiogroup').all()
        for rg in radiogroups:
            rg.locator('[role="radio"]').first.click()
        
        page.get_by_role('button', name='繼續').click()
        page.wait_for_load_state('networkidle')
        
        print("\n--- Page 3: Employee Questions ---")
        try:
            page.wait_for_selector('[role="radiogroup"]', timeout=5000)
        except:
            print("No radiogroups found on Page 3")

        radiogroups = page.get_by_role('radiogroup').all()
        if radiogroups:
            rg = radiogroups[0]
            print(f"Question 0: {rg.get_attribute('aria-label')}")
            options = rg.locator('[role="radio"]').all()
            for opt in options:
                print(f"  - Option: '{opt.get_attribute('data-value')}'")

        browser.close()

if __name__ == "__main__":
    debug_form()
