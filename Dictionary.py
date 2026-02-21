#DICTIONARY IN PYTHON
info={
    "key":"value", #to assign or add new
    "name":"santosh",
    "learning":["python", "Java" ,"C",],
    "age":21,
    "is_audlt":True,
    "marks":90.9,
    90:89,
    99.9:89.9
}
print(info)
print(info["name"])
print(info["age"])
print(info[90])
print(type(info))
info["name"]="Virat" #overwrite
info["surname"]="Kohli" #add or assign
print(info)

info1={}
print(info1)
info1["book"]="abc"
print(info1)

#NESTED DICTIONARIES
student={
    "name":"santosh",
    "subject":{"phy":89,
               "chem":90,
               "math":96}
}
print(student)
print(student["subject"])
print(student["subject"]["math"])

#DICTIONARY METHODS IN PYTHON
#1.myDict.keys() ,returns all keys
student_dict={
    "Name":"karan",
    "marks":57
}
print(student_dict.keys())
print(list(student_dict.keys())) #list
print(len(student_dict.keys()))

#2.myDict.values() ,return all keys
student_dict1={
    "match":"RCB vs CSK",
    "Date":"12/4/2026",
    "price":9999.00
}
print(student_dict1.values())
print(list(student_dict1.values()))

#3.myDoct.items() ,returns all(key,val) pairs as tuples
student_dict2={"match":"MI vs CSK",
    "Date":"14/4/2026",
    "price":9991.00
}
print(student_dict2.items())
pair=list(student_dict2.items())
print(pair[0])

#4.myDict.get("key") , return the key according to value
student_dict3={"match":"RCB vs KKR",
    "Date":"16/4/2026",
    "price":9996.00
}
print(student_dict3["match"])
#if we print(student_dict3["match2"]) gives error
print(student_dict3.get("match"))
print(student_dict3.get("match1")) #no error -->None

#5.myDict.update(newDict) ,insert the specified items to the dictionary
Student={
    "name":"santosh",
    "learning":"python", 
    "age":21,
    "is_audlt":True,
    "marks":90.9
}
new_dict={"city":"Bengaluru","python":89}
Student.update(new_dict)
print(Student)