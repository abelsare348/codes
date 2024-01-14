import charade
str1="hello my name is Aniket. i am good"
print(str1.capitalize())   # capitalize - truns the first letter of string to upper.
str2="india"
print(str2.center(10," ")) # adds the texts in center of the length specified and character appends in the start and end of string.

print(str2.ljust(10,"*"),str2.rjust(10,"*"))  # just like the pad,lpad,rpad function in sql.

str4="   Aniket   "
print(str4.lstrip(),str4.strip(),str4.rstrip())  #just like the trim function in sql ltrim, rtrim, trim.

print(str1.count("is",0,len(str2)))

str3="I Am Aniket"
print(charade.detect(str3.encode()))  # charade library can detect which encoding format is used.

print(str3.lower())   # convert the sting in lower character.

print(str3.upper())   # convert the string to upper character.

lst=str3.split(" ")
print(lst)

lst1=str3.rsplit(" ") # splits the string in backward direction.
print(lst1)

str5="I am from Maharashtra. \n I am good boy"

lst2=str5.splitlines() #split the string on the basis of \n.
print(lst2)





