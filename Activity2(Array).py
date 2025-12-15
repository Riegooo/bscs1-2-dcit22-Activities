
Technical_courses = ["BSCS", "BSIS", "BSIT", "BSCpE", "BSEE"]

print(f"Original Array: {Technical_courses}")
print(f"First Element: {Technical_courses[0]}") #first element
print(f"Third Element: {Technical_courses[2]}") #third element
print(f"Number of elements: {len(Technical_courses)}") #Display total number of elements

print()
print("Array Elements:")
for course in Technical_courses: #Loop through the array and print each element
    print(course)
print()
    
Technical_courses.append("BSME") #Append one element to the end of the array
Technical_courses.insert(1, "BSSE") #Insert one element at a specific index

print(f"Updated Array: {Technical_courses}") #Updated Array list, Total = 7

Technical_courses.remove("BSEE") #Remove one element by value
Technical_courses.pop(5) #Remove one element using pop()

print(f"Final Array: {Technical_courses}") #Final Array list, Total = 5


