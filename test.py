import requests

BASE = "http://127.0.0.1:5000/"

response1 = requests.put(BASE + "complaint/1", {"subject": "Bad Drainage System @Hyd", "description": "Drains are overflowing on highways and there is a huge traffic jam", "likes": 24556})
print(response1.json())

input()

response2 = requests.put(BASE + "complaint/2", {"subject": "Misconduct of cops in the state", "description": "Seized bike for no reason and asking for bribe", "likes": 8563})
print(response2.json())

input()

response3 = requests.put(BASE + "complaint/3", {"description": "random spam", "likes": 2})
print(response3.json())

input()

response4 = requests.get(BASE + "complaint/2")
print(response4.json())

input()

response5 = requests.get(BASE + "complaint/6")
print(response5.json())

input()

response6 = requests.patch(BASE + "complaint/1", {"description": "The issue is solved now!", "likes": 43577})
print(response6.json())

input()

response7 = requests.patch(BASE + "complaint/2", {"likes": 8944})
print(response7.json())

input()

response8 = requests.delete(BASE + "complaint/1")
print(response8)

input()

response9 = requests.get(BASE + "complaint/1")
print(response9)

input()

print("Testing phase done!")

