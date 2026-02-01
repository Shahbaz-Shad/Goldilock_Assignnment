"""Write a program to call a HTTP URL and print the output
a. URL is http://127.0.0.1:8999/test?value=p""" 

import requests

def call_http_url():
    url = "https://www.youtube.com/watch?v=YXbPbPZBZ-w"
    params = {"value": "p"}

    try:
        response = requests.get(url, params=params, timeout=5)

        if response.status_code == 200:
            print("Response from server:")
            print(response.text)
        else:
            print(f"HTTP Error: Status Code {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server")
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

call_http_url()
