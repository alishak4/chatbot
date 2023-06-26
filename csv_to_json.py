import csv
import json

csv_file = 'corpus.csv'
json_file = 'intents2.json'

# Load data from the CSV file
data = []
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        question = row[0]
        response = row[1]
        data.append({'question': question, 'response': response})

# Write data to the intents.json file
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)
