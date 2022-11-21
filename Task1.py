import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

bag_url=[]
bag_name=[]
bag_price=[]


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
        bag_url.append(i)
    for i in name:
        bag_name.append(i.text)
    for i in price:
        bag_price.append(i.text)

data={"Bag Url":bag_url,"Bag Name ":bag_name,"Bag Price":bag_price} 
df=pd.DataFrame(data)  
df.to_csv("Task1.csv")