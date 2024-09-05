#you can write anything in one stroke / like everyting should be in one expression

#The main difference between lambda function and other functions defined using def keyword is that, 
# we cannot use multiple statements inside a lambda function and allowed statements are also very limited inside lambda statements.
# Using lambda functions to do complex operations may affect the readability of the code

#The lambda function gets more helpful when used inside a function.

x= lambda x,y: x*y if x<10 else x/y

print(x(15,5))

y= lambda : print("hello world")

y()  # you'll have to call the function. if you call only the function name it will give you the address of function object where it is stored.

def cal():
    print("hello stign")
    return 'hello bhai'
    
print(cal())

lst=['Aniket','Bac']
x=map(lst,1)
print(lst)