from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='tantan')
location = geolocator.geocode("Noida")
print(location.address)

print((location.latitude, location.longitude))
print(location.raw)

