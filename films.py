from tkinter import *
from tkinter import ttk

import requests

APIKEY = "7f593280"
URL = "http://www.omdbapi.com/?s={}&apikey={}" #El API KEY lo dejamos también en .format

class Searcher(ttk.Frame):

    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent)

        lblSearcher = ttk.Label(self, text = "Film:")
        self.ctrSearcher = StringVar()
        txtSearcher = ttk.Entry(self, width=30, textvariable=self.ctrSearcher)
        btnSearcher = ttk.Button(self, text="Search", command= lambda: command(self.ctrSearcher.get()))    #command None

        lblSearcher.pack(side=LEFT)  #Pegamos a la izquierda  
        txtSearcher.pack(side=LEFT)
        btnSearcher.pack(side=LEFT)

    def click(self):
        print(self.ctrSearcher.get())

class Controller(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=400, height=550)
        self.grid_propagate(False)  #No te propagues, quédate con la medida que te he dado

        self.searcher = Searcher(self, self.busca)
        self.searcher.grid(column=0, row=0)

        self.film = Film(self)
        self.film.grid(column=0, row=1)

    def busca(self, pelicula):
        print(pelicula, "desde el controller")

        url = URL.format(pelicula, APIKEY)
        results = requests.get(url)

        if results.status_code == 200:
            films = results.json()  #sabemos que nuestra APIK siempre devuelve un json
            if films.get("Response") == "True":
                pinicula = films.get("Search")[0]
                otra_pinicula = {"titulo": pinicula.get("Title"), "anno": pinicula.get("Year"), "poster": pinicula.get("Poster")}
                self.film.encontrada = otra_pinicula

        else:
            pass

        print(results.text)

class Film(ttk.Frame):
    __encontrada = None

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.lblTitle = ttk.Label(self, text="Titulo")
        self.lblYear = ttk.Label(self, text="1900")

        self.lblTitle.pack(side=TOP)
        self.lblYear.pack(side=TOP)

    @property
    def encontrada(self):
        return self.__encontrada

    @encontrada.setter
    def encontrada(self,value):
        self.__encontrada = value

        self.lblTitle.config(text=self.__encontrada.get("titulo"))
        self.lblYear.config(text=self.__encontrada.get("anno"))
    




'''
        if results.status_code == 200:
            <pintar resultados>
        else:
            <pintar un error>


        print(results.status_code)
        print(results.text)

        

        parameters = {'s': pelicula, 'apikey': APIKEY}
        results = requests.get("http://www.omdbapi.com/", data=parameters)

        print(results.status_code)
        print(results.text)

        '''