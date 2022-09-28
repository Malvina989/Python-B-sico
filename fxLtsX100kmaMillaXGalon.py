# Ayuda: 1 milla = 1609.344 metros.
#        1 galón = 3.785411784 litros.
# Pasar litros cada 100km a millas por galón tomando como arg los litros
def liters_100km_to_miles_gallon(liters):
    milla = 100000/ 1609.344
    galon = liters/3.785411784
    return milla / galon

# Pasar miilas por galón a litros cada 100 km
def miles_gallon_to_liters_100km(miles):
    km = 100000 / 1609.344 
    litros = (km * 3.785411784)
    return litros / miles
    
# Pruebas
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
