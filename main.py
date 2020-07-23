import requests

URL = "http://www.omdbapi.com/?s={}&apikey=7f593280"

pelicula = input('Buscar: ')

respuesta = requests.get(URL.format(pelicula))

print(respuesta.text)   #Parámetro de request

mijson = respuesta.json  #JSON transformado en cadena para viajar por internet

#Json pasa a ser un diccionario

print(mijson.get("Search")[0].get("Title"))   #.get solo puedes hacerlo en los diccionarios
print(mijson.get("Search")[0].get("Poster"))