import json

# Load JSON data from file
with open(r'government-websites\websites.json', 'r') as file:
    data = json.load(file)

# Extract and print item information
for item in data['items']:
    print(f"Website Name: {item['name']}")
    file_name = 'train.txt'
    text_content = f"can u show detail of {item['name']}website\nwhat is {item['name']}\n"
    with open(file_name, 'a') as file:
        # Write the text content to the file
        file.write(text_content)
    print(f"  URL: {item['url']}")
    print(f"  Description: {item['description']}")
    print()

