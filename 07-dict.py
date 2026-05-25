# 1. Create Dict
player = {
    "name": "Tom",
    "hp": 100,
    "level": 5
}

# 2. Retrieve the Value Using the Key
# print(player["name"])
# print(player["hp"])

# 3. Edit Data
player["hp"] = 80

# 4. Add New Data
player["weapon"] = "Sword"

#print(player)

# 5. Iterate through the Dict
# for key in player:
#     print(key)

# Iterate through the Key
#print(player.keys())

for key in player.keys():
    print(key)

# Iterate through the Value
for value in player.values():
    print(value)


