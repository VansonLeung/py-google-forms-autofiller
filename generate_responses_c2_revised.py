import pandas as pd
import json
import random
import numpy as np

# Load the CSV data
csv_path = 'c2/revised.csv'
df = pd.read_csv(csv_path)

# Clean column names
df.columns = df.columns.str.strip()

# Mapping for Likert scale text to numbers
likert_map = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5
}

# Employee Columns
employee_demographics = {
    "gender": "Gender",
    "age": "Age Range",
    "education": "Education Level",
    "experience": "Working Experience",
    "employment_type": "Employment Type"
}

employee_questions = [
    "The McDonald’s work environment supports me in handling mental health challenges.",
    "McDonald’s provides a high level of safety and security for me while working.",
    "The quality of work and overall efficiency are negatively affected in a toxic work environment.",
    "My workplace is an excellent example of work-life balance.",
    "I feel very happy regarding the pay wages while comparing to workload at McDonald’s.",
    "I receive incentives and words of appreciation when I perform my best during my shift.",
    "I feel the company is concerned about my personal welfare and interests.",
    "I am satisfied with McDonald’s benefits package, including vacation, sick leave, transportation allowance, etc.",
    "I feel recognized by my managers for my work contributions.",
    "I am able to make important decisions independently in my role.",
    "My managers treat all employees fairly and without bias.",
    "I feel supported by my supervising managers when performing my tasks.",
    "I believe that everyone on the staff is treated equally at McDonald’s irrespective of their cast, creed, region, and religion.",
    "I am encouraged to share my ideas and contribute to improving work processes.",
    "I have never experienced gender inequality at McDonald’s.",
    "Overall, how satisfied are you working in McDonald's Sungai Dua, Penang?"
]

# Map CSV columns to questions
# The CSV columns have prefixes like "Work Environment [...]"
# We need to find the column that contains the question text
employee_col_map = {}
for col in df.columns:
    for q in employee_questions:
        if q in col:
            employee_col_map[q] = col
            break

# Customer Columns
# Note: Customer columns start around index 23 in the CSV
# We need to identify them carefully.
# Based on previous analysis:
customer_demographics = {
    "gender": "Gender.1",
    "age": "Age Range.1",
    "employment_status": "Employment status",
    "education": "Education Level.1",
    "frequency": "How often do you eat McDonald’s?"
}

customer_questions = [
    "McDonald‘s have clean and comfortable physical environment",
    "McDonalds restaurants have an appealing interior design.",
    "McDonald‘s restaurants are clean and well taken care of.",
    "McDonald‘s employees are well dressed and appear neat",
    "When McDonald‘s  promise to do something by a certain time, they do it.",
    "When customer has a problem,  McDonald‘s show sincere interest in solving the problem.",
    "McDonald‘s perform the service right the first time.",
    "McDonald‘s provide their services at the time they promise to do so",
    "McDonald‘s make information easily obtainable by customers.",
    "McDonald‘s meals are served quickly.",
    "McDonald‘s employees are always willing to help customers.",
    "McDonalds employees are never too busy to respond to customers requests.",
    "The behaviour of McDonald’s employees instill confidence in customers.",
    "Customers feel safe and comfortable when interacting with McDonald’s staff.",
    "McDonald’s employees are polite and friendly to customers.",
    "McDonald’s employees have the knowledge to answer customers’ questions about the menu, promotions, and services.",
    "McDonald‘s give customers individual attention.",
    "Operating hours of McDonald‘s are convenient to customers.",
    "McDonald‘s have their customers' interest at heart.",
    "Employees of McDonald's understand the specific needs of their customers.",
    "McDonald‘s restaurants are a comfortable place to eat in."
]

# Helper function to get distribution and sample
def get_distribution(series):
    counts = series.value_counts(normalize=True)
    return counts.index.tolist(), counts.values.tolist()

def sample_value(options, probs):
    if not options:
        return None
    return np.random.choice(options, p=probs)

# Separate Data
employee_data = df[df['Section A : Respondent Role'] == "Employee McDonald’s"]
customer_data = df[df['Section A : Respondent Role'] == "Customer McDonald’s"]

# Analyze Employee Distributions
employee_dists = {}
for key, col in employee_demographics.items():
    if col in employee_data.columns:
        employee_dists[key] = get_distribution(employee_data[col].dropna())
    else:
        print(f"Warning: Employee Column '{col}' not found")

for q in employee_questions:
    col = employee_col_map.get(q)
    if col and col in employee_data.columns:
        # Map text to numbers if needed
        series = employee_data[col].dropna()
        # Check if values are text
        if series.dtype == 'object':
            # Try mapping
            mapped_series = series.map(likert_map)
            # If mapping failed (NaNs), maybe it's already numbers or different text?
            # For "Overall satisfaction", it might be numbers.
            if mapped_series.isna().all():
                 # Maybe it's numbers as strings?
                 try:
                     mapped_series = series.astype(int)
                 except:
                     print(f"Warning: Could not map values for '{col}': {series.unique()}")
                     continue
            series = mapped_series
        
        employee_dists[q] = get_distribution(series)
    else:
        print(f"Warning: Employee Question Column for '{q}' not found")

# Analyze Customer Distributions
customer_dists = {}
for key, col in customer_demographics.items():
    if col in customer_data.columns:
        customer_dists[key] = get_distribution(customer_data[col].dropna())
    else:
        print(f"Warning: Customer Column '{col}' not found")

for q in customer_questions:
    if q in customer_data.columns:
        customer_dists[q] = get_distribution(customer_data[q].dropna())
    else:
        print(f"Warning: Customer Question Column '{q}' not found")

# Generate Responses
generated_responses = []

# Generate 20 Employees
print("Generating 20 Employees...")
for _ in range(20):
    response = {"role": "Employee McDonald’s"}
    # Demographics
    for key, (options, probs) in employee_dists.items():
        if key in employee_demographics:
            response[key] = sample_value(options, probs)
    
    # Questions
    for q in employee_questions:
        if q in employee_dists:
            options, probs = employee_dists[q]
            val = sample_value(options, probs)
            response[q] = int(val) if val is not None else 3 # Default to 3 if missing
            
    generated_responses.append(response)

# Generate 135 Customers
print("Generating 135 Customers...")
for _ in range(135):
    response = {"role": "Customer McDonald’s"}
    # Demographics
    for key, (options, probs) in customer_dists.items():
        if key in customer_demographics:
            response[key] = sample_value(options, probs)
            
    # Questions
    for q in customer_questions:
        if q in customer_dists:
            options, probs = customer_dists[q]
            val = sample_value(options, probs)
            response[q] = int(val) if val is not None else 3
            
    generated_responses.append(response)

# Shuffle
random.shuffle(generated_responses)

# Save
output_file = 'c2/responses.json'
with open(output_file, 'w') as f:
    json.dump(generated_responses, f, indent=2, ensure_ascii=False)

print(f"Generated {len(generated_responses)} responses in {output_file}")
