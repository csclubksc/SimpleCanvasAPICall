#!/usr/bin/python3
 
# Import the required libraries to work with JSON
import requests
import json

# Information that will be needed for GET request
# Typically these would be loaded in from a config file
token = '<TOKEN-FROM-CANVAS>' # Obtained through OAuth2 in real-world application
base_url = 'https://keene.instructure.com/api/v1/'


headers = {'Authorization': f'Bearer { token }'}

# Function to generate the final endpoint
def endpoint(ep):
    return f'{ base_url }{ ep }'

# Make the get request to the API with the appropriate headers
results = requests.get(endpoint('courses'), headers=headers)

# Get the text from the response body
response = results.text

# Format returned JSON into array of dictionaries
values = json.loads(response)

myCourse = input('Enter Course Name: ')
for course in values:
    # myCourse is cast to str (from input())
    if course.get('name', 0) == myCourse:
        resp = requests.get(endpoint('courses/%i/assignments' % course['id']), headers=headers)
        assignments = json.loads(resp.text)
        for assignment in assignments:
            if assignment['published']:
                print(assignment['name'] + "=> " + str(assignment['due_at']))
