"""Model statistics of a given data frame"""

import pandas as pd


class ModelStatistics:
    """Model statistics of a given data frame"""

    def __init__(self, data_frame: pd.DataFrame):
        self.mean_per_year = {}
        self.price_year_evolution = {}
        self.data_frame = data_frame
        self.price_column = "valeur_fonciere"
        self.year_column = "date_mutation"
        self.ground_surface_column = "surface_terrain"
        self.building_surface_column = "surface_reelle_bati"
        self.type_local_column = "type_local"
        self.postal_code = data_frame["code_postal"].tolist()[0]
        self.number_of_sales = len(data_frame)
        self.report = pd.DataFrame()
        self.report["postal_code"] = [self.postal_code]

    def compute_mean_value_square_meter_per_year(self):
        """For each year, compute the mean square meter price"""
        list_years = set([year.split("-")[0] for year in self.data_frame[self.year_column].unique()])
        # convert years to int
        list_years = [int(year) for year in list_years]
        # compute ration square meter price and create a new column
        self.data_frame["price_per_square_meter"] = self.data_frame[self.price_column] / self.data_frame[
            self.building_surface_column]


        for year in list_years:
            self.mean_per_year[year] = self.data_frame[self.data_frame[self.year_column].str.contains(str(year))][
                "price_per_square_meter"].mean()
        # add to self.report
        for year,value in self.mean_per_year.items():
            self.report[str(year)+"_mean_price_per_square_meter"] = [value]

    def compute_value_evolution(self):
        """Compute the evolution of the price between the
        years"""
        for year1, price1 in self.mean_per_year.items():
            for year2, price2 in self.mean_per_year.items():
                if year1 != year2 and year1 > year2:
                    self.price_year_evolution[year1, year2] = price2 - price1

        # add to self.report
        for year1_year2, price_evolution in self.price_year_evolution.items():
            #convert tuple year1_year2 to string
            year1_year2 = str(year1_year2[0])+"_"+str(year1_year2[1])
            self.report[year1_year2+"_difference"] = [price_evolution]
