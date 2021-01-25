import requests


def add_permit():
    url = "http://127.0.0.1:8080/accesscontrol/addpermit"

    payload = "    {\n    \"cardNumber\":19665490,\n    \"controlSN\":125029221,\n    \"controlIP\":\"169.254.18.28\"\n    }"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text
