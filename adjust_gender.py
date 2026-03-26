import json
import math
import random

input_file = 'c3/responses_random.json'
output_file = 'c3/responses_random_2.json'

with open(input_file, 'r') as f:
    data = json.load(f)

# Filter customers
# Matching "Customer McDonald" to handle potential variations, though we saw "Customer McDonald’s"
customers_indices = [i for i, r in enumerate(data) if "Customer McDonald" in r.get('role', '')]
total_customers = len(customers_indices)

print(f"Total customers found: {total_customers}")

# Target: 40% Male, 60% Female
target_males = int(total_customers * 0.40)
print(f"Target males: {target_males} (40%)")

# Assign genders
# Since the input is randomized, we can just iterate through the customers found
males_assigned = 0
for idx in customers_indices:
    if males_assigned < target_males:
        data[idx]['gender'] = 'Male'
        males_assigned += 1
    else:
        data[idx]['gender'] = 'Female'

print(f"Assigned {males_assigned} males and {total_customers - males_assigned} females.")

# Shuffle the data to mix the genders naturally
random.shuffle(data)

with open(output_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Saved to {output_file}")
