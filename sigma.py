my_dict={"id1":
    {"Name":["Aarza"],
    "Class":["VII"],
    "Subject_integrration":["English,Maths,Science"]},
    "id2":
    {"Name":["Aashman"],
    "Class":["VII"],
    "Subject_integrration":["English,Maths,Science"]},
    "id3":
    {"Name":["Aarza"],
    "Class":["VII"],
    "Subject_integrration":["English,Maths,Science"]},
    "id4":
    {"Name":["Anhad"],
    "Class":["VII"],
    "Subject_integrration":["English,Maths,Science"]},
    

    }
print(my_dict)
result={}
for key,value in my_dict.items():
    if value not in result.values():
        result[key]=value
print(result)