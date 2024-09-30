import requests
import uuid
base_url = "http://127.0.0.1:8000"

def test_register_user():
    user_id = uuid.uuid4().int
    data = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "password123",
        "vector": [0.1] * 128
    }
    response = requests.post(f"{base_url}/register", json=data)
    print(response.json())

def test_update_user():
    data = {
        "username": "updated_user",
        "email": "updated@example.com",
        "password": "newpassword123",
        "vector": [0.2] * 128
    }
    response = requests.put(f"{base_url}/update/1", json=data)
    print(response.json())

def test_search_user():
    vector = [0.1] * 128
    response = requests.post(f"{base_url}/search", json={"user_vector": vector})
    print(response.json())


def test_retrieve_user():
    response = requests.get(f"{base_url}/retrieve/1")
    print(response.json())

def test_delete_user():
    response = requests.delete(f"{base_url}/delete/1")
    print(response.json())



if __name__ == "__main__":
    test_register_user()
    test_update_user()
    test_search_user()
    test_retrieve_user()
    # test_delete_user()
  
