import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

item_url=[]
item_name=[]
item_price=[]


for i in range(1,20):
    url="https://www.flipkart.com/search?q=redmi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    req=requests.get(url)
    content=BeautifulSoup(req.content,'html.parser')

    anchors=content.find_all('a',{"class":"_1fQZEK"})
    all_links=set()
    for link in anchors:
        if(link.get('href')!='#'):
            linkText="https://www.flipkart.com"+link.get('href')
            all_links.add(linkText)
   
    name=content.find_all('div',{"class":"_4rR01T"})
    price=content.find_all('div',{"class":"_30jeq3 _1_WHN1"})

    for i in all_links:
        item_url.append(i)
    for i in name:
        item_name.append(i.text)
    for i in price:
        item_price.append(i.text)

data={"URL":item_url,"Name ":item_name,"Price":item_price} 
df=pd.DataFrame(data)  
df.to_csv("Task1.csv")