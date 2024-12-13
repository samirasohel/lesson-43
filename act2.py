my_dict={"name":"Samira","age":20,"grade":12}

print("My dictionary is",my_dict)

print("Name of student is",my_dict["name"])

my_dict["city"]="chattrogram"

print("Updated dictionary is",my_dict)

my_dict.pop("grade")

print("Updated dictionary is after pop",my_dict)

my_dict.clear()
print(my_dict)