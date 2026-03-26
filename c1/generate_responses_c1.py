import pandas as pd
import json
import random
import numpy as np

# Load the CSV data
csv_path = 'c1/The Influence of Employee Motivation on Customer Satisfaction in McDonald’s Restaurants. (Responses) - Form Responses 1.csv'
df = pd.read_csv(csv_path)

# Clean column names
df.columns = df.columns.str.strip()

# Define columns for each role
employee_cols = {
    "gender": "Gender",
    "age": "Age Range",
    "education": "Education Level",
    "experience": "Working Experience",
    "employment_type": "Employment Type",
    "q1": "I feel free to undertake tasks and decisions independently at work.",
    "q2": "I feel very happy regarding pay wages compared to workload.",
    "q3": "I believe that everyone on the staff is treated equally at McDonald’s irrespective of their cast, creed, region, and religion.",
    "q4": "I can put McDonald’s on Higher ranking regarding the safety and security of staff while working at McDonald’s.",
    "q5": "My workplace is the best example of work–life balance.",
    "q6": "Working at McDonald’s is a wonderful and interesting experience."
}

customer_cols = {
    "gender": "Gender.1",
    "age": "Age Range.1",
    "employment_status": "Employment status",
    "education": "Education Level.1",
    "frequency": "How often do you eat McDonald’s?",
    "q1": "The prices at McDonald‘s are fair.",
    "q2": "McDonald‘s food tastes good.",
    "q3": "McDonald‘s meals are served quickly.",
    "q4": "McDonald‘s restaurants are clean and well taken care of.",
    "q5": "McDonalds restaurants have an appealing interior design.",
    "q6": "McDonald‘s restaurants are a comfortable place to eat in."
}

# Helper function to get distribution and sample
def get_distribution(series):
    counts = series.value_counts(normalize=True)
    return counts.index.tolist(), counts.values.tolist()

def sample_value(options, probs):
    if not options:
        return None
    return np.random.choice(options, p=probs)

# Analyze distributions
role_dist = df['Section A : Respondent Role'].value_counts(normalize=True)
roles = role_dist.index.tolist()
role_probs = role_dist.values.tolist()

employee_data = df[df['Section A : Respondent Role'] == "Employee McDonald’s"]
customer_data = df[df['Section A : Respondent Role'] == "Customer McDonald’s"]

employee_dists = {}
for key, col in employee_cols.items():
    if col in employee_data.columns:
        employee_dists[key] = get_distribution(employee_data[col].dropna())
    else:
        print(f"Warning: Column '{col}' not found for Employee")

customer_dists = {}
for key, col in customer_cols.items():
    if col in customer_data.columns:
        customer_dists[key] = get_distribution(customer_data[col].dropna())
    else:
        print(f"Warning: Column '{col}' not found for Customer")

# Generate 30 responses
generated_responses = []
for _ in range(150):
    role = sample_value(roles, role_probs)
    response = {"role": role}
    
    if role == "Employee McDonald’s":
        for key, (options, probs) in employee_dists.items():
            response[key] = sample_value(options, probs)
            # Ensure Likert values are integers (they might be read as floats)
            if key.startswith('q'):
                try:
                    response[key] = int(response[key])
                except:
                    pass
    else:
        for key, (options, probs) in customer_dists.items():
            response[key] = sample_value(options, probs)
            if key.startswith('q'):
                try:
                    response[key] = int(response[key])
                except:
                    pass
                    
    generated_responses.append(response)

# Save to JSON
with open('c1/responses_c1.json', 'w') as f:
    json.dump(generated_responses, f, indent=2, ensure_ascii=False)

print("Generated 30 responses in c1/responses_c1.json")
