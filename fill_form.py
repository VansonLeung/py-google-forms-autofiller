import json
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
FORM_URL = os.getenv('FORM_URL')

with open('responses.json') as f:
    responses = json.load(f)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(FORM_URL)

    # Start from index 1, since 0 was already submitted
    for i in range(2, len(responses)):
        response = responses[i]
        print(f"Filling response {i+1}")
            
        # Page 1: Demographics
        page.locator(f'[data-value="{response["gender"]}"]').click()
        page.locator(f'[data-value="{response["age"]}"]').click()
        if response["ethnicity"] == "Other":
            page.locator('[data-params*="ethnicity"] [data-value="__other_option__"]').click()
            page.locator('[data-params*="ethnicity"] [aria-label*="其他回應"]').fill("Other")
        else:
            page.locator(f'[data-params*="ethnicity"] [data-value="{response["ethnicity"]}"]').click()
        
        if response["nationality"] == "Other":
            page.locator('[data-params*="nationality"] [data-value="__other_option__"]').click()
            page.locator('[data-params*="nationality"] [aria-label*="其他回應"]').fill("Other")
        else:
            page.locator(f'[data-params*="nationality"] [data-value="{response["nationality"]}"]').click()
        page.locator(f'[data-value="{response["year"]}"]').click()
        page.locator('[data-params*="Which school are you from"] input').fill(response["school"])
        page.locator(f'[data-value="{response["internet_exp"]}"]').click()
        page.locator(f'[data-value="{response["hours"]}"]').click()
        page.click('text=繼續')
        
        # Page 2: CSB
        # Adoption
        page.locator(f'div[aria-label*="antivirus software"] [data-value="{response["antivirus"]}"]').click()
        page.locator(f'div[aria-label*="two-factor authentication"] [data-value="{response["tfa"]}"]').click()
        
        # Frequency
        page.locator(f'div[aria-label*="install a new version"] [data-value="{response["install_os"]}"]').click()
        page.locator(f'div[aria-label*="URL bar"] [data-value="{response["url_bar"]}"]').click()
        page.locator(f'div[aria-label*="uses HTTPS"] [data-value="{response["https_check"]}"]').click()
        page.locator(f'div[aria-label*="websites I have not heard of"] [data-value="{response["visit_unknown"]}"]').click()
        page.locator(f'div[aria-label*="link in an email"] [data-value="{response["email_link"]}"]').click()
        page.locator(f'div[aria-label*="open attachments"] [data-value="{response["open_attach"]}"]').click()
        page.locator(f'div[aria-label*="check on links"] [data-value="{response["check_links"]}"]').click()
        page.locator(f'div[aria-label*="change my passwords"] [data-value="{response["change_pass"]}"]').click()
        page.click('text=繼續')
        
        # Page 3: Skills
        page.locator(f'div[aria-label*="computer skills"] [data-value="{response["computer_skills"]}"]').click()
        page.locator(f'div[aria-label*="internet skills"] [data-value="{response["internet_skills"]}"]').click()
        page.locator(f'div[aria-label*="information security"] [data-value="{response["info_security"]}"]').click()
        page.locator(f'div[aria-label*="cyber threats"] [data-value="{response["cyber_threats"]}"]').click()
        page.click('text=繼續')
        
        # Page 4: KCT
        page.locator(f'div[aria-label*="email worm"] [data-value="{response["email_worm"]}"]').click()
        page.locator(f'div[aria-label*="trojan horse"] [data-value="{response["trojan"]}"]').click()
        page.locator(f'div[aria-label*="spam"] [data-value="{response["spam"]}"]').click()
        page.locator(f'div[aria-label*="Phishing"] [data-value="{response["phishing"]}"]').click()
        page.locator(f'div[aria-label*="DoS"] [data-value="{response["dos"]}"]').click()
        page.locator(f'div[aria-label*="Social engineering"] [data-value="{response["social_eng"]}"]').click()
        page.locator(f'div[aria-label*="security incident"] [data-value="{response["security_incident"]}"]').click()
        page.click('text=繼續')
        
        # Page 5: IPC
        page.locator(f'div[aria-label*="expect to"] [data-value="{response["ipc1"]}"]').click()
        page.locator(f'div[aria-label*="want to"] [data-value="{response["ipc2"]}"]').click()
        page.locator(f'div[aria-label*="intend to"] [data-value="{response["ipc3"]}"]').click()
        page.click('text=繼續')
        
        # Page 6: ATT
        page.locator(f'div[aria-label*="security behaviors is good idea"] [data-value="{response["att1"]}"]').click()
        page.locator(f'div[aria-label*="beneficial"] [data-value="{response["att2"]}"]').click()
        page.locator(f'div[aria-label*="unpleasant"] [data-value="{response["att3"]}"]').click()
        page.locator(f'div[aria-label*="useless"] [data-value="{response["att4"]}"]').click()
        page.click('text=繼續')
        
        # Page 7: SN
        page.locator(f'div[aria-label*="I should perform"] [data-value="{response["sn1"]}"]').click()
        page.locator(f'div[aria-label*="it would be a good idea to"] [data-value="{response["sn2"]}"]').click()
        page.locator(f'div[aria-label*="want me to perform"] [data-value="{response["sn3"]}"]').click()
        page.locator(f'div[aria-label*="expected of me to"] [data-value="{response["sn4"]}"]').click()
        page.locator(f'div[aria-label*="feel under social pressure"] [data-value="{response["sn5"]}"]').click()
        page.click('text=繼續')
        
        # Page 8: PBC
        page.locator(f'div[aria-label*="I am confident that I could perform professionally recommended cyber security behavior."] [data-value="{response["pbc1"]}"]').click()
        page.locator(f'div[aria-label*="It is easy for me to perform professionally recommended cyber security behavior."] [data-value="{response["pbc2"]}"]').click()
        page.locator(f'div[aria-label*="I have the resources and the knowledge to perform (practice) professionally recommended cyber security behavior."] [data-value="{response["pbc3"]}"]').click()
        page.locator(f'div[aria-label*="The decision to perform professionally recommended cyber security behavior is beyond my control."] [data-value="{response["pbc4"]}"]').click()
        page.locator(f'div[aria-label*="Whether I perform professionally recommended cyber security behaviors or not is not entirely up to me."] [data-value="{response["pbc5"]}"]').click()
        page.click('text=繼續')
        
        # Page 9: PACT
        page.locator(f'div[aria-label*="I am aware of the importance of practicing cybersecurity behaviors towards/for the future of security online."] [data-value="{response["pact1"]}"]').click()
        page.locator(f'div[aria-label*="I am aware of the need to practice cyber security behavior to reduce the risks of cyber threats online."] [data-value="{response["pact2"]}"]').click()
        page.locator(f'div[aria-label*="I am aware of cyber threats and their risks online."] [data-value="{response["pact3"]}"]').click()
        page.locator(f'div[aria-label*="I am concerned about cyber threats risks and its consequences for my security online."] [data-value="{response["pact4"]}"]').click()
        page.click('text=繼續')
        
        # Page 10: Suggestions
        # page.locator('textarea[aria-label*="suggestions"]').fill(response["suggestions"])
        # page.click('text=Submit')
        
        # Wait for submission
        page.wait_for_url('**/formResponse')
        page.click('text=提交其他回應')
            
        print(f"Submitted response {i+1}")