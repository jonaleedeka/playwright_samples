from playwright.sync_api import Page

BASE_URL = "http://127.0.0.1:8000/"

def test_index(page:Page):
    response = page.goto(BASE_URL)
    assert response.ok