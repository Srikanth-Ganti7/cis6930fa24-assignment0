# -*- coding: utf-8 -*-
import pytest
import main

# Test to ensure data is downloaded and non-empty
def test_fetch_data():
    
    data = main.fetch_data(1)
    assert 'items' in data  
    assert isinstance(data['items'], list)  
    assert len(data['items']) > 0  

# Test extracting title from FBI API data
def test_extract_title():
    
    data = main.fetch_data(1)
    item = data['items'][0] 
    assert 'title' in item  
    assert isinstance(item['title'], str)  

# Test extracting subjects from FBI API data
def test_extract_subjects():
    
    data = main.fetch_data(1)
    item = data['items'][0]  
    assert 'subjects' in item  
    assert isinstance(item['subjects'], list)  

# Test extracting field_offices from FBI API data
def test_extract_field_offices():
    
    data = main.fetch_data(1)
    item = data['items'][0]  
    assert 'field_offices' in item  
    assert isinstance(item['field_offices'], list)  

# Test to print thorn-separated fields
def test_print_thorn_separated():
    
    data = main.fetch_data(1)
    item = data['items'][0]  
    title = item['title']
    subjects = ','.join(item['subjects']) if 'subjects' in item else ''
    field_offices = ','.join(item['field_offices']) if 'field_offices' in item else ''
    thorn_separated = f"{title}þ{subjects}þ{field_offices}"
    print(thorn_separated)
    assert thorn_separated  