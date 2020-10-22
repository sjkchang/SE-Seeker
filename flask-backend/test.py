import requests

BASE = "http//127.0.0.1:5000/api/"

data = [{"company": "Apple", "date": "Summer2020", "description": "An internship"},
        {"company": "Google", "date": "Summer2021", "description": "An internship2"},
        {"company": "Hi", "date": "Summer2019", "description": "An internship3"}]

for i in range(len(data)):
    response = requests.put(BASE + "internship/" + str(i), data[i])

input()
response = requests.get(BASE + "internship/0")
print(response.json())
 