#DE Ass0 - working code ver 2 - problem: subject, title, place error

# -*- coding: utf-8 -*-
import argparse
import sys
import urllib.request
import json

# Fetch data from the FBI API
def fetch_data(page):
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read())
    return data


# Load data from a local file
def load_local_data(file_location):
    try:
        # Specify encoding as 'utf-8' to handle special characters
        with open(file_location, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading the file {file_location}: {e}")
        return None


#print(data)


# Extract the title, subjects, and field offices from the data
def extract_data(data):
    records = []
    for item in data.get('items', []):
        title = item.get('title', '')  
        subjects = item.get('subjects', [])  
        field_offices = item.get('field_offices', []) 

        # Append a tuple of the title, subjects, and field offices in the correct order
        records.append((title, subjects, field_offices))
    return records


# Define a function to format the data
def format_data(records):
    thorn = 'þ'
    for title, subjects, field_offices in records:
        # Ensure subjects and field_offices are joined correctly
        subjects_str = ','.join(subjects) if subjects else ''
        field_offices_str = ','.join(field_offices) if field_offices else ''
        
        # Debugging:
        # print(f"Title: {title}")
        # print(f"Subjects: {subjects_str}")
        # print(f"Field Offices: {field_offices_str}")
        
        # Print the formatted line with thorn-separated fields in correct order
        print(f"{title}{thorn}{subjects_str}{thorn}{field_offices_str}")


# Define the main function
def main(page=None, thefile=None):
    if page is not None:
        data = fetch_data(page)
    elif thefile is not None:
        data = load_local_data(thefile)
    else:
        print("Error: No data source specified.", file=sys.stderr)
        sys.exit(1)
    
    #Debugging
    # print(data)

    records = extract_data(data)
    format_data(records)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetch and process FBI Wanted data.")
    parser.add_argument("--page", type=int, help="Page number to fetch from the FBI API.")
    parser.add_argument("--file", type=str, help="Local JSON file to process.")
    args = parser.parse_args()

    if args.page is not None:
        main(page=args.page)
    elif args.file is not None:
        main(thefile=args.file)
    else:
        parser.print_help(sys.stderr)
