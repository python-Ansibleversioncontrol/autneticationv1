import requests

# Get the server IP from the user
server_ip = input("Enter the server IP: ")

# Form the API URL using the server IP and endpoint
api_url = "https://{}/api/v1/fileset".format(server_ip) # Modify the endpoint according to your API

# Make the API call to retrieve the fileset information
response = requests.get(api_url)

# Parse the API response to obtain the fileset data
fileset_data = response.json()

# Sort the fileset data based on file size in descending order
sorted_fileset = sorted(fileset_data, key=lambda x: x["file_size"], reverse=True)

# Fetch the input of each file in the sorted fileset
for file_data in sorted_fileset:
    file_id = file_data["file_id"]
    file_name = file_data["file_name"]
    file_size = file_data["file_size"]

    # Process the file input as desired
    print("File ID: {file_id}, File Name: {file_name}, File Size: {file_size}")
~                                                                                                                                                                                                                                                  
~                                        