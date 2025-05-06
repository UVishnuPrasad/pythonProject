dict = {'john':99, 'david':89 ,'joseph':45}
name = input("Enter student name :").strip()
print("{0}'s marks is:{1}".format(name,dict.get(name))) if name in dict else print("Student not found")
