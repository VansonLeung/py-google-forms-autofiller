import pandas as pd
import json
import re

def extract_question_text(header):
    # Extract text inside [] if present, else return header
    match = re.search(r'\[(.*?)\]', header)
    if match:
        return match.group(1).strip()
    return header.strip()

def convert_csv_to_json():
    csv_path = 'c3/The Influence of Employee Motivation on Customer Satisfaction in McDonald’s Restaurants. (Responses) - Form Responses 1-3.csv'
    
    # Read CSV with pandas to handle parsing easily
    # We need to handle duplicate columns. pandas might mangle them (Gender, Gender.1)
    df = pd.read_csv(csv_path)
    
    # Identify columns
    # Employee columns are roughly the first set
    # Customer columns are the second set
    
    # Let's inspect columns to find the split point
    # "Section A : Respondent Role" is index 1
    
    # Employee Demographics
    emp_gender_col = "Gender"
    emp_age_col = "Age Range"
    emp_edu_col = "Education Level"
    emp_exp_col = "Working Experience " # Note space
    emp_type_col = "Employment Type"
    
    # Customer Demographics (likely have .1 suffix if pandas loaded them)
    cust_gender_col = "Gender.1"
    cust_age_col = "Age Range.1"
    cust_status_col = "Employment status"
    cust_edu_col = "Education Level.1"
    cust_freq_col = "  How often do you eat McDonald’s?  "
    
    responses = []
    
    for index, row in df.iterrows():
        role = row["Section A : Respondent Role"]
        
        response = {}
        response["role"] = role
        
        if role == "Employee McDonald’s":
            # Demographics
            response["gender"] = row[emp_gender_col]
            response["age"] = row[emp_age_col]
            response["education"] = row[emp_edu_col]
            response["experience"] = row[emp_exp_col]
            response["employment_type"] = row[emp_type_col]
            
            # Questions
            # Iterate through columns that look like "Category [Question]"
            for col in df.columns:
                if "[" in col and "]" in col:
                    # Check if it's an Employee question column (usually before Customer columns)
                    # But pandas might mix them if not careful.
                    # The CSV structure showed Employee questions come before Customer demographics.
                    # Let's rely on the fact that Employee rows have values in these columns
                    val = row[col]
                    if pd.notna(val) and str(val).strip() != "":
                        q_text = extract_question_text(col)
                        # Map "Strongly agree" to "Strongly Agree" (Capitalize)
                        if isinstance(val, str):
                            val = val.capitalize() # "Strongly agree" -> "Strongly agree" -> wait, "Strongly Agree" is title case
                            if val.lower() == "strongly agree": val = "Strongly Agree"
                            elif val.lower() == "agree": val = "Agree"
                            elif val.lower() == "neutral": val = "Neutral"
                            elif val.lower() == "disagree": val = "Disagree"
                            elif val.lower() == "strongly disagree": val = "Strongly Disagree"
                        
                        response[q_text] = val
                
                elif col.strip() == "Overall, how satisfied are you working in McDonald's Sungai Dua, Penang?":
                    val = row[col]
                    if pd.notna(val) and str(val).strip() != "":
                        response[col.strip()] = int(val) if isinstance(val, (int, float)) or str(val).isdigit() else val
                        
        elif role == "Customer McDonald’s":
            # Demographics
            response["gender"] = row[cust_gender_col]
            response["age"] = row[cust_age_col]
            response["employment_status"] = row[cust_status_col]
            response["education"] = row[cust_edu_col]
            response["frequency"] = row[cust_freq_col]
            
            # Questions
            # Customer questions are plain text headers, usually after demographics
            # We can list them or detect them.
            # They seem to be columns that are NOT demographics and NOT Employee questions.
            # And they have values for Customer rows.
            
            # Let's explicitly list known customer questions or detect them
            # Based on previous file, we know the questions.
            # Or we can just take all columns that have values and are not demographics/role.
            
            for col in df.columns:
                # Skip known demographics and role
                if col in [cust_gender_col, cust_age_col, cust_status_col, cust_edu_col, cust_freq_col, 
                           emp_gender_col, emp_age_col, emp_edu_col, emp_exp_col, emp_type_col, 
                           "Section A : Respondent Role", "Timestamp"]:
                    continue
                
                # Skip Employee questions (with brackets)
                if "[" in col and "]" in col:
                    continue
                
                val = row[col]
                if pd.notna(val) and str(val).strip() != "":
                    # This is likely a customer question
                    # Clean header
                    q_text = col.strip()
                    response[q_text] = int(val) if isinstance(val, (int, float)) else val

        responses.append(response)
        
    with open('c3/responses.json', 'w') as f:
        json.dump(responses, f, indent=2, ensure_ascii=False)
    
    print(f"Converted {len(responses)} responses to c3/responses.json")

if __name__ == "__main__":
    convert_csv_to_json()
