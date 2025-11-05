import random

# Define the options and their weights based on trends

gender_options = ['Male', 'Female']
gender_weights = [15, 34]  # Male:15, Female:34

age_options = ['18-29 years old', '30-39 years old', '40-49 years old', '50 years old and above']
age_weights = [42, 6, 0, 1]  # 40-49 not in data, set to 0

ethnicity_options = ['Malay', 'Chinese', 'India', 'Other']
ethnicity_weights = [1, 45, 1, 2]  # Malay:1, Chinese:45, India:1, Iban:2 -> Other

nationality_options = ['Malaysian', 'Other']
nationality_weights = [46, 3]  # Malaysian:46, others:3

year_options = ['1', '2', '3', '4', '5']
year_weights = [9, 24, 8, 5, 3]

# School is text, common ones
school_options = ['School of Management', 'School of Biological Sciences', 'University Tenaga Nasional', 'School of Pharmaceutical Sciences', 'School of Computer Science', 'School of Chemical Sciences', 'School of Housing Building and Planning', 'School of Social Sciences', 'School of Engineering', 'School of Physics', 'School of Communication', 'School of Accounting, Finance and Business', 'Som', 'business', 'International School', 'SCHOOL OF COMPUTER SCIENCE', 'UTAR', 'hbp', 'school of hbp', 'School of management', 'School of pharmaceutical sciences', 'School of Pharmaceutical Science', 'School of housing building and planning', 'School of Communication ', 'School of Pharmaceutical Sciences ', 'SMK SAINT ELIZABETH']
school_weights = [19, 2, 2, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # approximate counts

internet_exp_options = ['Less than 1 year', '1-2 year', '2-3 years', '3-4 years', 'More than 4 years']
internet_exp_weights = [0, 0, 1, 0, 48]  # only 2-3:1, >4:48

hours_options = ['Almost never', 'Less than 1 hour', '1-5 hours', '6-10 hours', '11-15 hours', 'More than 15 hours']
hours_weights = [0, 0, 12, 33, 2, 2]

# CSB Adoption
antivirus_options = ['0 Other', '1 No', '2 Yes']
antivirus_weights = [1, 13, 35]

tfa_options = ['0 Other', '1 No', '2 Yes']
tfa_weights = [1, 8, 40]

# Frequency
freq_options = ['0 Other', '1 Never', '2 Rarely', '3 Sometimes', '4 Often']

# Weights for each frequency question
install_os_weights = [0, 3, 12, 16, 18]
url_bar_weights = [0, 2, 8, 22, 17]
https_check_weights = [0, 3, 18, 12, 16]
visit_unknown_weights = [0, 14, 14, 16, 4]
email_link_weights = [1, 21, 10, 14, 3]
open_attach_weights = [1, 19, 15, 11, 3]
check_links_weights = [1, 10, 10, 14, 14]
change_pass_weights = [1, 8, 15, 13, 12]

# Skills Level
sk_options = ['1 very low', '2 low', '3 Neutual', '4 High', '5 Very High']

computer_skills_weights = [0, 2, 26, 20, 1]
internet_skills_weights = [0, 3, 19, 22, 5]
info_security_weights = [0, 5, 23, 19, 2]
cyber_threats_weights = [0, 3, 22, 23, 1]

# Knowledge of Cyber Threats
kct_options = ['0 I don’t know.', '1 Incorrect Answer', '2 Correct Answer']

email_worm_weights = [14, 9, 26]
trojan_weights = [12, 9, 28]
spam_weights = [4, 9, 36]
phishing_weights = [11, 9, 29]
dos_weights = [17, 13, 19]
social_eng_weights = [15, 17, 17]
security_incident_weights = [15, 8, 26]

# Likert scale for IPC, ATT, SN, PBC, PACT
likert_options = ['1 Strongly Disagree', '2 Disagree', '3 Neutral', '4 Agree', '5 Strongly Agree']

# IPC
ipc1_weights = [1, 0, 16, 21, 11]
ipc2_weights = [0, 3, 11, 24, 11]
ipc3_weights = [0, 1, 11, 23, 14]

# ATT
att1_weights = [1, 4, 5, 21, 18]
att2_weights = [1, 1, 7, 24, 16]
att3_weights = [7, 19, 9, 8, 6]
att4_weights = [8, 17, 9, 7, 8]

# SN
sn1_weights = [1, 5, 9, 22, 12]
sn2_weights = [2, 2, 9, 26, 10]
sn3_weights = [1, 3, 11, 23, 11]
sn4_weights = [1, 0, 10, 32, 6]
sn5_weights = [2, 7, 14, 16, 10]

# PBC
pbc1_weights = [2, 3, 13, 26, 5]
pbc2_weights = [2, 1, 17, 23, 6]
pbc3_weights = [2, 5, 14, 22, 6]
pbc4_weights = [3, 12, 14, 15, 5]
pbc5_weights = [3, 14, 12, 15, 5]

# PACT
pact1_weights = [1, 0, 11, 26, 11]
pact2_weights = [1, 1, 8, 26, 13]
pact3_weights = [2, 1, 10, 27, 9]
pact4_weights = [1, 1, 6, 29, 12]

# Generate 49 responses
responses = []
for _ in range(49):
    response = {
        'gender': random.choices(gender_options, weights=gender_weights)[0],
        'age': random.choices(age_options, weights=age_weights)[0],
        'ethnicity': random.choices(ethnicity_options, weights=ethnicity_weights)[0],
        'nationality': random.choices(nationality_options, weights=nationality_weights)[0],
        'year': random.choices(year_options, weights=year_weights)[0],
        'school': random.choices(school_options, weights=school_weights)[0],
        'internet_exp': random.choices(internet_exp_options, weights=internet_exp_weights)[0],
        'hours': random.choices(hours_options, weights=hours_weights)[0],
        'antivirus': random.choices(antivirus_options, weights=antivirus_weights)[0],
        'tfa': random.choices(tfa_options, weights=tfa_weights)[0],
        'install_os': random.choices(freq_options, weights=install_os_weights)[0],
        'url_bar': random.choices(freq_options, weights=url_bar_weights)[0],
        'https_check': random.choices(freq_options, weights=https_check_weights)[0],
        'visit_unknown': random.choices(freq_options, weights=visit_unknown_weights)[0],
        'email_link': random.choices(freq_options, weights=email_link_weights)[0],
        'open_attach': random.choices(freq_options, weights=open_attach_weights)[0],
        'check_links': random.choices(freq_options, weights=check_links_weights)[0],
        'change_pass': random.choices(freq_options, weights=change_pass_weights)[0],
        'computer_skills': random.choices(sk_options, weights=computer_skills_weights)[0],
        'internet_skills': random.choices(sk_options, weights=internet_skills_weights)[0],
        'info_security': random.choices(sk_options, weights=info_security_weights)[0],
        'cyber_threats': random.choices(sk_options, weights=cyber_threats_weights)[0],
        'email_worm': random.choices(kct_options, weights=email_worm_weights)[0],
        'trojan': random.choices(kct_options, weights=trojan_weights)[0],
        'spam': random.choices(kct_options, weights=spam_weights)[0],
        'phishing': random.choices(kct_options, weights=phishing_weights)[0],
        'dos': random.choices(kct_options, weights=dos_weights)[0],
        'social_eng': random.choices(kct_options, weights=social_eng_weights)[0],
        'security_incident': random.choices(kct_options, weights=security_incident_weights)[0],
        'ipc1': random.choices(likert_options, weights=ipc1_weights)[0],
        'ipc2': random.choices(likert_options, weights=ipc2_weights)[0],
        'ipc3': random.choices(likert_options, weights=ipc3_weights)[0],
        'att1': random.choices(likert_options, weights=att1_weights)[0],
        'att2': random.choices(likert_options, weights=att2_weights)[0],
        'att3': random.choices(likert_options, weights=att3_weights)[0],
        'att4': random.choices(likert_options, weights=att4_weights)[0],
        'sn1': random.choices(likert_options, weights=sn1_weights)[0],
        'sn2': random.choices(likert_options, weights=sn2_weights)[0],
        'sn3': random.choices(likert_options, weights=sn3_weights)[0],
        'sn4': random.choices(likert_options, weights=sn4_weights)[0],
        'sn5': random.choices(likert_options, weights=sn5_weights)[0],
        'pbc1': random.choices(likert_options, weights=pbc1_weights)[0],
        'pbc2': random.choices(likert_options, weights=pbc2_weights)[0],
        'pbc3': random.choices(likert_options, weights=pbc3_weights)[0],
        'pbc4': random.choices(likert_options, weights=pbc4_weights)[0],
        'pbc5': random.choices(likert_options, weights=pbc5_weights)[0],
        'pact1': random.choices(likert_options, weights=pact1_weights)[0],
        'pact2': random.choices(likert_options, weights=pact2_weights)[0],
        'pact3': random.choices(likert_options, weights=pact3_weights)[0],
        'pact4': random.choices(likert_options, weights=pact4_weights)[0],
        'suggestions': ''
    }
    responses.append(response)

# Print or save
import json
with open('responses.json', 'w') as f:
    json.dump(responses, f, indent=2)

print("Generated 49 responses")