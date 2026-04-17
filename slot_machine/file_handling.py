import json
def read_data():
    with open ("data/user.json","r") as f:
        data = json.load(f)
        return data

def write_data(data):
    with open("data/user.json","w") as f:
        json.dump(data,f,indent=4)