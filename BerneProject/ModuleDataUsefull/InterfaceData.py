import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class InterfaceData:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bibliothèque Data Visualization")
        
        # Calcul pour centrer la fenêtre
        window_width = 600  # Largeur souhaitée
        window_height = 400  # Hauteur souhaitée
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Agrandissement du menu déroulant et du bouton
        self.combo_box = ttk.Combobox(self.window, width=50, values=['Analyse des prêts par domaine', 'Tendance des prêts selon le jour de la semaine', 'Durée moyenne des prêts selon le type de ressource'])
        self.combo_box.current(0)

    def GenerationGraphique(self):
        print("Graphique généré !")

    def CreationBoutton(self):
        generate_button = tk.Button(self.window, text="Générer Graphique", command=self.GenerationGraphique, width=20)
        generate_button.pack(pady=5)

    def CreationComboBox(self):
        self.combo_box.pack(pady=10)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    interface = InterfaceData()
    interface.CreationComboBox()
    interface.CreationBoutton()
    interface.run()
