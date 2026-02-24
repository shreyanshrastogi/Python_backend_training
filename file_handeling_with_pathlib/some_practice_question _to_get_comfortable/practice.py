import json
from pathlib import Path

# 1-
#  Which function converts it into a Python dict?

# response_text = '{"city": "Delhi", "temp": 32}'
# response_dict = json.loads(response_text)
# print(response_dict)

# 2-
# You want to save this dictionary to user.json:

# user = {"name": "Shreyansh", "age": 21}
#  Which function do you use?
# path = Path("user.json")

# with path.open("w") as f:
#     json.dump(user, f, indent=4)

# 3-
#  Which function reads JSON from it?

# path=Path("config.json")
# path_dict={}
# with path.open('r') as f:
#     path_dict=json.load(f)

# 4-
# You need to send JSON data in an HTTP request body.
#  Which function converts dict → JSON string?


# j_string=json.dumps(j_dict)


# 5-
# loads should be used because it is string

# 6-

# with open("data.json") as f:
#     data = json.load(f)

# 7-

# with open("file.json", "w") as f:
#     json.dump({"a": 1}, f)


# 8-
# path=Path("students.json")
# dict_path={}
# with path.open('r') as f:
#     dict_path=json.load(f)

# print(len(dict_path["student"]))

# 9-


# data = {"course": "Python", "level": "backend"}
# data_s = json.dumps(data)
# print(data_s)

# 10-
# Save this list to numbers.json:
# nums = [1, 2, 3, 4, 5]
# path = Path("numbers.json")
# with path.open("w") as f:
#     json.dump(nums, f, indent=4)

# 11-You receive request body as string:
# 👉 Convert it to dict and access username.
# body = '{"username":"admin","password":"1234"}'
# body_d = json.loads(body)
# print(body_d["username"])


# q12-
# ❓ Q12

# You want to store API logs in a file:


# log = {"endpoint": "/login", "status": 400}
# path = Path("logs.json")
# old_log = {}
# with path.open("r") as f:
#     old_log = json.load(f)

# old_log.update(log)
# with path.open("w") as f:
#     json.dump(old_log, f, indent=4)


# q13

# one will be a string and second will be a dict,dumps means write to string