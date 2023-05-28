# this is the webscrapping of the site http://www.tunisie-annonce.com/
import csv
from bs4 import BeautifulSoup
import requests

data_array1 = {
    'nom': 1,
    "categorie": 4,
    "localisation": 7,
    "energie": 10,
    "puissance": 12,
    "kilometrage": 15,
    "mise_en_circulatiom": 17,
    "couleur": 20,
    "boite_de_vitesse": 22,
    "prix": 25,
    "description": 28,
    "inseree_le": 31,
    "modifiee_le": 33,
}

data_array2 = {
    'nom': 1,
    "categorie": 4,
    "localisation": 7,
    "energie": 13,
    "puissance": 15,
    "kilometrage": 18,
    "mise_en_circulatiom": 20,
    "couleur": 23,
    "boite_de_vitesse": 25,
    "prix": 28,
    "description": 31,
    "inseree_le": 34,
    "modifiee_le": 36,
    "adresse": 10
}


def get_data(link):
    global data_array1, data_array2
    details_text = requests.get(link).text
    soup2 = BeautifulSoup(details_text, 'lxml')
    all_data2 = soup2.find_all("table", class_='da_rub_cadre')
    # labels = all_data2[1].find_all('td', class_="da_label_field")
    # data = all_data2[1].find_all('td', class_="da_field_text")
    all_td = all_data2[1].find_all('td')
    if (all_td[9].text == "Adresse"):

        aux = [all_td[y].text.strip().replace('\xa0', ' ') for x, y in data_array2.items()]
        print(aux)
        writer.writerow(aux)
    else:

        aux = [all_td[y].text.strip() for x, y in data_array1.items()]
        print(aux)
        writer.writerow(aux)


with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    for e in range(1, 10):

        html_text = requests.get(
            'http://www.tunisie-annonce.com/AnnoncesAuto.asp?rech_cod_cat=2&rech_cod_rub=201&rech_cod_typ=&rech_cod_sou_typ=&rech_cod_pay=TN&rech_cod_reg=&rech_cod_vil=&rech_cod_loc=&rech_prix_min=&rech_prix_max=&rech_surf_min=&rech_surf_max=&rech_age=&rech_cod_energ=&rech_photo=&rech_order_by=31&rech_page_num=' + str(
                e)).text
        # print(html_text)
        soup = BeautifulSoup(html_text, 'lxml')
        all_data = soup.find_all('tr', class_='Tableau1')

        for e in all_data:
            details_link = 'http://www.tunisie-annonce.com/' + e.find_all('td')[7].a['href']
            print(details_link)
            get_data(details_link)

print("done ")
