import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .Requetage import Requetage

class InterfaceData:
    def __init__(self, ListeDomaines, ListeRessources):
        self.RQ = Requetage("BerneProject/DBBibliotheque.db")
        self.RQ.connect()
        self.window = tk.Tk()
        self.window.title("Bibliothèque Data Visualization")
        self.fig, self.ax = plt.subplots()
        
        # Calcul pour centrer la fenêtre
        window_width = 1080
        window_height = 720
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Création d'un Frame pour les menus déroulants
        self.dropdown_frame = tk.Frame(self.window)
        self.dropdown_frame.pack(pady=10)

        ### Domaine ###
        
        self.LabelDomaine = tk.Label(self.dropdown_frame, text="Domaine")
        self.LabelDomaine.grid(row=0, column=0, padx=5)
        
        self.domaines_combobox = ttk.Combobox(self.dropdown_frame, width=20, values=ListeDomaines)
        self.domaines_combobox.grid(row=1, column=0, padx=5)
        
        ### Ressource ###
        
        self.LabelRessource = tk.Label(self.dropdown_frame, text="Ressource")
        self.LabelRessource.grid(row=0, column=1, padx=5)

        self.resources_combobox = ttk.Combobox(self.dropdown_frame, width=20, values=ListeRessources)
        self.resources_combobox.grid(row=1, column=1, padx=5)
        
        ### Date début ###
        
        self.LabelDateDebut = tk.Label(self.dropdown_frame, text="Date de début (AAAA-MM-JJ)")
        self.LabelDateDebut.grid(row=0, column=2, padx=5)

        # Menu déroulant pour l'analyse temporelle
        self.debutDate = ttk.Entry(self.dropdown_frame, width=20)
        self.debutDate.grid(row=1, column=2, padx=5)
        
        ### Date fin ###
        
        self.LabelDateFin = tk.Label(self.dropdown_frame, text="Date de fin (AAAA-MM-JJ)")
        self.LabelDateFin.grid(row=0, column=3, padx=5)
        
        self.finDate = ttk.Entry(self.dropdown_frame, width=20)
        self.finDate.grid(row=1, column=3, padx=5)

        # Définir les sélections par défaut pour chaque combobox
        self.domaines_combobox.current(0)
        self.resources_combobox.current(0)

        # Emballage du bouton avant le canvas
        self.generate_button = tk.Button(self.window, text="Générer Graphique", command=self.GenerationGraphique, width=20)
        self.generate_button.pack(pady=5)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def GenerationGraphique(self):
        rq = Requetage("BerneProject/DBBibliotheque.db")
        rq.connect()
        
        domaine = self.domaines_combobox.get()        
        ressource = self.resources_combobox.get()
        dateDebut = self.debutDate.get()
        dateFin = self.finDate.get()
        if dateDebut < "2021-09-01" or dateFin > "2022-06-01":
            # Afficher un message d'erreur
            self.LabelError = tk.Label(self.dropdown_frame, text="Date invalide", fg="red")
            self.LabelError.grid(row=2, column=0, columnspan=4)
        
        self.ax.clear()
        
        ### Faire une courbe dans le temps pour les emprunts selon les domaines et les ressources ###
        
        try:
            if hasattr(self, 'LabelError'):
                self.LabelError.destroy()
    
            dataGraphique = rq.TauxEmpruntDansleTemps(dateDebut, dateFin, domaine, ressource)
            Dates, Taux = zip(*dataGraphique)
            self.ax.plot(Dates, Taux)
        except ValueError:
            self.LabelError = tk.Label(self.dropdown_frame, text="Pas de prets pour cette période", fg="red")
            self.LabelError.grid(row=2, column=0, columnspan=4)
        
        self.ax.set_title("Taux d'emprunt par domaines")
        self.ax.set_xlabel('Jours')
        self.ax.set_ylabel('Taux de prêt (%)')
        self.canvas.draw()
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    interface = InterfaceData(["Domaine1", "Domaine2", "Domaine3"], ["Ressource1", "Ressource2", "Ressource3"])
    interface.run()
