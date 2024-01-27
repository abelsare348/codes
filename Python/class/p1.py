#object has state, behaviour and identity
# state- refers to attribute of object like variables the type of data that object stores.
# behaviour - methods of class like they get access to method of class

class furniture:
    Country='India'
    def __init__(self):
        print("Obj is created for furniture class",self.__str__)
    def add(self,var1,var2):
        return var1+var2


obj=furniture()
obj.name='table'
print(obj.__str__())
print(obj.Country)
print(obj.add(2,3))