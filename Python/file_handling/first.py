import os

file=open(r'C:\Users\Aniket\Documents\Aniket\abc.txt','w+')

file.write('Hi, My name is Aniket!!')

file.seek(0)

print(file.read())

file.close()

#os.remove(r'C:\Users\Aniket\Documents\Aniket\bcd.txt')  

#os.rename(r'C:\Users\Aniket\Documents\Aniket\bcd.txt',r'C:\Users\Aniket\Documents\Aniket\cde.txt')

os.mkdir(r'C:\Users\Aniket\Documents\Aniket\timepass')