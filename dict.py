# dictionary is same like associative array in other languages.

marks ={
    "maths": 90,
    "english": 80,
    "science": 95
}

'''
 print(marks,type(marks))

 print(marks["maths"])

 print (marks.items()) key and values pairs output shows.

 print(marks.keys()) keys output shows.

 print(marks.values()) values output shows.

 marks.update({"maths" :100})

 print(marks["maths"]) update the value of maths key.

 marks.update({"social": 100}) it adds and updates the key and value.
 print(marks)

 print(marks.get("english")) it will shows the value in english key. 

 print(marks['english'])
 '''

# get prints null and normal print errors.
# print(marks.get("english1"))
# print(marks['english2'])

print(marks.pop("english")) #delete the value with its key.
print(marks) 

