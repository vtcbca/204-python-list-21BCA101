'''Write a script to enter any word and check it is palindrom or not.
 Name : Smit Lad.
 Date : 12-03-22'''
a=input("Enter any string : ")
b= "".join(reversed(a))
if a==b:
    print("{} is palindrom".format(a))
else :
    print ("{} is not palindrom.".format(a))
