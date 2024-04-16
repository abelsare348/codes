import requests

from bs4 import BeautifulSoup

response=requests.get('https://www.geeksforgeeks.org/python-programming-language/')

#print(response.content)  -- The content will print in line but not like understandable format.

soup = BeautifulSoup(response.content, 'html.parser') #beutifulsoup gives us flexibility to read like developers inspect tool in browser by 
#specifying parsing used in web page.

con=soup.find('div',class_='entry-content')

lines = con.find_all('p') 
  
for line in lines: 
    print(line.text)
#print(response.url)