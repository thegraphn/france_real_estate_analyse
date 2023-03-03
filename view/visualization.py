import streamlit as st


class Visualizer:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.st = st

    def setUp(self):
        self.st.set_page_config(page_title='Prices in France for the postal code',
                                page_icon=':building_construction:',
                                layout='wide',
                                initial_sidebar_state='auto')

    def display(self):
        self.setUp()
        self.st.title("Prices in France for the postal code")
        self.st.write(
            "This is a demo of a Streamlit app that displays the evolution of the prices of houses and apartments in France for a given postal code.")
        self.st.write(
            "The data is from the [Open Data of the French government](https://www.data.gouv.fr/en/datasets/demandes-de-valeurs-foncieres-des-ventes-de-terrains-et-de-biens-immeubles/).")
        for col in self.data_frame.columns:
            if col !="postal_code":
                self.st.write(col)
                self.st.bar_chart(data=self.data_frame,y=col,x="postal_code")



    def run(self):
        print("run")
        self.display()


import os

# os.system("streamlit run /home/graphn/repository/france_real_estate_analyse/fpl-app.py")
