import requests
from pprint import pprint

url = "https://dummyjson.com/users"
params = {"limit": 1000, "skip": 0}

response = requests.get(url, params=params)

response_json = response.json()
users = response_json["users"]

search_word = "manager"
search_word2 = "female"

thirty_age_people = []
users_in_montana = []
people_work = []
people_lives_and_work_in_the_same_city = []
female_manager_workers = []
green_eye_people_email = []

for user in users:
    if user.get("age") <= 30:
        thirty_age_people.append(user)
    if user["state"] == "Montana":
        users_in_montana.append(user)
    if user["title"] == "Quality Assurance Engineer":
        people_work.append(user)
    if user["eyeColor"] == "Green":
        green_eye_people_email.append(user["email"])
    if user["address"]["city"] == user["company"]["address"]["city"]:
        people_lives_and_work_in_the_same_city.append(user)
    if search_word in user["title"]:
        if search_word2 in user["gender"]:
            female_manager_workers.append(user)

# pprint(green_eye_people_email)
# pprint(thirty_age_people)
