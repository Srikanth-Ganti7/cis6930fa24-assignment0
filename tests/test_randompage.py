import pytest
import main
import random

def test_random_page_fetch():
    random_page = random.randint(1, 5)
    data = main.fetch_data(random_page)
    assert 'items' in data
    assert isinstance(data['items'], list)
    assert len(data['items']) > 0
