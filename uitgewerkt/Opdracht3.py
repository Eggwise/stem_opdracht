##Deel 1
#Plak hier jouw code van Opdracht 2, Deel 1

#Voeg deze onderdelen toe:

import time #Bovenaan, bij het importeren van de andere libraries

list_path_time=[] #Voor de loop, bij de andere 'lege' variabelen

#In blok 1:
ip_time_dictionary[ip]=time
list_of_paths.append([])
list_of_paths[visitor_ID].append(page)
ip_ID_dictionary[ip]=visitor_ID
list_path_time.append([]) #Toevoeging Tijd
list_path_time[visitor_ID].append((page, time)) #Toevoeging Tijd
visitor_ID=visitor_ID+1

#In blok 3:
ID=ip_ID_dictionary[ip]
list_of_paths[ID].append(page)
list_path_time[ID].append((page, time)) #Toevoeging Tijd


##Deel 2
#Definities tijdstippen voor later gebruik
Office_hours_start=datetime.strptime('09:00:00', '%H:%M:%S').strftime('%H:%M:%S')
Office_hours_end=datetime.strptime('17:00:00', '%H:%M:%S').strftime('%H:%M:%S')
visit_times={'During office hours':0, 'Outside of office hours': 0}

#We loopen door de lijst
for i in list_path_time:
  time_object=datetime.strptime(i[0][1],'%H:%M:%S').strftime('%H:%M:%S')
  if time_object >= Office_hours_start and time_object<Office_hours_end:
    visit_times['During office hours']+=1
  elif time_object >= Office_hours_end or time_object < Office_hours_start:
    visit_times['Outside of office hours']+=1

print (visit_times)


##Deel 3
list_of_visit_durations=[]

for i in list_path_time:
  if len(i)==1:
    continue
  else:
    first_time=i[0][1]
    last_time=i[-1][1]
    time_online=(datetime.strptime(last_time, '%H:%M:%S') - datetime.strptime(first_time, '%H:%M:%S')).seconds
    list_of_visit_durations.append(time_online)

print (list_of_visit_durations)



##Deel 4
one_page=0
page=0
#Maak een lijst aan per pagina, zoals hieronder. We slaan hier in op hoe lang de pagina is bezocht, als losse items zodat we er later beter statistische analyses mee uit kunnen voeren.
home_page_times=[]
contact_page_times=[]
journal_page_times=[]
about_page_times=[]

#Loopen door lijst van gekoppelde pagina's en tijdstippen
for i in list_path_time:
  #Uitzondering voor bezoeker van maar een pagina
  if len(i) == 1:
    one_page+=1
    page=0
  else:
    #we loopen door iedere tuple in de lijst
    for combination in i:
      #We werken met Try en Except omdat we werken met de tijd van iedere pagina en de opvolgende. Bij laatst bezochte pagina is dit echt niet mogelijk. Zo voorkomen we een traceback.
      try:
        #Deze twee variabelen dienen als index
        next_page=page+1
        #We halen de tijdstippen uit de tuples. De eerste index voor het aanwijzen van de tuple, de tweede voor het item in de tuple. Dit geeft ons twee strings die we opslaan in variabelen.
        time_page1=i[page][1]
        time_page2=i[next_page][1]
        #We trekken tijdstip 2 van 1 af, zo zien we hoeveel seconden het duurde voor de bezoeker de volgende pagina bezocht.
        #We gebuiken functies uit de time library. Eerst converten we beide strings naar het juiste format, dan trekken we ze van elkaar af, en dan converten we het overgebleven 'tijdstip' naar seconden.
        time_on_page=(datetime.strptime(time_page2, '%H:%M:%S') - datetime.strptime(time_page1, '%H:%M:%S')).seconds
        #We slaan alleen het bezoek op wanneer dit langer dan 5 seconden was. Zo voorkomen we opslag van 'toevallige' activiteiten
        if time_on_page > 5:
          #We moeten het gegeven in de juiste lijst opslaan. Je moet een voorwaarde aanmaken voor iedere pagina die je hebt. Tip: door (list_path_time) te printen, zie je de pagian namen. Zo controleer je makkelijk of je ze allemaal gehad hebt, en hoe ze precies opgeslagen zijn. Tip: een deel van de string overnemen is voldoende, houdt je code netjes.
          #Tip: als je pagina redirect van home, zie je dat deze ook telkens is opgeslagen. Gebruik home dan als laatste statement.
          if 'contact' in i[page][0]:
            contact_page_times.append(time_on_page)
          elif 'journal' in i[page][0]:
            journal_page_times.append(time_on_page)
          elif 'about' in i[page][0]:
            about_page_times.append(time_on_page)    
          elif 'home' in i[page][0]:
            home_page_times.append(time_on_page)
        #We verhogen de variabelen voor de index, dan nemen we in de loop het volgende item
        page+=1
      except:
        #Dit wordt uitgevoerd wanneer het einde van de lijst van een bezoeker bereikt is. We resetten de variabele, zodat we bij de volgende lijst weer aan het begin beginnen.
        page=0
#Pas de print-statements aan zodat je voor iedere lijst output hebt
print ('The amount of people that visited only one page: ', one_page)
print ('Home: ', home_page_times)
print ('Contact: ', contact_page_times)
print ('Journal: ', journal_page_times)
print ('About: ', about_page_times)