import pandas as pd
import numpy as np
from collections import Counter

# Read the CSV file
df = pd.read_csv('/Users/van/Downloads/xls/Exploring the factors that influence the cybersecurity behaviors of young adults Group36 (Responses).xlsx - Form Responses 1.csv')

# Display basic info
print("Shape:", df.shape)
print("Columns:", list(df.columns))

# Analyze demographics
print("\n=== Demographics ===")
demo_cols = ['1. Gender: ', '2. Age：  ', '3.What is your ethnicity? ', '4.What is your nationality?', '5.Currently, what year of study are you in? ', '6. Which school are you from? (e.g., School of Management) ', '7. How many years of experience do you have in using the internet? ', '8. How many hours do you spend using the internet each day? ']
for col in demo_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze CSB Adoption
print("\n=== CSB Adoption ===")
csb_cols = ['Cybersecurity Behaviors (CSB) Adoption [Do you use antivirus software on your computer?]', 'Cybersecurity Behaviors (CSB) Adoption [Do you use two-factor authentication (e.g., 2-Step Verification) for at least one of your online accounts?]']
for col in csb_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze Frequency of CSB
print("\n=== Frequency of CSB ===")
freq_cols = [col for col in df.columns if 'Frequency of Cybersecurity Behaviors (CSB)' in col]
for col in freq_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze Skills
print("\n=== Skills Level ===")
skill_cols = [col for col in df.columns if 'Skills Level (SK)' in col]
for col in skill_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze Knowledge
print("\n=== Knowledge of Cyber Threats ===")
know_cols = [col for col in df.columns if 'Knowledge of Cyber Threats (KCT)' in col]
for col in know_cols:
    print(f"{col}: {Counter(df[col].dropna())}")

# Analyze other sections
sections = {
    'IPC': 'Intention to Practice Cyber Security (IPC)',
    'ATT': 'Attitude toward Cyber Security Behavior (practices) (ATT)',
    'SN': 'Subjective Norms (social influence) (SN)',
    'PBC': 'Perceived Behavioral Control (self-efficacy and controllability) (PBC)',
    'PACT': 'Perceived Awareness of Cyber Threats (PACT)'
}

for abbr, prefix in sections.items():
    print(f"\n=== {abbr} ===")
    cols = [col for col in df.columns if prefix in col]
    for col in cols:
        print(f"{col}: {Counter(df[col].dropna())}")

print("\n=== Suggestions ===")
print(Counter(df['Any suggestions'].dropna()))