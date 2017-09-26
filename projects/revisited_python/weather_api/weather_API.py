import requests

package = {
    'APPID': "a7b8474154ce2639ffe7bb923a50a829", 'units': "imperial"
}


question = input('Would you like to search by (c)ity name of (z)ip?: ')
city = input("What city or zip are you looking for?: ")


if question == 'c':
    package['q'] = city
    r = requests.post('https://api.openweathermap.org/data/2.5/weather?q={}'.format(city), params=package)
else:
    package['zip'] = city
    r = requests.post('https://api.openweathermap.org/data/2.5/weather?zip={}'.format(city), params=package)

data = r.json()

# # Went ahead and checked outputs for the above posts
# print(data['main'])

print("Here's the current weather in {}:".format(city))
print("\n")
print("Current temperature is {}F".format(data['main']['temp']))
print("Current atmospheric pressure is {}hPa".format(data['main']['pressure']))
print("Current humidity is {}%".format(data['main']['humidity']))
print("Minimum temperature is {}F".format(data['main']['temp_min']))
print("Maximum temperature is {}F".format(data['main']['temp_max']))


