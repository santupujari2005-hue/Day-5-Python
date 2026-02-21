#1.Store following word meanings in a python dictionary :
# table : “a piece of furniture” “list of facts & figures” cat : “a small animal”
dict_1={
    "cat":"a small animal",
    "table":["a pice of furniture","list of facts & figures"] 
        }
print(dict_1)
#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”“java”,“C++”,“C”,
subjects={"python","java","c++","python","javascript","java","python","java","c++","c"   
}
print(subjects)
print(len(subjects))


#2.WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}
x=int(input("enter phy: "))
marks.update({"phy":x})
x=int(input("enter chem: "))
marks.update({"chem":x})
x=int(input("enter eng: "))
marks.update({"eng":x})
print(marks)

#Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)
values={12,"9.0"}
print(values)
#OR
values1={
    ("float",9.0),
    ("int",9)
}
print(values1)

