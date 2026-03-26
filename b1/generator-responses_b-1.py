import random
import json

# Define the options and their weights based on trends-b-1.md

# Demographics
gender_options = ['Female', 'Male']
gender_weights = [46, 44]

age_options = ['21 - 25 years old', '18 – 20 years old', '31 – 35 years old', '26 - 30 years old', '46 – 50 years old', '36 – 40 years old']
age_weights = [45, 14, 10, 10, 6, 5]

employment_options = ['Student', 'Private Sector', 'Self-employed', 'Government Sector', 'Unemployed']
employment_weights = [52, 21, 12, 3, 2]

education_options = ["Bachelor's Degree", 'Master', 'Diploma', 'Secondary School', 'Primary School']
education_weights = [41, 26, 14, 8, 1]

# Usage Patterns
user_options = ['Yes']
user_weights = [90]

frequency_options = ['Daily', 'Weekly', 'Rarely', 'Monthly']
frequency_weights = [59, 17, 7, 7]

# Purpose: multiple select, use top combinations as options
purpose_options = [
    'Grocery shopping|Paying tolls|Dining out|Bill payments|Mobile top-up',
    'Dining out',
    'Grocery shopping|Dining out',
    'Dining out|Bill payments',
    'Paying tolls|Dining out',
    'Grocery shopping',
    'Grocery shopping|Paying tolls|Dining out|Bill payments',
    'Grocery shopping|Dining out|Bill payments|Mobile top-up',
    'Bill payments',
    'Grocery shopping|Bill payments',
    'Grocery shopping|Dining out|Mobile top-up',
    'Grocery shopping|Dining out|Bill payments',
    'Grocery shopping|Paying tolls',
    'Paying tolls|Dining out|Bill payments|Mobile top-up',
    'Grocery shopping|Paying tolls|Dining out',
    'Paying tolls',
    'Dining out|Bill payments|Mobile top-up',
    'Grocery shopping|Paying tolls|Dining out|Mobile top-up',
    'Mobile top-up',
    'Grocery shopping|Bill payments|Mobile top-up',
    'Grocery shopping|Dining out|Transfer to friends ',
    'Dining out|Mobile top-up',
    'Paying tolls|Dining out|Bill payments',
    'Paying tolls|Bill payments'
]
purpose_weights = [18, 10, 8, 6, 6, 6, 5, 4, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]

spend_options = ['Less than RM500', 'RM500 to RM1,000', 'RM1,000 to RM2,000', 'Over RM2,000']
spend_weights = [26, 25, 21, 18]

long_options = ['More than 2 years', '1 to 2 years', '6 months to 1 year', 'Less than 6 months']
long_weights = [58, 14, 11, 7]

# Satisfaction and Issues
satisfied_options = ['4 - Satisfied', '3 - Neutral', '5 - Very Satisfied', '2 - Dissatisfied', '1 - Very Dissatisfied']
satisfied_weights = [31, 29, 22, 5, 3]

issues_options = ['Rarely', 'Sometimes', 'Never', 'Often', 'Always']
issues_weights = [33, 23, 19, 13, 2]

improved_options = ['5 - Strongly Agree', '4 - Agree', '3 - Neutral', '2 - Disagree', '1 - Strongly Disagree']
improved_weights = [37, 35, 13, 3, 2]

# Importance and Likelihood
important_options = ['4 - Very Important', '5 - Extremely Important', '3 - Moderately Important', '1- Not Important', '2 - Slightly Important']
important_weights = [37, 20, 16, 11, 6]

likely_options = ['4 - Likely', '3 - Neutral', '5 - Very Likely', '2 - Unlikely', '1 - Very Unlikely']
likely_weights = [32, 32, 16, 8, 2]

# Alternative Payment Methods: multiple select
alternatives_options = [
    'Cash|Credit Card/Debit Card|Other E-wallets (e.g., GrabPay, ShopeePay)|Online Banking',
    'Cash',
    'Cash|Credit Card/Debit Card',
    'Credit Card/Debit Card|Other E-wallets (e.g., GrabPay, ShopeePay)|Online Banking',
    'Cash|Other E-wallets (e.g., GrabPay, ShopeePay)',
    'Credit Card/Debit Card|Online Banking',
    'Cash|Credit Card/Debit Card|Other E-wallets (e.g., GrabPay, ShopeePay)',
    'Other E-wallets (e.g., GrabPay, ShopeePay)',
    'Cash|Credit Card/Debit Card|Online Banking',
    'Other E-wallets (e.g., GrabPay, ShopeePay)|Online Banking',
    'Cash|Other E-wallets (e.g., GrabPay, ShopeePay)|Online Banking',
    'Credit Card/Debit Card|Other E-wallets (e.g., GrabPay, ShopeePay)',
    'Cash|Online Banking',
    'Online Banking',
    'Credit Card/Debit Card'
]
alternatives_weights = [24, 13, 9, 6, 6, 5, 5, 5, 4, 3, 3, 3, 2, 1, 1]

# Perceived Usefulness: 1-5 scale
pu_options = [1, 2, 3, 4, 5]

pu1_weights = [0, 2, 9, 32, 47]
pu2_weights = [0, 3, 11, 39, 37]
pu3_weights = [0, 3, 7, 43, 37]
pu4_weights = [0, 4, 8, 35, 43]
pu5_weights = [2, 4, 10, 38, 36]
pu6_weights = [0, 2, 11, 39, 38]
pu7_weights = [1, 4, 11, 32, 42]

# Perceived Ease of Use
peu_options = [1, 2, 3, 4, 5]

peu1_weights = [0, 2, 16, 30, 42]
peu2_weights = [1, 4, 10, 32, 43]
peu3_weights = [2, 2, 13, 35, 38]
peu4_weights = [3, 3, 12, 37, 35]
peu5_weights = [0, 1, 14, 25, 50]
peu6_weights = [0, 3, 19, 23, 45]

# Perceived Compatibility
pc_options = [1, 2, 3, 4, 5]

pc1_weights = [0, 2, 18, 31, 39]
pc2_weights = [0, 1, 12, 44, 33]
pc3_weights = [0, 3, 14, 36, 37]
pc4_weights = [1, 1, 13, 32, 43]
pc5_weights = [0, 4, 14, 35, 37]
pc6_weights = [0, 2, 12, 34, 42]

# Perceived Security and Trust
pst_options = [1, 2, 3, 4, 5]

pst1_weights = [0, 3, 19, 35, 33]
pst2_weights = [0, 6, 14, 45, 25]
pst3_weights = [1, 4, 21, 32, 32]
pst4_weights = [0, 7, 15, 35, 33]
pst5_weights = [0, 2, 20, 42, 26]
pst6_weights = [0, 4, 12, 50, 24]
pst7_weights = [0, 3, 17, 42, 28]
pst8_weights = [0, 3, 14, 40, 33]
pst9_weights = [2, 3, 12, 41, 32]

# Perceived Convenience
pconv_options = [1, 2, 3, 4, 5]

pconv1_weights = [2, 1, 8, 34, 45]
pconv2_weights = [0, 4, 13, 40, 33]
pconv3_weights = [1, 0, 18, 31, 40]
pconv4_weights = [2, 2, 9, 34, 43]
pconv5_weights = [1, 3, 12, 27, 47]
pconv6_weights = [0, 2, 10, 37, 41]

# Consumer Intention
ci_options = [1, 2, 3, 4, 5]

ci1_weights = [0, 3, 8, 35, 44]
ci2_weights = [0, 2, 7, 40, 41]
ci3_weights = [3, 3, 10, 31, 43]
ci4_weights = [0, 2, 9, 37, 42]
ci5_weights = [1, 5, 11, 32, 41]
ci6_weights = [0, 0, 13, 30, 47]

# To induce some randomness and make it less detectable as fake, we'll add a small chance (5%) to choose a random option instead of weighted for some fields
def random_choice_with_noise(options, weights, noise_prob=0.05):
    if random.random() < noise_prob:
        return random.choice(options)
    else:
        return random.choices(options, weights=weights)[0]

# Generate 49 responses
responses = []
for _ in range(110):
    response = {
        'gender': random_choice_with_noise(gender_options, gender_weights),
        'age': random_choice_with_noise(age_options, age_weights),
        'employment': random_choice_with_noise(employment_options, employment_weights),
        'education': random_choice_with_noise(education_options, education_weights),
        'user': random_choice_with_noise(user_options, user_weights),
        'frequency': random_choice_with_noise(frequency_options, frequency_weights),
        'purpose': random_choice_with_noise(purpose_options, purpose_weights),
        'spend': random_choice_with_noise(spend_options, spend_weights),
        'long': random_choice_with_noise(long_options, long_weights),
        'satisfied': random_choice_with_noise(satisfied_options, satisfied_weights),
        'issues': random_choice_with_noise(issues_options, issues_weights),
        'improved': random_choice_with_noise(improved_options, improved_weights),
        'important': random_choice_with_noise(important_options, important_weights),
        'likely': random_choice_with_noise(likely_options, likely_weights),
        'alternatives': random_choice_with_noise(alternatives_options, alternatives_weights),
        'pu1': random_choice_with_noise(pu_options, pu1_weights),
        'pu2': random_choice_with_noise(pu_options, pu2_weights),
        'pu3': random_choice_with_noise(pu_options, pu3_weights),
        'pu4': random_choice_with_noise(pu_options, pu4_weights),
        'pu5': random_choice_with_noise(pu_options, pu5_weights),
        'pu6': random_choice_with_noise(pu_options, pu6_weights),
        'pu7': random_choice_with_noise(pu_options, pu7_weights),
        'peu1': random_choice_with_noise(peu_options, peu1_weights),
        'peu2': random_choice_with_noise(peu_options, peu2_weights),
        'peu3': random_choice_with_noise(peu_options, peu3_weights),
        'peu4': random_choice_with_noise(peu_options, peu4_weights),
        'peu5': random_choice_with_noise(peu_options, peu5_weights),
        'peu6': random_choice_with_noise(peu_options, peu6_weights),
        'pc1': random_choice_with_noise(pc_options, pc1_weights),
        'pc2': random_choice_with_noise(pc_options, pc2_weights),
        'pc3': random_choice_with_noise(pc_options, pc3_weights),
        'pc4': random_choice_with_noise(pc_options, pc4_weights),
        'pc5': random_choice_with_noise(pc_options, pc5_weights),
        'pc6': random_choice_with_noise(pc_options, pc6_weights),
        'pst1': random_choice_with_noise(pst_options, pst1_weights),
        'pst2': random_choice_with_noise(pst_options, pst2_weights),
        'pst3': random_choice_with_noise(pst_options, pst3_weights),
        'pst4': random_choice_with_noise(pst_options, pst4_weights),
        'pst5': random_choice_with_noise(pst_options, pst5_weights),
        'pst6': random_choice_with_noise(pst_options, pst6_weights),
        'pst7': random_choice_with_noise(pst_options, pst7_weights),
        'pst8': random_choice_with_noise(pst_options, pst8_weights),
        'pst9': random_choice_with_noise(pst_options, pst9_weights),
        'pconv1': random_choice_with_noise(pconv_options, pconv1_weights),
        'pconv2': random_choice_with_noise(pconv_options, pconv2_weights),
        'pconv3': random_choice_with_noise(pconv_options, pconv3_weights),
        'pconv4': random_choice_with_noise(pconv_options, pconv4_weights),
        'pconv5': random_choice_with_noise(pconv_options, pconv5_weights),
        'pconv6': random_choice_with_noise(pconv_options, pconv6_weights),
        'ci1': random_choice_with_noise(ci_options, ci1_weights),
        'ci2': random_choice_with_noise(ci_options, ci2_weights),
        'ci3': random_choice_with_noise(ci_options, ci3_weights),
        'ci4': random_choice_with_noise(ci_options, ci4_weights),
        'ci5': random_choice_with_noise(ci_options, ci5_weights),
        'ci6': random_choice_with_noise(ci_options, ci6_weights)
    }
    responses.append(response)

# Save to JSON
with open('responses-b-1.json', 'w') as f:
    json.dump(responses, f, indent=2)

print("Generated 110 responses in responses-b-1.json")