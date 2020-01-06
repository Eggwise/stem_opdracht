##Deel 1 ## Het bestand openen
import csv

# de strato klanten hebben als delimiter een spatie.

with open('data.txt') as csvfile:
  file = csv.reader(csvfile, delimiter=',')
    
  linecount=0
  for line in file:
    if linecount == 0:
      print('Column names are:', ', '.join(line))
      linecount=1
    else:
      print('De datum waarop de website bezocht werd was:',''.join(line[0]),', de bezochte pagina was: ',''.join(line[3]))


##Deel 2 ## Bezoekers onderscheiden
import csv

with open('DataOpslagSTEM_.txt') as csvfile:
  file = csv.reader(csvfile, delimiter=',')
    
  linecount=0
  list_of_ips=list()
  for line in file:
    if linecount==0:
      linecount=1
    else:
      ip=line[...]
      print (ip)
      if ip in list_of_ips:
        continue
      else:
        list_of_ips.append(ip)
print (list_of_ips)
print (len(list_of_ips))

##Deel 3
import csv

with open('DataOpslagSTEM_.txt') as csvfile:
    file = csv.reader(csvfile, delimiter=',')

    linecount = 0
    ip_count=dict()
    for line in file:
      if linecount==0:
        linecount=1
      else:
        ip=line[...]
        if ip not in ip_count:
          ip_count[ip]=1
        else:
          ip_count[ip]=ip_count[ip]+1
print (ip_count)