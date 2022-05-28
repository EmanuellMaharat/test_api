import requests
import json
#1 

def test_dir():
    response = requests.get('https://ivolunteer-app.herokuapp.com/users/register')
    print(dir(response))

def test_status_code():
    response = requests.get('https://ivolunteer-app.herokuapp.com/users/register')
    assert response.status_code == 200

def test_json():
    r = requests.post('https://httpbin.org/post', auth=('maharatemanuel@gmail.com','12345678'))
    print(r)





