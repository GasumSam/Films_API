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

    def busca(self, pelicula):
        print(pelicula, "desde el controller")

        url = URL.format(pelicula, APIKEY)
        results = requests.get(url)

        print(results.text)

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