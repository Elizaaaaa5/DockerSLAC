#Print your name and make a file use your name as file name
name = 'Eliza'
file = open("%s.txt" %name, "w")
file.writelines("Hello Newbie.")
file.close()
print("Hello, %s, we made a file for you." %name)


