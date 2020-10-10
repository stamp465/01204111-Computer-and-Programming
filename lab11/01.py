import csv

class Country:
  nbCountry = 0
  def __init__(self, country, population, EU,coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry += 1

def readfile(file) :
	f = open(file)
	Countries = csv.DictReader(f)
	#print(type(Countries))
	lis_of_country = []
	for i in Countries :
		lis_of_country.append( Country(i['country'],i['population'],i['EU'],i['coastline']) )
	return lis_of_country


file = input("Enter File name: ")
lis = readfile(file)
#print(Country.nbCountry)
for i in lis :
	if i.EU == 'no' and i.coastline == 'yes' :
		print(i.country,i.population)