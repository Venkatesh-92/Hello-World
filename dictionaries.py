# dictionary

birthday = {
    "venkatesh": "15-07-1992",
    "deepu_shree": "13-07-1997",
}

'''meaning = {
    "train":"top_speed_is_180kmph",
    "jet":"top_speed_is_2900kmph",
    "bus":"top_speed_is_160kmph",
    "Bike":"top_speed_is_120kmph"   
}
'''
'''
# Accessing dictionary element,
print(birthday["deepu_shree"])

# print type,
print(type(birthday))

# safe accessing,
print(birthday.get("duthiksha","not found"))
'''

# adding dictionary element,
print("adding duthiksha to the list") # this is one method 
birthday["duthiksha"]= "06-01-2025" # this is another method
print(birthday)

#updating dictionary element,
print(birthday)

print("updating...")
birthday["venkatesh"]= "15-07-1993"

print(birthday)

# removing element from dictionary,
print(birthday)
birthday.pop("venkatesh")
print(birthday)

print(birthday)
birthday.clear()
print(birthday)

# dictionary methods,
birthday = {
    "venkatesh": "15-07-1992",
    "deepu_shree": "13-07-1997",
}

print(birthday.keys())

print(birthday.values())

print(birthday.items())


birthday1 = {
    "venkatesh": "15-07-1992",
    "deepu_shree": "13-07-1997",
}

birthday2= {
    "venky": "15-07-1992",
    "deepu_shree_MS": "13-07-1997",
}
birthday1.update(birthday2)
print(birthday1)

# add (marge) two dictionary
item1 = {
    "milk":"1ltr",
     "price":"55",
     "weight":"1kg"
}

item2 = {
    "apple" : "1",
       "price" : "200",
         "qulity" : "first_qulity",
             "color":"red_color",
                  "weight":"2.5kg"
}

items = [item1,item2]
print(items)

print(f"total weight: {item1["weight"]+ " " + item2["weight"]}") # formated string,