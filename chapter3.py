#                    "CHAPTER-03 - STRINGS"
# name="Sukriti"
# petname = name[0:5]  #first index included but last index was excluded
# print(petname)
# print(name[:4]) #is same as print(name[0:4])
# print(name[1:]) #same as print(name[1:6])
# print (name[-4:-1]) #same as print(name[3:6])
# print(name[3:6])

# alphabet="abcdefghijklmnopqrstuvwxyz"
# print(alphabet[1:24:5]) #it will print the alphabets from 1 to 24 with a gap of 5

# print("my \"name\" is sukriti \nand i love to do \tcoding and typing as fast  as i can")

# PROBLEM 01 
# name = input("Enter your name(in caps): ")
# print("GOOD AFTERNOON",name)

# PROBLEM 02 
# letter = ''' Dear <|Name|>,
#                             You are selected! 
#                             <|Date|>'''
# print(letter.replace("<|Name|>", "Sukriti Chaudhary").replace("<|Date|>","29 December 2024"))

# PROBLEM 03
# name= "My name is  Sukiii  riitiiiiii ulf jiya  cutiee patutiiii"
# # print(name.find(" "))

# PROBLEM 04
#  i have changed the double spaces of problem 03  to single spaces in problem 04
# print(name.replace("  ", " "))
# print(name) # strings are immutable (which means if we change something in the string it makes a new string and doesn't change the original one...)

# PROBLEM 05
# letter= "Dear Sukki roti, you are doing great!! Thanks "  this is the original one!!!
letter= "Dear Sukki roti,\n \tYou are doing great!! \nThanks " #i have modified this sentence using "escape sequence character"
print(letter)




