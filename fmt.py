import json 
with open("example.json" , "r") as json_file:
    data=json.load(json_file)
def dict_to_js(did):
    print(json.dumps(did))
did={"name":"Assel" , "age":"18", "birth":"04.03.07"}
a=did
dict_to_js(did)
with open("example.json", "w") as json_file:
    json.dump(a, json_file)