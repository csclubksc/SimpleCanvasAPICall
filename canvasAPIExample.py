import requests
import json

token = "<Insert custom token here>"
api = "https://keene.instructure.com/api/v1/"
headers = {'Authorization' : 'Bearer ' + '%s' % token}

url = api + 'courses?enrollment_state=active'

results = requests.get(url, headers=headers)
response = results.text

values = json.loads(response)

myCourse = input("Enter Course Name: ")

for course in values:
    if 'name' in course and course['name'] == myCourse:
        assignments = requests.get('https://keene.instructure.com/api/v1/courses/' + str(course['id']) + '/assignments',
                                    headers=headers)
        jsonAssignments = json.loads(assignments.text)
        for assignment in jsonAssignments:
            if assignment['published']:
                print(assignment['name'] + "=> " + str(assignment['due_at']))
