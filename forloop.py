devices = ["phone", 1, "laptop", 50.2]

for x in devices:
    print(x)

name = "Jarell"
for y in name:
    print(y)

for x in devices:
    print(x)
    if x == "laptop":
        break

for x in devices:
    if x == "laptop":
        continue
    print(x)

