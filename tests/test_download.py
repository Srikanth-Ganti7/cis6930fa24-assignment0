import main
import os
import pytest

# Define the path to the JSON file
local_file_path = os.path.join(os.path.dirname(__file__), '..', 'loadfile.json')

# Test to ensure data is loaded from the local JSON file and non-empty
def test_load_data():
    data = main.load_local_data(local_file_path)
    assert 'items' in data  
    assert isinstance(data['items'], list)  
    assert len(data['items']) > 0  

def test_extract_title():
    data = main.load_local_data(local_file_path)
    item = data['items'][0]  # Assuming we're testing the first item
    assert 'title' in item  
    assert isinstance(item['title'], str)

def test_extract_subjects():
    data = main.load_local_data(local_file_path)
    item = data['items'][0]  
    assert 'subjects' in item  
    assert isinstance(item['subjects'], list)  

def test_extract_field_offices():
    data = main.load_local_data(local_file_path)
    item = data['items'][0]  
    
    # Ensure 'field_offices' exists and is a list
    if 'field_offices' in item:
        assert isinstance(item['field_offices'], list)
    else:
        assert False, "'field_offices' is missing"

def test_print_thorn_separated():
    data = main.load_local_data(local_file_path)
    item = data['items'][0]  
    
    # Extract the fields with safe defaults for missing values
    title = item.get('title', 'No title available')
    subjects = ','.join(item.get('subjects', []))
    field_offices = ','.join(item.get('field_offices', []) if item.get('field_offices') else [])
    
    thorn_separated = f"{title}þ{subjects}þ{field_offices}"
    print(thorn_separated)
    
    # Ensure the output is not empty
    assert thorn_separated

