#Import the required libraries to work with JSON
import requests
import json

# Information that will be needed for GET request
token = "<TOKEN-FROM-CANVAS>" #Obtained through OAuth2 in real-world application
api = "https://keene.instructure.com/api/v1/"
headers = {'Authorization': 'Bearer ' + '%s' % token}

#Construct the URL for the request
url = api + 'courses'

#Make the get request to the API with the appropriate headers
results = requests.get(url, headers=headers)

#Get the text from the response body
response = results.text

#Format returned JSON into array of dictionaries
values = json.loads(response)