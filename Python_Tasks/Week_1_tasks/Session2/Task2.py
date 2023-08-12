import requests

def get_ip_info():
    response = requests.get("https://ipinfo.io/json")
    
    if response.status_code == 200:
        data = response.json()
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve IP information.")

get_ip_info()
