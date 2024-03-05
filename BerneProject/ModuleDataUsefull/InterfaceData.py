import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .Requetage import Requetage

class InterfaceData:
    def __init__(self):
        self.RQ = Requetage("BerneProject/DBBibliotheque.db")
        self.RQ.connect()
        self.window = tk.Tk()
        self.window.title("Bibliothèque Data Visualization")
        self.fig, self.ax = plt.subplots()
        
        # Calcul pour centrer la fenêtre
        window_width = 600
        window_height = 400
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Création d'un Frame pour les menus déroulants
        self.dropdown_frame = tk.Frame(self.window)
        self.dropdown_frame.pack(pady=10)

        # Menu déroulant pour le choix du domaine
        self.domain_combobox = ttk.Combobox(self.dropdown_frame, width=20, values=['Aucun','Domaine1', 'Domaine2', 'Domaine3'])
        self.domain_combobox.grid(row=0, column=0, padx=5)

        # Menu déroulant pour le choix de la ressource
        self.resource_combobox = ttk.Combobox(self.dropdown_frame, width=20, values=['Aucun','Ressource1', 'Ressource2', 'Ressource3'])
        self.resource_combobox.grid(row=0, column=1, padx=5)

        # Menu déroulant pour l'analyse temporelle
        self.temporal_analysis_combobox = ttk.Combobox(self.dropdown_frame, width=20, values=['Jour', 'Semaine', 'Mois', 'Semestre', 'Année'])
        self.temporal_analysis_combobox.grid(row=0, column=2, padx=5)

        # Définir les sélections par défaut pour chaque combobox
        self.domain_combobox.current(0)
        self.resource_combobox.current(0)
        self.temporal_analysis_combobox.current(0)

        # Emballage du bouton avant le canvas
        self.generate_button = tk.Button(self.window, text="Générer Graphique", command=self.GenerationGraphique, width=20)
        self.generate_button.pack(pady=5)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def GenerationGraphique(self):
        selection = self.combo_box.get()
        self.ax.clear()

        if selection == 'Analyse des prêts par domaine':
            data = self.RQ.analyse_prets_par_domaine()
            domains, counts = zip(*data)
            self.ax.bar(domains, counts)
        elif selection == 'Tendance des prêts selon le jour de la semaine':
            data = self.RQ.tendance_prets_selon_jour_semaine()
            days, counts = zip(*data)
            self.ax.bar(days, counts)
        elif selection == 'Durée moyenne des prêts selon le type de ressource':
            data = self.RQ.duree_moyenne_prets_selon_type_ressource()
            types, averages = zip(*data)
            self.ax.bar(types, averages)

        self.ax.set_title(selection)
        self.canvas.draw()
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    interface = InterfaceData()
    interface.run()
