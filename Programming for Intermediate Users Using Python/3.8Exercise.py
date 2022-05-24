#1
opening_file = open("newfile.txt", "r")
#2
print(opening_file.read())
#3
print(opening_file.readline())
#4
for line in opening_file:
    print(line)

#5
import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
      os.remove("newfile.txt")

