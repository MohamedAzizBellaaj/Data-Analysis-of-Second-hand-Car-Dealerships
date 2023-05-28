from bs4 import BeautifulSoup
import requests 
url="https://www.automobile.tn/fr/occasion"
# print(page)
for j in range(10):
    if j==0 :
        page=requests.get(url)
    else :
        page=requests.get(f'{url}/{j}')
    print(f'***********************************page {j}**************************************')
    soup=BeautifulSoup(page.content,'html.parser')
    cars=soup.find_all('div', class_="occasion-item")
    # print(cars[0])
    specs=['year',"road","map","fuel","boite"]
    for i,car in enumerate(cars): 
        print(f'************car {i}*************')
        title=car.find('h2').span.text
        print(f'title= {title}')
        for spec in specs :
            var=car.find('li', class_=spec)
            value=var.find('span',class_='value').text
            print(f'{spec} = {value}')
        price=car.find('div',class_="price").text.replace(' ','').replace('\n','')
        print (f'price= {price}')

