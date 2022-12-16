import numbers
import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier 


number = "+33614212907" 
ch_nmber = phonenumbers.parse(number, "CH")
service_number = phonenumbers.parse(number, "RO")

print(geocoder.description_for_number)(ch_nmber, "en")
print(carrier.name_for_number(service_number, "en")) 