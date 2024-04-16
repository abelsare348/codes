#class code functions

def add(num1:int,num2:float) ->int:
    x=num1+num2
    return x

def print_list(lst:list):
    for i in lst:
        print(i)

print("Hello")

if __name__=='__main__':
    print("Hello world!!!")
    print(add(1,1))
    lst=[1,2,3,4,5]
    print(type(lst))
    print_list(lst)
