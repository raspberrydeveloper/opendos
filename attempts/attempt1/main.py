import threading
import requests
import time

url = "https://example.com" # Replace with your desired URL
data = {"key": "value"} # Replace with your desired POST data

def make_request():
    while True:
        try:
            response = requests.post(url, data=data)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(e)
        time.sleep(0.001) # Sleep for 1 millisecond

# Create 10 threads to make the requests
for i in range(10):
    thread = threading.Thread(target=make_request)
    thread.start()
