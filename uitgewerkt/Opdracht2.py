#deel 1 done
#deel 2 todo


## Deel 1
import csv
from datetime import datetime, time

ip_time_dictionary = dict()  # om het IP-adres te koppelen aan het meest recente tijdstip
ip_ID_dictionary = dict()  # om het IP-adres te koppelen aan een ID-nummer, zo kunnen we naar de lijst van deze bezoeker verwijzen
current_date = 0  # om de meest recente datum op te slaan
visitor_ID = 0  # om het ID-nummer te maken
list_of_paths = []  # om de lijsten van de bezoekers op één plek op te slaan

with open('DataOpslagSTEM_.txt') as csvfile:
    file = csv.reader(csvfile, delimiter=",")

    # linecount = 0

    first_line = True
    for line in file:

        #We checken of het de eerste regel van het csv bestand is
        # Vervolgens zetten we first line op false zodat de if statement volgende keer volgende keer niet weer op true komt
        # dan gebruiken we continue om een loop-regel over te slaan
        if first_line is True:
            first_line = False
            continue

        #we definieren een aantal variabelen die we nodig hebben.
        #deze variabelen komen uit de comma seperated line
        date = line[0]
        time = line[1]
        ip = line[2]
        page = line[3]

        # print(date, time, ip)

        #we kijken of er al een tijd opgeslagen is bij de debetreffende IP adres
        if ip not in ip_time_dictionary:
            # hier gebruiken we weer Blok 1

            #voeg nieuwe lijst en sla tijd op
            ip_time_dictionary[ip] = time
            list_of_paths.append([])
            list_of_paths[visitor_ID].append(page)
            ip_ID_dictionary[ip] = visitor_ID
            visitor_ID = visitor_ID + 1
            # handig om te weten de visitor id is hetzelfde nummer als de index van diens lijst in de list_of_paths
            # ga verder want dit is een unieke bezoeker en we kunnen de tijd niet vergelijken met een vorige tijd of datum.
            continue


        # We zijn klaar met de if... dus het ip bestaat al en er is al een tijd gelogd.
        # misschien is die tijd wel gelogd in een vorige datum
        if date != current_date:
            #Ja een nieuwe dag is aangebroken! voeg weer een nieuwe lijst toe en sla tijd op. (gebruik blok 1)

            ip_time_dictionary[ip] = time
            list_of_paths.append([])
            list_of_paths[visitor_ID].append(page)
            ip_ID_dictionary[ip] = visitor_ID
            visitor_ID = visitor_ID + 1

            #we moeten deze datum wel even onthouden
            current_date = date

            #ga maar weer verder, we hoeven niks te vergelijken, het is een nieuwe lijst.
            continue

        #oke. Het is geen nieuwe dag, er is al eerder activiteit opgeslagen.

        # hier komt Blok 2
        #we pakken de laatste tijd a.h.v de ip adres
        past_time = ip_time_dictionary[ip]
        # we vergelijken de huidige tijd met de vorige tijd en krijgen een tijdverschill object die we in de time_spend variabele stoppen
        time_spend = datetime.strptime(time, '%H:%M:%S') - datetime.strptime(past_time, '%H:%M:%S')
        #we kijken hoeveel seconde het verschil is
        seconds = time_spend.seconds

        #gebruik 30 minuten als minimale duration
        MINIMAL_DURATION = 1800

        #de verstreken tijd is minder dan de minimale duratie.
        if seconds < MINIMAL_DURATION:
            ID = ip_ID_dictionary[ip]
            #we voegen de pagina toe
            list_of_paths[ID].append(page)
        else:
            #dit duurde wel heel lang, waarschijnlijk is dit een 2e bezoek. Maak weer een nieuwe lijst (blok 1)
            ip_time_dictionary[ip] = time
            list_of_paths.append([])
            list_of_paths[visitor_ID].append(page)
            ip_ID_dictionary[ip] = visitor_ID
            visitor_ID = visitor_ID + 1

print(list_of_paths)


for list in list_of_paths:

    formatted_list = 'Begin   '

    for page in list:
        if page == '':
            page = 'Hoofdpagina'

        formatted_list += ' -->     ' + page + ''
    formatted_list += '---> EIND '

    print(formatted_list)

'''Voorbeeld output

Begin    -->     /sitemap_index.xml---> EIND
Begin    -->     /category-sitemap.xml---> EIND
Begin    -->     /page-sitemap.xml---> EIND
Begin    -->     Hoofdpagina---> EIND
Begin    -->     Hoofdpagina -->     /disclaimer/ -->     /privacybeleid/ -->     /contact-opnemen-met-veilig-gehecht/---> EIND


'''


def originele_blokken():

    # Blok 1
    ip_time_dictionary[ip] = time
    list_of_paths.append([])
    list_of_paths[visitor_ID].append(page)
    ip_ID_dictionary[ip] = visitor_ID
    visitor_ID = visitor_ID + 1

    # Blok 2
    past_time = ip_time_dictionary[ip]
    time_spend = datetime.strptime(time, '%H:%M:%S') - datetime.strptime(past_time, '%H:%M:%S')
    seconds = time_spend.seconds

    # Block 3
    ID = ip_ID_dictionary[ip]
    list_of_paths[ID].append(page)



##Deel 2 - TODO
# 1 Waarom maken we deze variabelen aan voor de loop?

# antwoord: Zodat we deze variabelen aan kunnen passen aan de hand van de variabelen in de lijst en de condities in de loop.
# en er later conclusies uit kunnen trekken. bijvoorbeeld totaal aantal bezoekers dat maar 1 pagina gebruikt.
# of bijvoorbeeld hoeveel bezoekers van welke naar welke pagina gaan (page combi) - todo not sure

one_page = 0
page_combos = dict()
current_page = 0

for path in list_of_paths:
    # 2 Welke conditie wordt hier gesteld en waarom is dat nodig?
    # er wordt gekeken of er maar 1 pagina in de lijst met path's zitten. Door de lengte van de lijst te vergelijken met 1.
    # Zo weten we of de unieke gebruiker maar 1 pagina heeft bezocht van de website.

    if len(path) == 1:
        one_page = one_page + 1
        # continue

    # 3 Wat is het nadeel van het gebruiken van else? Wat zou een alternatief zijn?
    # wordt de code onoverzichtelijker van. Meer complex. minder leesbaar.
    # je kunt beter continue toevoegen in de if hierboven

    else:
        for page in path:
            # 4 Waarom hebben we try en except nodig?
            # omdat er een index out of range exception kan voorkomen

            try:
                # 5 Leg uit wat er in de loop gebeurd. Doe dit eventueel in stapjes
                # er wordt een "Page combi" gecreerd aan de hand van de pagina's die deze gebruiker bezocht heeft.
                # dit is bullshit, waarom zou je current page gebruiken die buiten de loop wordt gedefinieerd? Deze code is zo corrupt als het maar kan.
                # ohh omdat je hem in de except weer op 0 zet. Maar dat is moeilijk lelijk. Zie code hieronder in de functie "beter"

                next_page = current_page + 1
                page_combi = '"' + path[current_page] + '-' + path[next_page] + '"'
                current_page = current_page + 1

                if page_combi not in page_combos:
                    page_combos[page_combi] = 1
                else:
                    page_combos[page_combi] = page_combos[page_combi] + 1
            except:
                current_page = 0

# ##Deel 2 - Beter.
#
# one_page = 0
# page_combos = dict()
#
# for path in list_of_paths:
#
#     if len(path) == 1:
#         one_page = one_page + 1
#         continue
#
#     for current_page_index, page in enumerate(path):
#
#         if current_page_index + 1 > len(path):
#             break
#
#         next_page_index = current_page_index + 1
#         page_combi = '"' + path[current_page_index] + '-' + path[next_page_index] + '"'
#
#         if page_combi not in page_combos:
#             page_combos[page_combi] = 1
#         else:
#             page_combos[page_combi] = page_combos[page_combi] + 1
