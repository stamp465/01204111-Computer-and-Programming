import csv

class Country:
  nbCountry = 0
  def __init__(self, country, population, EU,coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry += 1
  def inEu_coastline (self) :
    return self.EU == 'no' and self.coastline == 'yes'

class City:
  nbCity = 0
  sumtemincountry = {}
  nubcityincountry = {}
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    City.nbCity += 1
    if country not in City.sumtemincountry.keys() :
      City.sumtemincountry[country] = 0
    City.sumtemincountry[country] += float(temperature)
    if country not in City.nubcityincountry.keys() :
      City.nubcityincountry[country] = 0
    City.nubcityincountry[country] += 1

def readfile_city(file) :
  f = open(file)
  Cities = csv.DictReader(f)
  #print(type(Countries))
  lis_of_country = []
  for i in Cities :
    lis_of_country.append( City( i['city'],i['country'],i['latitude'],i['longitude'],i['temperature']  ) )
  return lis_of_country

def readfile_country(file) :
  f = open(file)
  Countries = csv.DictReader(f)
  #print(type(Countries))
  lis_of_country = []
  for i in Countries :
    lis_of_country.append( Country(i['country'],i['population'],i['EU'],i['coastline']) )
  return lis_of_country


file1 = input("Enter city file: ")
lis1 = readfile_city(file1)
file2 = input("Enter country file: ")
lis2 = readfile_country(file2)
print("Average temperature of countries having coastline, but not in EU:")
for i in lis2 :
  if i.inEu_coastline() :
    if i.country in City.sumtemincountry.keys() :
      print(i.country,"%.2f"%(City.sumtemincountry[i.country]/City.nubcityincountry[i.country]))