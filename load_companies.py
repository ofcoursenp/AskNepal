import json

# Load JSON data from file
with open(r'tech-companies\data\companies.json', 'r') as file:
    data = json.load(file)

# Extract and print company information
for company in data['companies']:
    print(f"Company Name: {company['name']}")
    file_name = 'boderlines_train.txt'
    text_content = f"where is {company['name']} \nwhat is {company['name']}\ncan u show details of {company['name']}\n"
    with open(file_name, 'a') as file:
        # Write the text content to the file
        file.write(text_content)
    print(f"  Logo Name: {company['logoName']}")
    print(f"  Established At: {company['establishedAt']}")
    print(f"  Location: {company['location']}")
    print(f"  Website: {company['website']}")
    print(f"  Email: {company['email']}")
    print(f"  Phone: {company['phone']}")
    print("  Socials:")
    for social, link in company['socials'].items():
        print(f"    - {social.capitalize()}: {link}")
    print()
