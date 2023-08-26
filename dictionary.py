# Dictionary is mutable

dict = {"Good": "Something pleasant",
        "Fetch" : "to bring",
        "1" : "the number 1"}
print(type(dict))
print(dict["Good"])

marks = {"Sudarshan" : 80, "Shivani" : 90, "Sankalp" : 65}

# get value by key - Ist way
# It throws error if key not present
print(marks["Sudarshan"])

marks["Harry"] = 100
print(marks)

# get value by key - IInd way
# It does not throw error if key not present
print(marks.get("Sudarshan"))

print(marks.keys())
print(marks.values())
print(marks.items())
