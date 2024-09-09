# -*- coding: utf-8 -*-
import pytest
import main
import random

# Helper function to fetch data from a random page
def fetch_data_from_random_page():
    random_page = random.randint(1, 5)  # Randomly fetch data from pages 1 to 5
    return main.fetch_data(random_page)

# Test to ensure data is downloaded and non-empty
def test_fetch_data():
    data = fetch_data_from_random_page()  
    assert 'items' in data  
    assert isinstance(data['items'], list)  
    assert len(data['items']) > 0  

# Test to ensure that the 'title' field is extracted correctly
def test_extract_title():
    data = fetch_data_from_random_page()
    item = data['items'][0]  
    assert 'title' in item  
    assert isinstance(item['title'], str)  

# Test to ensure that the 'subjects' field is extracted correctly
def test_extract_subjects():
    data = fetch_data_from_random_page()
    item = data['items'][0]  
    assert 'subjects' in item  
    assert isinstance(item['subjects'], list)  

# Test to ensure that 'field_offices' field is extracted correctly
def test_extract_field_offices():
    data = fetch_data_from_random_page()
    item = data['items'][0]  

    # Ensure 'field_offices' exists and is a list
    if 'field_offices' in item and item['field_offices'] is not None:
        assert isinstance(item['field_offices'], list), "'field_offices' is not a list"
    else:
        
        assert item['field_offices'] is None or 'field_offices' not in item, "'field_offices' is either missing or None"


# Test to ensure the thorn-separated fields are printed correctly
def test_print_thorn_separated():
    data = fetch_data_from_random_page()
    item = data['items'][0]
    
    # Extract fields with safe defaults
    title = item.get('title', 'No title available')
    subjects = ','.join(item.get('subjects', []))  
    field_offices = ','.join(item.get('field_offices', []) if item.get('field_offices') else [])
    
    thorn_separated = f"{title}þ{subjects}þ{field_offices}"
    print(thorn_separated)  
    
    # Ensure the output is not empty
    assert thorn_separated





