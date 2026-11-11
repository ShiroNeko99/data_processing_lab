import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

from email.quoprimime import unquote

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All cities in Germany")
for city in cities:
    if city["country"] == "Germany":
        print(city)
print()

# Print all cities in Spain with a temperature above 12°C

print("City in Spain that temperature above 12°C")
for city in cities:
    if city["country"] == "Spain" and float(city["temperature"]) > 12:
        print(city)
print()

# Count the number of unique countries

unique_country = []

for city in cities:
    if city["country"] not in unique_country:
        unique_country.append(city["country"])

print(f"Number of unique countries: {len(unique_country)}")
print()

# Print the average temperature for all the cities in Germany

germany_all_temp = [float(city['temperature']) for city in cities]
print(f"Average temperature for all Germany cities: {sum(germany_all_temp) / len(germany_all_temp):.2f}")
print()

# Print the max temperature for all the cities in Italy

itary_all_temp = [float(city['temperature']) for city in cities]
print(f"Italy max temperature: {max(itary_all_temp)}")
print()