#We openen bestand in python, we stoppen deze functie in de naam 'file'
#Met 'r' geven we aan het bestand te openen om te lezen (read).
file = open('*.txt', 'r')
#We lezen alle regels in het bestand, deze functie in de naam 'lines'.
lines = file.readlines() 
#We sluiten het bestand weer, zodat we deze dadelijk kunnen open in 'Write-mode'. 
file.close() 

#We openen het bestand in write-mode zodat we het kunnen bewerken
file = open('*.txt', 'w')
#We loopen door alle gelezen regels
for line in lines:
  #Beschrijf de voorwaarden van de regels die bewaard moeten worden
  if 'mijndomein.nl proxybot/0.1' not in line and 'wp' not in line and 'action' not in line and 'env' not in line and 'ucp' not in line:
    #de regel die voldoet, wordt opgeslagen in het databestand
    file.write(line)
#We sluiten het bestand
file.close()
print ('Klaar!')