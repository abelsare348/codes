str1="Hello World"
print(str1[2:7]) #we can slice down the string into desired o/p we want
print("****************")
print(str1[::-1]) #third parameter decide the jump for character 
print(str1[0::2]) #if the parameter is not given it takes the default limit.

del str1
try:
    print(str1)
except:
    print("String does not exists anymore")
