import csv

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

def readfile(file) :
  f = open(file)
  Cities = csv.DictReader(f)
  #print(type(Countries))
  lis_of_country = []
  for i in Cities :
    lis_of_country.append( City( i['city'],i['country'],i['latitude'],i['longitude'],i['temperature']  ) )
  return lis_of_country


file = input("Enter file name: ")
lis = readfile(file)
for i in City.sumtemincountry :
  print(i,"%.2f"%(City.sumtemincountry[i]/City.nubcityincountry[i]))
