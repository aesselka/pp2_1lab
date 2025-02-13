import json
with open('sample-data.json', "r") as file:
    data = json.load(file)

ty = []
ty.append("Interface Status")
ty.append("=" * 90)
ty.append(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
ty.append("-" * 90)


for i in data["imdata"]:
    b = i["l1PhysIf"]["attributes"]
    ty.append(f"{b['dn']:<50} {b['pathSDescr']:<20} {b['speed']:<10} {b['mtu']:<10}")

for i in ty:
    print(i)