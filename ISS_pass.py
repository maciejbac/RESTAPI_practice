# This program checks with the API to estimate when is the next time ISS will fly over London
#
# Import liobrary used to sent HTTP requests
import requests

# Pass save required parameters (Latitude and longitude) into a variable, 51N 0.3E is the approximate location of London 
query = {'lat':'51', 'lon':'0.3'}
# Send an API call to the REST API, passing my query variable as a 2nd argument to filter the results
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)

# Print the contents of the returned json file
print(response.json())



