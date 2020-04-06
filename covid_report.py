from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from covid_ui import Ui_MainWindow
import pandas as pd
import requests
import xlsxwriter
from datetime import datetime

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
                '''
                Load csv file to dataframe and reformat columns
                '''
                self.covid_df = pd.read_csv(data_path)

                self.covid_df = self.covid_df.rename(columns={'dateRep': 'Date'})


            except IOError as e:
                pandas_error = QMessageBox.critical(self, "Error", "Unable to read data file")

    def load_list(self):
        """
        Fill country list with country from loaded data
        """

        self.ui.countryList.clear()
        country_list = [country for country in self.covid_df["countriesAndTerritories"]]

        # Remove duplicates
        self.country_list = list(set(country_list))
        self.country_list.sort()
        self.country_list.insert(0, 'All')
        searched_country = self.ui.searchCountry.toPlainText()

        if len(searched_country) > 1:
            self.country_list = [country for country in self.country_list
                                 if searched_country.lower() in country.lower()]

        self.ui.countryList.addItems(self.country_list)

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
        """

        self.selected_item = selectedItem.text()

        if selectedItem.text() == "All":
            self.ui.selectedDate.setText(self.covid_df['Date'].values[0])
            self.ui.selectedCountry.setText("All the world")

            sorted_by_date = self.covid_df.sort_values("Date")
            self.ui.selectedFirstCase.setText(sorted_by_date['Date'].values[-1])

            last_day_df = self.covid_df.loc[self.covid_df['Date'] == self.covid_df['Date'].values[0]]

            self.ui.selectedLastDayCases.setText(str(last_day_df['cases'].sum()))

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

            self.ui.selectedDate.setText(selected_country_df['Date'].values[0])
            self.ui.selectedCountry.setText(selectedItem.text())
            self.ui.selectedFirstCase.setText(selected_country_df['Date'].values[-1])

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

    def create_xls(self):
        """
        Create xls report for selected country using xlsxwriter
        Tab 'Summary' includes general info and amount of cases and deaths
        Tab "Day_by_day' includes each day statistics
        :return: xls file with country name and current date as filename
        """
        date = datetime.now().strftime('%Y%m%d')
        if self.selected_item == "All":
            xls_name = f"Global_{date}.xlsx"
            selected_data = self.covid_df

        elif self.selected_item is None:
            selection_warning = QMessageBox.warning(self, "No country selected", "Please select country for report")
            return False

        else:
            xls_name = f"{self.selected_item}_{date}.xlsx"
            selected_data = self.covid_df.loc[
                self.covid_df['countriesAndTerritories'] == self.selected_item]

        '''
        Create file and add worksheets
        '''
        xls_name = f"Reports/{xls_name}"
        xls_file = xlsxwriter.Workbook(xls_name)
        summary = xls_file.add_worksheet("Summary")
        day_by_day = xls_file.add_worksheet("Day_by_day")



        # Create formats for workbook

        header_format = xls_file.add_format({'bold': True,
                                             'font_size': '12',
                                             'border': 1,
                                             'align': 'center_across'})

        col_A_format = xls_file.add_format({'border': 1,
                                            'align': 'left'})

        col_B_format = xls_file.add_format({'border': 1,
                                            'align': 'right',
                                            'font_color': 'red'})

        date_format = xls_file.add_format({'num_format': 'dd mmm yyyy',
                                           'border': 1,
                                           'align': 'left',
                                           'bold': True})

        percent_increase_format = xls_file.add_format({'border': 1,
                                                       'italic': True,
                                                       'font_color': 'green',
                                                       'align': 'center',
                                                       'num_format': '0.00%'})
        '''
        Filling and formatting summary tab
        '''

        summary.set_default_row(hide_unused_rows=True)
        summary.set_column('C:XFD', None, None, {'hidden': True})

        summary.set_column(0, 1, 12.15)
        summary.merge_range('A1:B1', self.selected_item, header_format)

        summary.write('A2', "Date:", col_A_format)
        summary.write('B2', selected_data['Date'].values[0], col_B_format)

        summary.write(2, 0, "Total cases:", col_A_format)
        summary.write(2, 1, selected_data['cases'].sum(), col_B_format)

        summary.write(3, 0, "Total deaths:", col_A_format)
        summary.write(3, 1, selected_data['deaths'].sum(), col_B_format)

        summary.write(4, 0, "First case:", col_A_format)
        summary.write(4, 1, selected_data['Date'].values[-1], col_B_format)


        '''
        Filling and formatting day_by_day tab
        '''

        # Simplify dataframe by dropping columns

        selected_data = selected_data.drop(['day', 'month', 'year', 'geoId',
                                            'countryterritoryCode', 'popData2018',
                                            'countriesAndTerritories'], axis=1)


        # If user choice is All world, sum up values by dates
        if self.selected_item == "All":

            global_values = selected_data.groupby('Date', axis=0, as_index=False).sum()
            global_values['Date'] = pd.to_datetime(global_values['Date'], format='%d/%m/%Y')
            global_values = global_values.sort_values(by=['Date'], ascending=False)
            global_values['Date'] = global_values['Date'].dt.strftime('%d/%m/%Y')

            selected_data_dict = global_values.to_dict()

        # Save dataframe as dict to put values into report
        else:
            selected_data_dict = selected_data.to_dict()

        day_by_day.set_column(0, 4, 12)
        day_by_day.set_column(5, 6, 17)

        # Write headers
        day_by_day.write(0, 0, "Date", header_format)
        day_by_day.write(0, 1, "Cases", header_format)
        day_by_day.write(0, 2, "Deaths", header_format)
        day_by_day.write(0, 3, "Total cases", header_format)
        day_by_day.write(0, 4, "Total deaths", header_format)
        day_by_day.write(0, 5, "% cases increase", header_format)
        day_by_day.write(0, 6, "% death increase", header_format)



        # Write values from dataframe based dict
        col_num = 0
        for key, value in selected_data_dict.items():
            row_num = 1
            day_by_day.write(row_num, col_num, key)

            for val in value.values():
                if col_num == 0:

                    # convert value to datetime
                    val = datetime.strptime(val, '%d/%m/%Y')
                    day_by_day.write_datetime(row_num, col_num, val, date_format)
                else:
                    day_by_day.write(row_num, col_num, val, col_B_format)
                row_num += 1
            col_num += 1

        # Write total cases and death for each day and % of increase

        if self.selected_item == "All":
            row_num = global_values['Date'].shape[0]
        else:
            row_num = selected_data['Date'].shape[0]

        row = row_num

        while row > 0:

            if row == row_num:
                day_by_day.write_formula(row, 3, f'=B{row+1}', col_B_format)
                day_by_day.write_formula(row, 4, f'=C{row+1}', col_B_format)
                day_by_day.write(row, 5, "=0", percent_increase_format)
                day_by_day.write(row, 6, "=0", percent_increase_format)

            else:
                day_by_day.write_formula(row, 3, f'=D{row+2}+B{row+1}', col_B_format)
                day_by_day.write_formula(row, 4, f'=E{row+2}+C{row+1}', col_B_format)

                # day_by_day.write_formula(row, 5, f'=B{row+1}/D{row+2}', percent_increase_format)

                '''
                Avoiding divide by 0 error in % increase columns
                '''
                if self.selected_item == "All":
                    if global_values.iloc[row:, global_values.columns.get_loc('deaths')].sum() == 0:
                        day_by_day.write_formula(row, 6, "=0", percent_increase_format)
                    else:
                        day_by_day.write_formula(row, 6, f'=C{row+1}/E{row+2}', percent_increase_format)

                    if global_values.iloc[row:, global_values.columns.get_loc('cases')].sum() == 0:
                        day_by_day.write_formula(row, 5, "=0", percent_increase_format)
                    else:
                        day_by_day.write_formula(row, 5, f'=B{row+1}/D{row+2}', percent_increase_format)
                else:
                    if selected_data.iloc[row:, selected_data.columns.get_loc('deaths')].sum() == 0:
                        day_by_day.write_formula(row, 6, "=0", percent_increase_format)
                    else:
                        day_by_day.write_formula(row, 6, f'=C{row+1}/E{row+2}', percent_increase_format)

                    if selected_data.iloc[row:, selected_data.columns.get_loc('cases')].sum() == 0:
                        day_by_day.write_formula(row, 5, "=0", percent_increase_format)
                    else:
                        day_by_day.write_formula(row, 5, f'=B{row+1}/D{row+2}', percent_increase_format)

            row -= 1

        xls_file.close()

        xls_done = QMessageBox.information(self, "Report created", "Selected report has been created")

    def __init__(self):
        super(CovidReport, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """
        Geting data and loading at start app
        """
        self.selected_item = None

        self.get_data()
        self.load_list()

        self.ui.countryList.itemClicked.connect(self.selected_country_values)
        self.ui.searchCountry.textChanged.connect(self.load_list)
        self.ui.updateButton.clicked.connect(self.get_data)
        self.ui.createXls.clicked.connect(self.create_xls)

        #TODO add creating visualisation
        #TODO fix data cleaning - 0 at begining at some countries

app = QtWidgets.QApplication([])
application = CovidReport()

application.show()


sys.exit(app.exec())
