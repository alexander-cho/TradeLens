import os
from dotenv import load_dotenv
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

from fredapi import Fred

load_dotenv()


class FederalReserve:
    """
    Federal Reserve API class for fetching macroeconomic data
    """
    def __init__(self):
        self.api_key = os.getenv('FRED_API_KEY')
        self.fred = Fred(api_key=self.api_key)

    def get_gdp(self) -> dict:
        """
        Get the quarterly gdp data

        Returns:
            dict: Quarterly GDP data of key value pairs of type Timestamp and float, in billions
        """
        quarterly_gdp = self.fred.get_series('GDP').to_dict()
        filtered_quarterly_gdp = {}
        # remove nan values
        for k, v in quarterly_gdp.items():
            if pd.notna(v):
                filtered_quarterly_gdp[k] = v

        return {
            'description': 'Quarterly GDP',
            'data': filtered_quarterly_gdp
        }

    def get_debt_as_pct_of_gdp(self) -> dict:
        """
        Get the total public debt as a percentage of the gross domestic product

        Returns:
            dict: response of key value pairs of Timestamp and float, expressed in percentage points
        """
        percentages = self.fred.get_series('GFDEGDQ188S').to_dict()

        return {
            'description': 'Debt as Percentage of GDP',
            'data': percentages
        }

    def get_total_debt(self) -> dict:
        """
        Get the total public debt of the US

        Returns:
            dict: response of key value pairs of Timestamp and float, expressed in billions of dollars
        """
        debt = self.fred.get_series('GFDEBTN').to_dict()

        return {
            'description': 'Total Public Debt, Quarterly',
            'data': debt
        }

    def get_interest_payments(self) -> dict:
        """
        Get the quarterly interest payments

        Returns:
            dict: quarterly interest payments of key value pairs of type Timestamp and float, in billions of dollars
        """
        interest_payments = self.fred.get_series('A091RC1Q027SBEA').to_dict()

        return {
            'description': 'Quarterly Interest Payments',
            'data': interest_payments
        }

    def get_cpi(self) -> dict:
        """
        Get the monthly YoY consumer price changes

        Returns:
            dict: Monthly CPI of key value pairs of type Timestamp and float, which represents percentage change
        """
        monthly_cpi = self.fred.get_series('CPALTT01USM659N').to_dict()

        return {
            'description': 'Monthly CPI',
            'data': monthly_cpi
        }

    def get_ppi(self) -> dict:
        """
        Get the monthly producer price index where an index of 1982 = 100 is used as a benchmark

        Returns:
            dict Monthly ppi of key value pairs of type Timestamp and float, expressed as a float
        """
        monthly_ppi = self.fred.get_series('PPIACO').to_dict()

        return {
            'description': 'Monthly ppi',
            'data': monthly_ppi
        }

    def get_pce(self) -> dict:
        """
        Get the monthly personal consumption expenditure across the US.

        Returns:
            dict: Monthly personal consumption expenditure of key value pairs of Timestamp and float, expressed in
                billions of dollars
        """
        monthly_pce = self.fred.get_series('PCE').to_dict()

        return {
            'description': 'Monthly personal consumption expenditure',
            'data': monthly_pce
        }

    def get_disposable_income(self) -> dict:
        """
        Get the monthly real disposable income per capita

        Returns:
            dict: Monthly real disposable income per capita of key value pairs of type Timestamp and float, in dollars
        """
        real_personal_disposable_income = self.fred.get_series('A229RX0').to_dict()

        return {
            'description': 'Disposable personal income',
            'data': real_personal_disposable_income
        }

    def get_unemployment_rate(self) -> dict:
        """
        Get the monthly unemployment rate

        Returns:
            dict: Monthly unemployment rate of key value pairs of type Timestamp and float, expressed as a percentage
        """
        monthly_unemployment_rate = self.fred.get_series('UNRATE').to_dict()

        return {
            'description': 'Monthly unemployment rate',
            'data': monthly_unemployment_rate
        }

    def get_payroll(self) -> dict:
        """
        Get the monthly series of nonfarm payroll employees

        Returns:
            dict: Monthly series data of nonfarm payroll of key value pairs of type Timestamp and float, expressed
                in thousands of employees
        """
        total_nonfarm_payroll = self.fred.get_series('PAYEMS').to_dict()

        return {
            'description': 'Monthly series of nonfarm payroll',
            'data': total_nonfarm_payroll
        }

    def get_interest_rates(self):
        """
        Get the monthly interest rate (Fed Funds) reading

        Returns:
            dict: Monthly interest rates of key value pairs of type Timestamp and float, expressed as a whole
                percentage
        """
        monthly_interest_rates = self.fred.get_series('FEDFUNDS').to_dict()

        return {
            'description': 'Monthly interest rates',
            'data': monthly_interest_rates
        }

    def get_10yr(self) -> dict:
        """
        Get the daily change for the 10-year treasury yield

        Returns:
            dict: Daily changes of key value pairs of type Timestamp and float, expressed as a percentage
        """
        ten_year_yield = self.fred.get_series('DGS10').to_dict()
        filtered_ten_year_yield = {}
        # remove nan values
        for k, v in ten_year_yield.items():
            if pd.notna(v):
                filtered_ten_year_yield[k] = v

        return {
            'description': 'Ten Year Yield, daily',
            'data': filtered_ten_year_yield
        }

    def get_trade_balance(self) -> dict:
        """
        Get the monthly trade balance (trade deficit) data: difference between exports and imports

        Returns:
            dict: Monthly trade deficit data of key value pairs of type Timestamp and float,
                expressed in millions of dollars
        """
        trade_balance = self.fred.get_series('BOPGSTB').to_dict()

        return {
            'description': 'Trade balance (deficit)',
            'data': trade_balance
        }

    def get_fdi(self) -> dict:
        """
        Get the quarterly new foreign direct investment in the US

        Returns:
            dict: FDI of key value pairs of type Timestamp and float, expressed in millions of dollars
        """
        fdi = self.fred.get_series('ROWFDIQ027S').to_dict()
        return {
            'description': 'foreign direct investment to the USA',
            'data': fdi
        }

    def get_ipi(self) -> dict:
        """
        Get the monthly industrial production where an index of 2017 = 100 is used as a benchmark

        Returns:
            dict Monthly ipi of key value pairs of type Timestamp and float, expressed as a float
        """
        monthly_ipi = self.fred.get_series('INDPRO').to_dict()

        return {
            'description': 'Industrial production',
            'data': monthly_ipi
        }

    def get_capacity_utilization(self) -> dict:
        """
        Get the capacity utilization as a percentage of the maximum potential output of the economy can produce
        under normal operating conditions without straining its resources

        Returns:
            dict: Return monthly capacity utilization of key value pairs of type Timestamp and float, expressed as
                a percentage
        """
        capacity_utilization = self.fred.get_series('TCU').to_dict()

        return {
            'description': 'Capacity utilization',
            'data': capacity_utilization
        }

    def get_housing_units_started(self) -> dict:
        """
        Get number of newly started to-be privately owned housing units each month (non-cumulative)

        Returns:
            dict: housing units as key value pairs of type Timestamp and float, expressed in thousands of units
        """
        units_started = self.fred.get_series('HOUST').to_dict()

        return {
            'description': 'Housing units started',
            'data': units_started
        }

    def get_median_home_sale_price(self) -> dict:
        """
        Get quarterly median home sale price

        Returns:
            dict: median home sale price of key value pairs of type Timestamp and float, expressed as units of dollars
        """
        median_sales_price = self.fred.get_series('MSPUS').to_dict()

        return {
            'description': 'Median home sale price',
            'data': median_sales_price
        }

    def get_oil_prices(self) -> dict:
        """
        Get monthly recorded oil prices

        Returns:
            dict: Monthly crude oil as key value pairs of type Timestamp and float,
                expressed in dollars per barrel
        """
        oil_prices = self.fred.get_series('MCOILWTICO').to_dict()

        return {
            'description': 'Oil prices',
            'data': oil_prices
        }

    def get_natural_gas_prices(self) -> dict:
        """
        Get monthly recorded natural gas prices

        Returns:
            dict: Monthly natural gas as key value pairs of type Timestamp and float,
                expressed in dollars per million BTU
        """
        natural_gas_prices = self.fred.get_series('MHHNGSP').to_dict()

        return {
            'description': 'Natural gas prices',
            'data': natural_gas_prices
        }

    def get_sugar_prices(self) -> dict:
        """
        Get monthly recorded global price of sugar

        Returns:
            dict:Monthly sugar prices as key value pairs of type Timestamp and float,
                expressed in US cents per pound
        """
        sugar_prices = self.fred.get_series('PSUGAUSAUSDM').to_dict()
        filtered_sugar_prices = {}
        # remove nan values
        for k, v in sugar_prices.items():
            if pd.notna(v):
                filtered_sugar_prices[k] = v

        return {
            'description': 'Global sugar prices',
            'data': filtered_sugar_prices
        }

    def get_corn_prices(self) -> dict:
        """
        Get monthly recorded global corn prices

        Returns:
            dict: Monthly corn prices as key value pairs of type Timestamp and float,
                expressed in US dollars per metric ton
        """
        corn_prices = self.fred.get_series('PMAIZMTUSDM').to_dict()
        filtered_corn_prices = {}
        # remove nan values
        for k, v in corn_prices.items():
            if pd.notna(v):
                filtered_corn_prices[k] = v

        return {
            'description': 'Global corn prices',
            'data': filtered_corn_prices
        }

    @staticmethod
    def plot_indicator(indicator: dict) -> str:
        """
        Plot the chart given selected indicator above
        """
        timestamps = list(indicator.get('data').keys())
        values = list(indicator.get('data').values())

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=timestamps,
                y=values,
                mode='lines',
                name=indicator.get('description')
            )
        )

        fig.update_layout(
            title=indicator.get('description'),
            xaxis_title='Date',
            yaxis_title='Value',
            width=1200,
            height=500,
            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10
            )
        )

        # convert plot to HTML string
        plot_html = pio.to_html(fig, full_html=False)

        return plot_html
