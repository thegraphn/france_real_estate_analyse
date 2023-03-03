import streamlit as st


class Visualizer:
    def __init__(self, list_data_frames):
        self.list_data_frames = list_data_frames
        self.st = st

    def setUp(self):
        self.st.set_page_config(page_title='Prices in France for the postal code',
                                page_icon=':soccer:',
                                layout='wide',
                                initial_sidebar_state='auto')

    def display(self):
        self.setUp()
        self.st.title("Prices in France for the postal code")
        self.st.write(
            "This is a demo of a Streamlit app that displays the evolution of the prices of houses and apartments in France for a given postal code.")
        self.st.write(
            "The data is from the [Open Data of the French government](https://www.data.gouv.fr/en/datasets/demandes-de-valeurs-foncieres-des-ventes-de-terrains-et-de-biens-immeubles/).")

        # for each data frame  year and plot
        for data_frame in self.list_data_frames:
            for col in data_frame.columns:
                self.st.write(col)

                print(data_frame["postal_code"].tolist())
                self.st.write("Post code: " + str(data_frame["postal_code"].tolist()[0]))
                self.st.write(data_frame[col])

    def run(self):
        self.display()


import os

# os.system("streamlit run /home/graphn/repository/france_real_estate_analyse/fpl-app.py")
