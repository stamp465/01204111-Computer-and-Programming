import csv

class City:
  nbCity = 0
  summ = 0
  minn = 1e9
  maxx = -1
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    City.nbCity += 1
    City.minn = min(float(temperature),City.minn)
    City.maxx = max(float(temperature),City.maxx)
    City.summ += float(temperature)

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
print("Minimum: %.2f"%City.minn)
print("Maximum: %.2f"%City.maxx)
print("Average temperature: %.4f"%(City.summ/City.nbCity))