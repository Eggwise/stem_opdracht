## Deel 1
import csv
from datetime import datetime, time

ip_time_dictionary=dict() #om het IP-adres te koppelen aan het meest recente tijdstip
ip_ID_dictionary=dict() #om het IP-adres te koppelen aan een ID-nummer, zo kunnen we naar de lijst van deze bezoeker verwijzen
current_date = 0 #om de meest recente datum op te slaan
visitor_ID=0 #om het ID-nummer te maken
list_of_paths=[] #om de lijsten van de bezoekers op één plek op te slaan


with open('.txt') as csvfile:
    file = csv.reader(csvfile, delimiter=",")

    linecount=0
    for line in file:
      if linecount == 0:
        linecount=1
      else:
        ip=line[2]
        time=line[1]
        date=line[0]
        # voor strato het volgende aanpassen:
        #datumentijd=line[4] #deze regel toevoegen
        #time =datumentijd[11:18] #time op deze manier aanpassen
        #date =datumentijd[1:12] #date op deze manier aanpassen
        page = line[3]
        if ip not in ip_time_dictionary:
          #
        else:
          if date != current_date: #Vraag 5
            #
            current_date=date
          else:
            #
            if seconds > 1800:
              #
            else:
              #

print (list_of_paths)

#Blok 1
ip_time_dictionary[ip]=time
list_of_paths.append([])
list_of_paths[visitor_ID].append(page)
ip_ID_dictionary[ip]=visitor_ID
visitor_ID=visitor_ID+1

#Blok 2
past_time=ip_time_dictionary[ip]
time_spend=datetime.strptime(time, '%H:%M:%S') - datetime.strptime(past_time, '%H:%M:%S')
seconds = time_spend.seconds

#Block 3
ID=ip_ID_dictionary[ip]
list_of_paths[ID].append(page)

##Deel 2
#1 Waarom maken we deze variabelen aan voor de loop?
one_page=0
page_combos=dict()
current_page=0

for path in list_of_paths:
  #2 Welke conditie wordt hier gesteld en waarom is dat nodig?
  if len(path) == 1:
    one_page=one_page+1
  #3 Wat is het nadeel van het gebruiken van else? Wat zou een alternatief zijn?
  else:
    for page in path:
      #4 Waarom hebben we try en except nodig?
      try:
        #5 Leg uit wat er in de loop gebeurd. Doe dit eventueel in stapjes
        next_page=current_page+1
        page_combi='"' + path[current_page] + '-' +path[next_page] + '"'
        current_page=current_page+1
        if page_combi not in page_combos:
          page_combos[page_combi]=1
        else:
          page_combos[page_combi]=page_combos[page_combi]+1
      except:
        current_page=0
print
print