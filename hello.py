# hello.py - A simple Python script
print("Hello, world!")
import requests

# Replace with your raw URL
raw_url = "https://raw.githubusercontent.com/23Raakd831/OUSL001/refs/heads/main/hello.py"

response = requests.get(raw_url)

if response.status_code == 200:
    print("Script fetched successfully!")
    print("Script content:\n")
    print(response.text)
else:
    print("Failed to fetch the script. Status code:", response.status_code)
with open("fetched_script_output.txt", "w") as file:
    file.write(response.text)
print("Script content saved to 'fetched_script_output.txt'")
