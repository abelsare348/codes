def Generate(num1: int,num2: int):
    x=num1+num2
    yield x
    y=num1-num2
    yield y
    z=num1*num2
    yield z
    
x=Generate(12,13)

#print(tuple(x))  #it gives us immutable collection

#print(list(x)) #it gives us mutable collection 

#print(set(x))   # It gives us ordered collection

print(next(x))
print(next(x))
print(next(x))