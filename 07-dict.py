# Create Dict
player = {
    "name": "Tom",
    "hp": 100,
    "level": 5
}

# Retrieve the Value Using the Key
print(player["name"])
print(player["hp"])

# Edit Data
player["hp"] = 80

# Add New Data
player["weapon"] = "Sword"

# Iterate through the Dict
for key in player:
     print(key)

# .keys()
print(player.keys())

for key in player.keys():
    print(key)

# .values()
for value in player.values():
    print(value)

# .items()
for key, value in player.items():
    print(f"{key}: {value}")

