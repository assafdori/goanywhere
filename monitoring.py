import requests
from requests.auth import HTTPBasicAuth

# Replace with actual API URL for GoAnywhere Agent status
api_url = "https://goanywhere-instance/api/agents/status"

# Authentication (Basic Auth) - replace with your actual credentials
username = "your_username"
password = "your_password"

# Or, if you are using an API token instead of Basic Auth:
# headers = {
#     'Authorization': 'Bearer YOUR_API_TOKEN',
#     'Content-Type': 'application/json'
# }

def check_agent_status():
    try:
        # Using basic authentication
        response = requests.get(api_url, auth=HTTPBasicAuth(username, password))
        
        # If you're using token-based auth, use the following instead
        # response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()  # Assuming the response is in JSON format
            print("Agent Status:", data)
            # Perform further checks on the status (e.g., look for 'status' field)
            if data.get('status') == 'online':
                print("Agent is online and healthy.")
            else:
                print("Agent is not online. Status:", data.get('status'))
        else:
            print(f"Failed to retrieve agent status. HTTP Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with GoAnywhere API: {e}")

if __name__ == "__main__":
    check_agent_status()
