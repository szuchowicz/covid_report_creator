from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from covid_ui import Ui_MainWindow
import pandas as pd
import requests

import sys


class CovidReport(QtWidgets.QMainWindow):

    def get_data(self):
        """
        Collect current data from website, if cannot access website get data from last file
        :return:
        Pandas dataframe containing current covid-19 data from around world
        """

        source_url= 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
        data_path = "Data/covid_data.csv"

        try:
            """
            Checking header type - if correct update file, else get previous data
            """

            header = requests.head(source_url, allow_redirects=True).headers.get('content-type')

            if header == "application/octet-stream":
                new_data = requests.get(source_url, allow_redirects=True)
                open(data_path, "wb").write(new_data.content)

                url_connected = QMessageBox.information(self, "Data collected", "Newest data collected from website")
            else:
                url_error = QMessageBox.warning(self, "URL connection error",
                                                "Unable to connect to website, getting data from last file")

        except Exception:
            url_error = QMessageBox.warning(self, "URL connection error",
                                            "Unable to connect to website, getting data from last file")

        finally:
            """
            Trying to open existing data file
            """

            try:
                self.covid_df = pd.read_csv(data_path)
            except IOError as e:
                pandas_error = QMessageBox.critical(self, "Error", "Unable to read data file")

    def load_list(self):
        """
        Fill country list with country from loaded data
        """

        country_list = [country for country in self.covid_df["countriesAndTerritories"]]
        self.country_list = list(set(country_list))
        self.country_list.sort()

        self.ui.countryList.addItems(self.country_list)
        self.ui.countryList.insertItem(0, 'All')
        #TODO add filter by search box input

    def percent_count(self, total_amount, increase):

        previus_day_amount = total_amount - increase
        if previus_day_amount == 0:
            return "N/A"
        else:
            percent_val = round(increase / previus_day_amount * 100, 2)
            return percent_val

    def selected_country_values(self, selectedItem):
        """
        Update labels depends on item selected from countryList by user
        :param selectedItem:
        :return:
        """


        if selectedItem.text() == "All":
            self.ui.selectedDate.setText(self.covid_df['dateRep'].values[0])
            self.ui.selectedCountry.setText("All the world")

            sorted_by_date = self.covid_df.sort_values("dateRep")
            self.ui.selectedFirstCase.setText(sorted_by_date['dateRep'].values[-1])

            last_day_df = self.covid_df.loc[self.covid_df['dateRep'] == self.covid_df['dateRep'].values[0]]

            # prelast_day_df = self.covid_df.loc[self.covid_df['dateRep'] == self.covid_df['dateRep'].values[1]]

            self.ui.selectedLastDayCases.setText(str(last_day_df['cases'].sum()))

            """
            Count % increse cases and deaths
            
            previous_day_cases = self.covid_df['cases'].sum() - last_day_df['cases'].sum()
            cases_percent = last_day_df['cases'].sum() / previous_day_cases
            cases_percent = round(cases_percent*100, 2)

            previous_day_deaths = self.covid_df['deaths'].sum() - last_day_df['deaths'].sum()
            deaths_percent = last_day_df['deaths'].sum() / previous_day_deaths
            deaths_percent = round(deaths_percent * 100, 2)
            """
            self.ui.selectedPercentDayCases.setText(
                str(self.percent_count(self.covid_df['cases'].sum(), last_day_df['cases'].sum())) + "%")

            self.ui.selectedLastDayDeaths.setText(str(last_day_df['deaths'].sum()))
            self.ui.selectedPercentDayDeaths.setText(
                str(self.percent_count(self.covid_df['deaths'].sum(), last_day_df['deaths'].sum())) + "%")

            self.ui.selectedTotalCases.setText(str(self.covid_df['cases'].sum()))
            self.ui.selectedTotalDeaths.setText(str(self.covid_df['deaths'].sum()))

        else:
            """
            Slicing selected country from data file
            """
            selected_country_df = self.covid_df.loc[
                self.covid_df["countriesAndTerritories"] == selectedItem.text()]

            self.ui.selectedDate.setText(selected_country_df['dateRep'].values[0])
            self.ui.selectedCountry.setText(selectedItem.text())
            self.ui.selectedFirstCase.setText(selected_country_df['dateRep'].values[-1])

            self.ui.selectedLastDayCases.setText(str(selected_country_df['cases'].values[0]))
            self.ui.selectedPercentDayCases.setText(
                str(self.percent_count(selected_country_df['cases'].sum(), selected_country_df['cases'].values[0]))
                + "%")

            self.ui.selectedLastDayDeaths.setText(str((selected_country_df['deaths'].values[0])))
            self.ui.selectedPercentDayDeaths.setText(
                str(self.percent_count(selected_country_df['deaths'].sum(), selected_country_df['deaths'].values[0]))
                + "%")

            self.ui.selectedTotalCases.setText(str(selected_country_df['cases'].sum()))
            self.ui.selectedTotalDeaths.setText(str(selected_country_df['deaths'].sum()))

    def __init__(self):
        super(CovidReport, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """
        Geting data and loading
        """
        self.get_data()
        self.load_list()

        self.ui.countryList.itemClicked.connect(self.selected_country_values)

        #TODO add creating xls reports and visualisation

app = QtWidgets.QApplication([])
application = CovidReport()

application.show()


sys.exit(app.exec())
