# this file is for cleaning the data

import csv

struct = {"marque": "null",
          "modele": "null",
          "prix": "null",
          "kilometrage": "null",
          "annee": "null",
          "localisaton": "null",
          "cylindree": "null",
          "description": "null",
          "carrosserie": "null",
          "energie": "null",
          "puissance": "null",
          "boite": "null",
          "couleur": "null",
          "prix_neuve ": "null"
          }

with open("cleaner.csv", 'w', encoding='UTF8',newline='') as f2:
    with open("data1.csv", 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        writer = csv.writer(f2)
        title = [x for x,y in struct.items()]
        print(title)
        writer.writerow(title)
        for row in reader:
            # marque
            struct["marque"] = row[1][row[1].index('>') + 1:row[1].rindex('>')].strip()
            # modele
            struct["modele"] = row[1][row[1].rindex('>') + 1:].strip()
            # localisation
            if (len(row[2].split('>')) > 1):
                struct["localisaton"] =row[2].split('>')[1].strip()
            # energie
            struct["energie"] = row[3].strip()
            # puissance
            struct["puissance"] = row[4].strip()
            # kilometrage
            if row[5].replace(' ', '').isdigit():
                if int(row[5].strip().replace(' ', '')) < 1000:
                    struct["kilometrage"] = int(row[5].strip().replace(' ', '')) * 1000
                else:
                    struct["kilometrage"] = int(row[5].strip().replace(' ', ''))
            #annee
            struct["annee"] = row[6][row[6].rindex('/')+1:].strip()
            #couleur
            struct["couleur"] = row[7].strip()
            #boite
            struct["boite"] = row[8].strip()
            #prix
            struct["prix"] = ''.join(row[9].strip().split()[0:2])
            #description
            struct["description"] = row[10].strip()

            data = [y for x,y in struct.items()]
            writer.writerow(data)
            print(data)

print("done")