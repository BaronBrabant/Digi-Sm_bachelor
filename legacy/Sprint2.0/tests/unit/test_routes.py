import pytest
from my_app import routes
from flask import Flask
from my_app import app

client = app.test_client()

def test_home_route():
    
    response = client.get('/')
    assert response.status_code == 302
    
    

def test_home_page():

    # Create a test client using the Flask application configured for testing
    with client as test_client:
        response = test_client.get('/')
        assert response.status_code == 302
        print(response.data)
        #assert b"Welcome to the" in response.data
        #assert b"Flask User Management Example!" in response.data
        #assert b"Need an account?" in response.data
        #assert b"Existing user?" in response.data
 
 
def test_newTask_route():

    # Create a test client using the Flask application configured for testing
    with client as test_client:
        response = test_client.post('/newTask')
        
        assert response.status_code == 302
       
           
def test