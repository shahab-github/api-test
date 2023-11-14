import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

try:
    resp = requests.get(url)
    resp.raise_for_status()
except requests.HTTPError as err:
    print(err)
else:
    if resp.status_code == 200:
        data = json.loads(resp.text)
        # users_list = [user.get('name') for user in data]
        # print(users_list)
        # usernames_list = [user.get('usernames') for user in data if user.get('usernames') != None]
        # print(usernames_list)
        custom_response = []
        for user in data:
            name = user.get("name")
            email = user.get("email")
            user_dict = dict()
            user_dict["Name"] = name
            user_dict["Email"] = email
            custom_response.append(user_dict)

        print(json.dumps(custom_response, indent= 4))


# print(type(resp.json()[0]))
# print(resp.json()[0])
