import pandas as pd
import numpy as np
from collections import Counter

# Read the CSV file
df = pd.read_csv('/Users/van/Downloads/xls/From Cashless to Contactless _ Exploring Consumer Behavior Towards QR Code Payments in Malaysia’s Technology Industry (Responses) - Form Responses 1.csv')

# Display basic info
# print("Shape:", df.shape)
# print("Columns:")
# for i, col in enumerate(df.columns):
#     print(f"{i}: '{col}'")

# Analyze demographics
print("\n=== Demographics ===")
demo_cols = ['Gender', 'Age', 'Employment Status', 'Education Level']
for col in demo_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze usage patterns
print("\n=== Usage Patterns ===")
usage_cols = ['Are you a user of the Touch ‘n Go e-wallet?', '1. Frequency of Using Touch ’n Go eWallet Services', '2. For what purpose do you primarily use Touch ’n Go eWallet? \n(Select all that apply)', '3. How much do you spend on average per month with Touch ‘n Go e-wallet?', '4. How long have you been using Touch ’n Go eWallet?']
for col in usage_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze satisfaction and issues
print("\n=== Satisfaction and Issues ===")
sat_cols = ['5. How satisfied are you with the rewards and cashback programs provided by Touch ’n Go eWallet?', '6. How often do you encounter technical issues when making payment via Touch ’n Go QR code?', '7. Do you feel that Touch ’n Go eWallet has improved your overall shopping or payment experience?']
for col in sat_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze importance and likelihood
print("\n=== Importance and Likelihood ===")
imp_cols = ['8. How important is the availability of Touch ’n Go eWallet at merchants and service providers to your decision to use it?', '9. How likely are you to explore and use new features or services introduced in the Touch ’n Go eWallet app?']
for col in imp_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze alternatives
print("\n=== Alternative Payment Methods ===")
print("10. Which alternative payment methods do you often use besides Touch ’n Go eWallet? (Select all that apply):", Counter(df['10. Which alternative payment methods do you often use besides Touch ’n Go eWallet? (Select all that apply)'].dropna()))

# Analyze Likert scale sections
sections = {
    'Perceived Usefulness': [col for col in df.columns if 'Perceived Usefulness' in col],
    'Perceived Ease of Use': [col for col in df.columns if 'Perceived Ease of Use' in col],
    'Perceived Compatibility': [col for col in df.columns if 'Perceived Compatibility' in col],
    'Perceived Security and Trust': [col for col in df.columns if 'Perceived Security and Trust' in col],
    'Perceived Convenience': [col for col in df.columns if 'Perceived Convenience' in col],
    'Consumer Intention': [col for col in df.columns if 'Consumer Intention' in col]
}

for abbr, cols in sections.items():
    print(f"\n=== {abbr} ===")
    for col in cols:
        print(f"{col}: {Counter(df[col].dropna())}")