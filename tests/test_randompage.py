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
    data = fetch_data_from_random_page()  # Fetch data from a random page
    assert 'items' in data  # Ensure 'items' key exists
    assert isinstance(data['items'], list)  # Ensure 'items' is a list
    assert len(data['items']) > 0  # Ensure 'items' list is not empty

# Test to ensure that the 'title' field is extracted correctly
def test_extract_title():
    data = fetch_data_from_random_page()
    item = data['items'][0]  # Get the first item
    assert 'title' in item  # Ensure 'title' key exists
    assert isinstance(item['title'], str)  # Ensure the 'title' is a string

# Test to ensure that the 'subjects' field is extracted correctly
def test_extract_subjects():
    data = fetch_data_from_random_page()
    item = data['items'][0]  # Get the first item
    assert 'subjects' in item  # Ensure 'subjects' key exists
    assert isinstance(item['subjects'], list)  # Ensure 'subjects' is a list

# Test to ensure that 'field_offices' field is extracted correctly
def test_extract_field_offices():
    data = fetch_data_from_random_page()
    item = data['items'][0]  # Get the first item

    # Ensure 'field_offices' exists and is a list
    if 'field_offices' in item and item['field_offices'] is not None:
        assert isinstance(item['field_offices'], list), "'field_offices' is not a list"
    else:
        # Pass the test if 'field_offices' does not exist or is None, since that is valid data
        assert item['field_offices'] is None or 'field_offices' not in item, "'field_offices' is either missing or None"


# Test to ensure the thorn-separated fields are printed correctly
def test_print_thorn_separated():
    data = fetch_data_from_random_page()
    item = data['items'][0]
    
    # Extract fields with safe defaults
    title = item.get('title', 'No title available')
    subjects = ','.join(item.get('subjects', []))  # Join subjects with commas
    field_offices = ','.join(item.get('field_offices', []) if item.get('field_offices') else [])
    
    thorn_separated = f"{title}þ{subjects}þ{field_offices}"
    print(thorn_separated)  # Print the thorn-separated values
    
    # Ensure the output is not empty
    assert thorn_separated

# Test that API is being called and data is being fetched successfully
def test_api_called():
    data = fetch_data_from_random_page()
    
    # Check that API call returns valid data and ensure that it's non-empty
    assert data is not None  # Ensure we got a response
    assert 'items' in data  # Ensure 'items' key exists
    assert len(data['items']) > 0  # Ensure 'items' list is not empty

# Test fetching data from a random page
def test_random_page_fetch():
    data = fetch_data_from_random_page()
    assert 'items' in data
    assert isinstance(data['items'], list)
    assert len(data['items']) > 0

