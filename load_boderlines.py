import json

# Load JSON data from file
with open(r'borderlines\borderlines.json', 'r') as file:
    data = json.load(file)

# Extract and print city information
for city in data['cities']:
    print(f"City: {city['name']}")

    file_name = 'boderlines_train.txt'
    text_content = f"where is {city['name']} \nwhat is {city['name']}\ncan u show details of {city['name']}\n"
    with open(file_name, 'a') as file:
        # Write the text content to the file
        file.write(text_content)
# The file is automatically closed after the 'with' block
    print(f'Text has been written to {file_name}')
    print(f"  Latitude: {city['latitude']}")
    print(f"  Longitude: {city['longitude']}")
    print(f"  Timezone: {city['timezone']}")
    print(f"  Official Language: {city['officialLanguage']}")
    print(f"  Currency: {city['currency']['name']} ({city['currency']['code']})")
    print(f"  Land Area: {city['landArea']['value']} {city['landArea']['unit']}")
    print(f"  Elevation: {city['elevation']['value']} {city['elevation']['unit']}")
    if 'landmarks' in city:
        print(f"  Landmarks:")
        for landmark in city['landmarks']:
            print(f"    - {landmark['name']} (Lat: {landmark['latitude']}, Lon: {landmark['longitude']})")
    print()
