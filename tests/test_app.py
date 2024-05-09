from playwright.sync_api import Page, expect
import pytest
from lib.database_connection import DatabaseConnection
# Tests for your routes go here

"""
We can render the index page
"""


def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")

""" 
Once a username and password that is submitted matches with the database
we should reach the landing page/dashboard at spaces.html

"""
def test_once_logged_in_riderect_to_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/Login")
    
    page.click("text='Login'")
    
    button = page.locator('login-button')
    expect(button).to_have_text('LOGIN')
    page.fill("input[name=email]", "ben@gmail.com")
    page.fill("input[name=password]", "Password123!")
    
    # page.fill("input[name=title]", "Test Album")
    # page.fill("input[name=release_year]", "2024")
    # page.fill('input[name=artist_id]', "1")
    # page.click("text='Add Album'")
    # page.goto(f'http://{test_web_address}/albums')
    # h2_tags = page.locator('h2')
    # p_tags = page.locator('p')
    # expect(h2_tags).to_have_text(["Title: Doolittle ", "Title: Surfer Rosa ", "Title: Test Album"])
    # expect(p_tags).to_have_text(['Released: 1989', 'Released: 1988', 'Released: 2024'])