import json

person = {
    "name": "Tom",
    "age": 20,
    "skills": ["Python", "Git"]
}

# Test 1
text = json.dumps(person)

print(person)
print(text)

print(type(person))
print(type(text))

print(person == text)
print("-----------------------------------------------------------")

# Test 2
new_person = json.loads(text)

print(new_person)
print(type(new_person))
print(person == new_person)

