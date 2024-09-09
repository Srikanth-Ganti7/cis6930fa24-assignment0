import pytest
import main

# Define the path to your local data file
local_file_path = 'C:/ganti.b/SEM3/DE/cis6930fa24-assignment0/loadfile'

# Test to ensure data is loaded and non-empty from the local file
def test_load_data():
    data = main.load_local_data(local_file_path)
    assert 'items' in data  
    assert isinstance(data['items'], list)  
    assert len(data['items']) > 0  

# Test extracting title from the local file data
def test_extract_title():
    data = main.load_local_data(local_file_path)
    item = data['items'][0] 
    assert 'title' in item  
    assert isinstance(item['title'], str)  

# Test extracting subjects from the local file data
def test_extract_subjects():
    data = main.load_local_data(local_file_path)
    item = data['items'][0]  
    assert 'subjects' in item  
    assert isinstance(item['subjects'], list)  

# Test extracting field offices from the local file data
def test_extract_field_offices():
    data = main.load_local_data(local_file_path)
    item = data['items'][0]
    
    # Ensure 'field_offices' exists and is not None
    if 'field_offices' in item and item['field_offices'] is not None:
        assert isinstance(item['field_offices'], list)
    else:
        assert False, "'field_offices' is either missing or None"

# Test to print thorn-separated fields from the local file data
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
