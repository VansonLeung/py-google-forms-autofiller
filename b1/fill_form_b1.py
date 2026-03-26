import json
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfGMNUw1m-b-UqO1z3RAlCKep7CxzDPjYbbKlohB0smVSJQDQ/viewform"

with open('responses-b-1.json') as f:
    responses = json.load(f)

# Define refs for options
gender_refs = {"Male": "i9", "Female": "i6"}
age_refs = {
    "18 – 20 years old": "i17",
    "21 - 25 years old": "i20",
    "26 - 30 years old": "i23",
    "31 – 35 years old": "i26",
    "36 – 40 years old": "i29",
    "46 – 50 years old": "i32",
    "Above 50 years old": "i35"
}
employment_refs = {
    "Government Sector": "i43",
    "Private Sector": "i46",
    "Self-employed": "i49",
    "Student": "i52",
    "Unemployed": "i55"
}
education_refs = {
    "Primary School": "i63",
    "Secondary School": "i66",
    "Diploma": "i69",
    "Bachelor's Degree": "i72",
    "Master": "i75",
    "Ph.D.": "i78"
}
frequency_refs = {
    "Daily": "i6",
    "Weekly": "i9",
    "Monthly": "i12",
    "Rarely": "i15"
}
purpose_refs = {
    "Grocery shopping": "i24",
    "Paying tolls": "i27",
    "Dining out": "i30",
    "Bill payments": "i33",
    "Mobile top-up": "i36",
    "Other": "i39"
}
spend_refs = {
    "Less than RM500": "i47",
    "RM500 to RM1,000": "i50",
    "RM1,000 to RM2,000": "i53",
    "Over RM2,000": "i56"
}
long_refs = {
    "Less than 6 months": "i64",
    "6 months to 1 year": "i67",
    "1 to 2 years": "i70",
    "More than 2 years": "i73"
}
satisfied_refs = {
    "1 - Very Dissatisfied": "i81",
    "2 - Dissatisfied": "i84",
    "3 - Neutral": "i87",
    "4 - Satisfied": "i90",
    "5 - Very Satisfied": "i93"
}
issues_refs = {
    "Never": "i101",
    "Rarely": "i104",
    "Sometimes": "i107",
    "Often": "i110",
    "Always": "i113"
}
improved_refs = {
    "1 - Strongly Disagree": "i121",
    "2 - Disagree": "i124",
    "3 - Neutral": "i127",
    "4 - Agree": "i130",
    "5 - Strongly Agree": "i133"
}
important_refs = {
    "1- Not Important": "i141",
    "2 - Slightly Important": "i144",
    "3 - Moderately Important": "i147",
    "4 - Very Important": "i150",
    "5 - Extremely Important": "i153"
}
likely_refs = {
    "1 - Very Unlikely": "i161",
    "2 - Unlikely": "i164",
    "3 - Neutral": "i167",
    "4 - Likely": "i170",
    "5 - Very Likely": "i173"
}
alternatives_refs = {
    "Cash": "i182",
    "Credit Card/Debit Card": "i185",
    "Other E-wallets (e.g., GrabPay, ShopeePay)": "i188",
    "Online Banking": "i191",
    "Other": "i194"
}

# For Likert scales, question texts for aria-label
pu_questions = [
    "Using Touch ’n Go eWallet helps me make faster payments.",
    "The features offered by Touch ’n Go eWallet are useful for my daily transactions.",
    "Touch ’n Go eWallet enhances my overall shopping convenience.",
    "Touch ’n Go eWallet helps me reduce the time spent on payment processes.",
    "Using Touch ’n Go eWallet increases my productivity in managing payments.",
    "Touch ’n Go eWallet provides valuable services that meet my payment needs.",
    "The convenience of Touch ’n Go eWallet motivates me to use it frequently."
]
peu_questions = [
    "I find the Touch ’n Go eWallet application easy to navigate.",
    "Making payments with Touch ’n Go eWallet is simple and straightforward.",
    "The process of reloading or top-up on Touch ’n Go eWallet is convenient.",
    "It is easy for me to find merchants that accept Touch ’n Go QR code payments.",
    "Learning to use Touch ’n Go eWallet was easy for me.",
    "The interface of Touch ’n Go eWallet is user-friendly."
]
pc_questions = [
    "Using Touch ’n Go QR payments fits well with my lifestyle.",
    "Touch ’n Go QR payments are compatible with the way I usually make payments.",
    "Using Touch ’n Go QR payments suits my daily routines.",
    "Touch ’n Go QR payments align with my preference for cashless transactions.",
    "Touch ’n Go QR payments fit well with the technologies I already use (e.g., smartphone apps).",
    "Using QR payments through Touch ’n Go matches the way I prefer to manage my finances."
]
pst_questions = [
    "I feel that my personal information is safe when I use Touch ’n Go QR payments.",
    "Touch ’n Go provides secure protection against unauthorized access.",
    "I believe that QR transactions made through Touch ’n Go are safe from fraud.",
    "Touch ’n Go has strong security features that protect my financial information.",
    "I trust Touch ’n Go to handle my transactions reliably.",
    "I believe Touch ’n Go is a trustworthy eWallet provider.",
    "I trust Touch ’n Go to complete my QR payment transactions accurately and on time.",
    "Touch ’n Go’s positive reputation increases my confidence in using QR payments.",
    "I trust that the company maintains transparency in its services."
]
pconv_questions = [
    "Ordering and paying through Touch ’n Go eWallet saves me time.",
    "Using Touch ’n Go eWallet is more convenient compared to cash or card payments.",
    "It is easy to pay multiple merchants using Touch ’n Go QR code in one go.",
    "Touch ’n Go eWallet makes my daily transactions more efficient.",
    "I can use Touch ’n Go eWallet anytime and anywhere without hassle.",
    "Touch ’n Go eWallet reduces the physical need to carry cash or cards."
]
ci_questions = [
    "I am satisfied with my experience using Touch ’n Go eWallet.",
    "I will likely continue to use Touch ’n Go eWallet in the future.",
    "I would recommend Touch ’n Go eWallet to friends and family.",
    "I frequently use Touch ’n Go eWallet for my transactions.",
    "I prefer Touch ’n Go eWallet over other payment methods.",
    "I feel that Touch ’n Go eWallet has improved my lifestyle convenience."
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(FORM_URL)

    for i in range(110):
        response = responses[i+11]
        print(f"Filling response {i+11}")
        
        # Initial: Yes/No
        if response["user"] == "Yes":
            page.locator('[id="i6"]').click()
        else:
            page.locator('[id="i9"]').click()
        page.click('text=繼續')
        
        # Personal Profile
        page.locator(f'[id="{gender_refs[response["gender"]]}"]').click()
        page.locator(f'[id="{age_refs[response["age"]]}"]').click()
        page.locator(f'[id="{employment_refs[response["employment"]]}"]').click()
        page.locator(f'[id="{education_refs[response["education"]]}"]').click()
        page.click('text=繼續')
        
        # Section B
        page.locator(f'[id="{frequency_refs[response["frequency"]]}"]').click()
        for p in response["purpose"].split("|"):
            page.locator(f'[id="{purpose_refs[p.strip()]}"]').click()
        page.locator(f'[id="{spend_refs[response["spend"]]}"]').click()
        page.locator(f'[id="{long_refs[response["long"]]}"]').click()
        page.locator(f'[id="{satisfied_refs[response["satisfied"]]}"]').click()
        page.locator(f'[id="{issues_refs[response["issues"]]}"]').click()
        page.locator(f'[id="{improved_refs[response["improved"]]}"]').click()
        page.locator(f'[id="{important_refs[response["important"]]}"]').click()
        page.locator(f'[id="{likely_refs[response["likely"]]}"]').click()
        for a in response["alternatives"].split("|"):
            page.locator(f'[id="{alternatives_refs[a.strip()]}"]').click()
        page.click('text=繼續')
        
        # Section C
        # Perceived Usefulness
        for j in range(7):
            val = response[f"pu{j+1}"]
            page.locator(f'[aria-label*="{pu_questions[j]}"][data-value="{val}"]').click()
        
        # Perceived Ease of Use
        for j in range(6):
            val = response[f"peu{j+1}"]
            page.locator(f'[aria-label*="{peu_questions[j]}"][data-value="{val}"]').click()
        
        # Perceived Compatibility
        for j in range(6):
            val = response[f"pc{j+1}"]
            page.locator(f'[aria-label*="{pc_questions[j]}"][data-value="{val}"]').click()
        
        # Perceived Security and Trust
        for j in range(9):
            val = response[f"pst{j+1}"]
            page.locator(f'[aria-label*="{pst_questions[j]}"][data-value="{val}"]').click()
        
        # Perceived Convenience
        for j in range(6):
            val = response[f"pconv{j+1}"]
            page.locator(f'[aria-label*="{pconv_questions[j]}"][data-value="{val}"]').click()
        
        # Consumer Intention
        for j in range(6):
            val = response[f"ci{j+1}"]
            page.locator(f'[aria-label*="{ci_questions[j]}"][data-value="{val}"]').click()
        
        page.locator('text=提交').click()  # Submit
        
        # Wait for submission
        page.wait_for_url('**/formResponse')
        page.click('text=提交其他回應')
        
        print(f"Submitted response {i+1}")
        