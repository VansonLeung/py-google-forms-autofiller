import random

# Define the options and their weights based on trends-2.md

gender_options = ['Male', 'Female']
gender_weights = [33, 65]  # Male:33, Female:65

age_options = ['18-29 years old', '30-39 years old', '40-49 years old', '50 years old and above']
age_weights = [82, 12, 4, 0]  # 50+ not in data, set to 0

ethnicity_options = ['Chinese', 'India', 'Iban', 'Malay', 'Other']
ethnicity_weights = [89, 3, 2, 2, 2]

nationality_options = ['Malaysian', 'Other', 'China', 'Chinese']
nationality_weights = [90, 5, 2, 1]

year_options = ['1', '2', '3', '4', '5']
year_weights = [22, 44, 17, 10, 5]

# School options with weights from trends-2.md
school_options = ['School of Management', 'business', 'School of Pharmaceutical Sciences', 'School of Biological Sciences', 'School of Management ', 'School of Housing Building and Planning', 'School of Engineering', 'SCHOOL OF COMPUTER SCIENCE', 'International School', 'University Tenaga Nasional', 'School of Accounting, Finance and Business', 'School of Social Sciences', 'School of Communication', 'School of management', 'SCHOOL OF MANAGEMENT', 'SOM', 'UTAR', 'hbp', 'School of Computer Science', 'School of Business Management', 'School of Pharmaceutical Sciences ', 'School of Pharmaceutical Science', 'school of hbp', 'School of Chemical Sciences', 'SMK SAINT ELIZABETH ', 'School of Communication ', 'School of housing building and planning ', 'School of management ', 'School of pharmaceutical sciences ', 'Som', 'School of Physics', 'SMK SAINT ELIZABETH']
school_weights = [41, 7, 5, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

internet_exp_options = ['More than 4 years', '2-3 years']
internet_exp_weights = [95, 3]

hours_options = ['6-10 hours', '1-5 hours', 'More than 15 hours', '11-15 hours']
hours_weights = [59, 30, 6, 3]

# CSB Adoption
antivirus_options = ['2 Yes', '1 No', '0 Other']
antivirus_weights = [74, 23, 1]

tfa_options = ['2 Yes', '1 No', '0 Other']
tfa_weights = [81, 16, 1]

# Frequency
freq_options = ['4 Often', '3 Sometimes', '2 Rarely', '1 Never', '0 Other']

# Weights for each frequency question
install_os_weights = [38, 34, 21, 5, 0]  # 4,3,2,1,0
url_bar_weights = [32, 44, 18, 4, 0]
https_check_weights = [31, 24, 39, 4, 0]
visit_unknown_weights = [6, 32, 30, 29, 0]
email_link_weights = [5, 31, 19, 40, 3]
open_attach_weights = [4, 23, 32, 38, 1]
check_links_weights = [29, 28, 18, 21, 2]
change_pass_weights = [26, 24, 33, 14, 1]

# Skills Level
sk_options = ['3 Neutual', '4 High', '2 low', '5 Very High']

computer_skills_weights = [54, 38, 4, 2]
internet_skills_weights = [37, 41, 6, 14]  # 3,4,2,5
info_security_weights = [48, 36, 10, 4]
cyber_threats_weights = [41, 49, 6, 2]

# Knowledge of Cyber Threats
kct_options = ['2 Correct Answer', '0 I don’t know.', '1 Incorrect Answer']

email_worm_weights = [57, 25, 16]
trojan_weights = [56, 25, 17]
spam_weights = [73, 8, 17]
phishing_weights = [57, 23, 18]
dos_weights = [40, 35, 23]
social_eng_weights = [32, 33, 33]  # 2,0,1
security_incident_weights = [56, 26, 16]

# Likert scale for IPC, ATT, SN, PBC, PACT
likert_options = ['4 Agree', '3 Neutral', '5 Strongly Agree', '1 Strongly Disagree', '2 Disagree']

# IPC
ipc1_weights = [40, 37, 19, 2, 0]
ipc2_weights = [49, 24, 20, 0, 5]
ipc3_weights = [44, 20, 33, 0, 1]

# ATT
att1_weights = [37, 13, 40, 2, 6]
att2_weights = [46, 14, 34, 1, 3]
att3_weights = [17, 16, 14, 12, 39]
att4_weights = [15, 23, 14, 14, 32]

# SN
sn1_weights = [43, 20, 27, 2, 6]
sn2_weights = [51, 17, 22, 5, 3]
sn3_weights = [50, 20, 21, 2, 5]
sn4_weights = [69, 15, 11, 3, 0]
sn5_weights = [29, 26, 17, 5, 21]

# PBC
pbc1_weights = [54, 24, 9, 4, 7]
pbc2_weights = [39, 40, 13, 5, 1]
pbc3_weights = [40, 27, 13, 4, 14]
pbc4_weights = [24, 23, 10, 9, 32]
pbc5_weights = [25, 20, 13, 7, 33]

# PACT
pact1_weights = [44, 27, 25, 2, 0]
pact2_weights = [51, 20, 23, 1, 3]
pact3_weights = [54, 22, 16, 4, 2]
pact4_weights = [62, 10, 21, 2, 3]

# Suggestions - mostly empty, add some random text occasionally
suggestions_options = ['', 'No', 'good', 'no', 'It would be great to see online posters about cybersecurity threats and how to fight against them', 'Great ', '.', 'Practice cybersecurity are important']
suggestions_weights = [85, 2, 1, 1, 1, 1, 1, 1]  # Approximate, mostly ''

# To induce some randomness and make it less detectable as fake, we'll add a small chance (5%) to choose a random option instead of weighted for some fields
def random_choice_with_noise(options, weights, noise_prob=0.05):
    if random.random() < noise_prob:
        return random.choice(options)
    else:
        return random.choices(options, weights=weights)[0]

# Generate 49 responses
responses = []
for _ in range(49):
    response = {
        'gender': random_choice_with_noise(gender_options, gender_weights),
        'age': random_choice_with_noise(age_options, age_weights),
        'ethnicity': random_choice_with_noise(ethnicity_options, ethnicity_weights),
        'nationality': random_choice_with_noise(nationality_options, nationality_weights),
        'year': random_choice_with_noise(year_options, year_weights),
        'school': random_choice_with_noise(school_options, school_weights),
        'internet_exp': random_choice_with_noise(internet_exp_options, internet_exp_weights),
        'hours': random_choice_with_noise(hours_options, hours_weights),
        'antivirus': random_choice_with_noise(antivirus_options, antivirus_weights),
        'tfa': random_choice_with_noise(tfa_options, tfa_weights),
        'install_os': random_choice_with_noise(freq_options, install_os_weights),
        'url_bar': random_choice_with_noise(freq_options, url_bar_weights),
        'https_check': random_choice_with_noise(freq_options, https_check_weights),
        'visit_unknown': random_choice_with_noise(freq_options, visit_unknown_weights),
        'email_link': random_choice_with_noise(freq_options, email_link_weights),
        'open_attach': random_choice_with_noise(freq_options, open_attach_weights),
        'check_links': random_choice_with_noise(freq_options, check_links_weights),
        'change_pass': random_choice_with_noise(freq_options, change_pass_weights),
        'computer_skills': random_choice_with_noise(sk_options, computer_skills_weights),
        'internet_skills': random_choice_with_noise(sk_options, internet_skills_weights),
        'info_security': random_choice_with_noise(sk_options, info_security_weights),
        'cyber_threats': random_choice_with_noise(sk_options, cyber_threats_weights),
        'email_worm': random_choice_with_noise(kct_options, email_worm_weights),
        'trojan': random_choice_with_noise(kct_options, trojan_weights),
        'spam': random_choice_with_noise(kct_options, spam_weights),
        'phishing': random_choice_with_noise(kct_options, phishing_weights),
        'dos': random_choice_with_noise(kct_options, dos_weights),
        'social_eng': random_choice_with_noise(kct_options, social_eng_weights),
        'security_incident': random_choice_with_noise(kct_options, security_incident_weights),
        'ipc1': random_choice_with_noise(likert_options, ipc1_weights),
        'ipc2': random_choice_with_noise(likert_options, ipc2_weights),
        'ipc3': random_choice_with_noise(likert_options, ipc3_weights),
        'att1': random_choice_with_noise(likert_options, att1_weights),
        'att2': random_choice_with_noise(likert_options, att2_weights),
        'att3': random_choice_with_noise(likert_options, att3_weights),
        'att4': random_choice_with_noise(likert_options, att4_weights),
        'sn1': random_choice_with_noise(likert_options, sn1_weights),
        'sn2': random_choice_with_noise(likert_options, sn2_weights),
        'sn3': random_choice_with_noise(likert_options, sn3_weights),
        'sn4': random_choice_with_noise(likert_options, sn4_weights),
        'sn5': random_choice_with_noise(likert_options, sn5_weights),
        'pbc1': random_choice_with_noise(likert_options, pbc1_weights),
        'pbc2': random_choice_with_noise(likert_options, pbc2_weights),
        'pbc3': random_choice_with_noise(likert_options, pbc3_weights),
        'pbc4': random_choice_with_noise(likert_options, pbc4_weights),
        'pbc5': random_choice_with_noise(likert_options, pbc5_weights),
        'pact1': random_choice_with_noise(likert_options, pact1_weights),
        'pact2': random_choice_with_noise(likert_options, pact2_weights),
        'pact3': random_choice_with_noise(likert_options, pact3_weights),
        'pact4': random_choice_with_noise(likert_options, pact4_weights),
        'suggestions': random_choice_with_noise(suggestions_options, suggestions_weights)
    }
    responses.append(response)

# Print or save
import json
with open('responses-2.json', 'w') as f:
    json.dump(responses, f, indent=2)

print("Generated 49 responses in responses-2.json")