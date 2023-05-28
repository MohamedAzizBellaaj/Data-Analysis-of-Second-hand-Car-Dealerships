from bs4 import BeautifulSoup
import requests 
from csv import writer

def format_number(s) :
    n=s[:-2]
    return n.replace(' ','')

def extract(detail) :
    # split the url to get the brand and the model seperated (there's no other way ig) 
    titre=detail.split('/')
    row.append(titre[3].replace('-',' '))
    row.append(titre[4].replace('-',' '))
    detail_url='https://www.automobile.tn'+ detail
    detail_page=requests.get(detail_url)
    detail_soup=BeautifulSoup(detail_page.content,'html.parser')
    price=detail_soup.find('div', class_='small-price').span.text
    row.append(format_number(price))
    #get 'Kilométrage',"année","localisation","date_ajout"
    ul=detail_soup.find('ul', class_="list-unstyled")
    lis=ul.find_all('li')
    for li in lis :
        if li.label : #do not get the number of the seller
            if li.label.text == 'Kilométrage : ':
                row.append(format_number(li.span.text))
            else : 
                row.append(li.span.text.strip())
    #get description 
    desc=detail_soup.find_all('div', class_='description')
    if len(desc)>1 : 
        description=desc[1].text
    else : 
        description=''

    row.append(description.strip().replace('\n',''))
    #get 'carrosserie','energie','puissance','boite','transmission','couleur'
    tech_details=detail_soup.find('div', class_='technical-details')
    tables=tech_details.find_all('table')
    for table in tables: 
        head=table.thead.tr.th.text.strip().replace('\n','')
        info=table.tbody.tr.td.text.strip().replace('\n','')
        if head=='Puissance fiscale' :
            row.append(format_number(info))
        else:
            row.append(info)

        if head=='Couleur':
            break
    #get prix du neuf 
    price_new=detail_soup.find('div',class_='price')
    if price_new and price_new.span : 
        row.append(format_number(price_new.span.text))
    else : 
        row.append('')

    # print(row)



url="https://www.automobile.tn/fr/occasion"
number_of_pages=278
specs=['marque', 'modele', 'prix','kilometrage',"annee","localisation","date_ajout",'description','carrosserie','energie','puissance','boite','transmission','couleur','prix_neuve']
with open('cars.csv','w', encoding='utf8',newline='') as f:
    the_writer= writer(f, dialect='excel')
    the_writer.writerow(specs)
    for j in range(number_of_pages):
        if j==0 :
            page=requests.get(url)
        else :
            page=requests.get(f'{url}/{j}')
        print(f'***********************************page {j}**************************************')
        soup=BeautifulSoup(page.content,'html.parser')
        cars=soup.find_all('div', class_="occasion-item")
        for car in cars: 
            row=[]
            detail=car.find('a', class_="details-container")["href"]
            extract(detail)
            the_writer.writerow(row)
