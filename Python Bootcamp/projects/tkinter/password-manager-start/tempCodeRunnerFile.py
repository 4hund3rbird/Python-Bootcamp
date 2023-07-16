import json
my_data={
    "name":"age"
}
with open("data1.json","w") as file:
    json.dump(my_data,file)
    file.close()