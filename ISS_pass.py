# This program checks with the API to estimate when is the next time ISS will fly over London
#
# Import library used to sent HTTP requests
import requests
import datetime
# Pass save required parameters (Latitude and longitude) into a variable, 51N 0.3E is the approximate location of London
query = {'lat':'51', 'lon':'0.3'}
# Send an API call to the REST API, passing my query variable as a 2nd argument to filter the results
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
# Print the HTTP status code (200 = OK)
#print(response)
# Save API response values to a new variable
response_values = response.json()

# Extract the unix time from the json
datetime_request = int(response_values.get('request').get('datetime'))

# Convert unix time to UTC format
datetime_handle = datetime.datetime.fromtimestamp(int(datetime_request)).strftime('%d/%m/%Y at %H:%M:%S')

# Print the output
print('ISS will pass over London on:\n' + datetime_handle + ' UTC')
