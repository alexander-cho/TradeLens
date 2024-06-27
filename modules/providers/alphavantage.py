import os
from dotenv import load_dotenv
import requests
import warnings

warnings.filterwarnings(action="ignore", category=FutureWarning)

load_dotenv()


class AlphaVantage:
    def __init__(self):
        self.api_key = os.getenv('ALPHAVANTAGE_API_KEY')
        self.TOP_GAINERS_LOSERS_URL = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={self.api_key}'

    def get_top_gainers_losers(self) -> dict:
        """
        Get the 20 top gainers and losers, as well as the most actively traded stocks for the day

        Returns:
            dict: with keys ['metadata', 'last_updated', 'top_gainers', 'top_losers', 'most_actively_traded']

                'top_gainers', 'top_losers', 'most_actively_trade':
                    list of dictionaries for each ticker containing the following keys
                    ['ticker', 'price', 'change_amount', 'change_percentage', 'volume']
        """
        # request = requests.get(self.TOP_GAINERS_LOSERS_URL)
        # top_gainers_losers = request.json()
        # return top_gainers_losers

        return {'metadata': 'Top gainers, losers, and most actively traded US tickers', 'last_updated': '2024-06-26 16:15:59 US/Eastern', 'top_gainers': [{'ticker': 'SBEV+', 'price': '0.0577', 'change_amount': '0.0326', 'change_percentage': '129.8805%', 'volume': '1270'}, {'ticker': 'OPTXW', 'price': '0.1468', 'change_amount': '0.0827', 'change_percentage': '129.0172%', 'volume': '320068'}, {'ticker': 'WENA', 'price': '3.62', 'change_amount': '1.97', 'change_percentage': '119.3939%', 'volume': '88972619'}, {'ticker': 'BNIXW', 'price': '0.02', 'change_amount': '0.0099', 'change_percentage': '98.0198%', 'volume': '3600'}, {'ticker': 'CLDI+', 'price': '0.0396', 'change_amount': '0.0196', 'change_percentage': '98.0%', 'volume': '1560'}, {'ticker': 'CMAXW', 'price': '0.0193', 'change_amount': '0.0093', 'change_percentage': '93.0%', 'volume': '31636'}, {'ticker': 'ESGLW', 'price': '0.0117', 'change_amount': '0.0056', 'change_percentage': '91.8033%', 'volume': '300'}, {'ticker': 'COOTW', 'price': '0.03', 'change_amount': '0.014', 'change_percentage': '87.5%', 'volume': '31370'}, {'ticker': 'TCOA+', 'price': '0.0375', 'change_amount': '0.0175', 'change_percentage': '87.5%', 'volume': '4441'}, {'ticker': 'NNAGW', 'price': '0.054', 'change_amount': '0.0243', 'change_percentage': '81.8182%', 'volume': '29371'}, {'ticker': 'CMAX', 'price': '3.41', 'change_amount': '1.51', 'change_percentage': '79.4737%', 'volume': '13627993'}, {'ticker': 'FFIE', 'price': '0.4585', 'change_amount': '0.1935', 'change_percentage': '73.0189%', 'volume': '638092483'}, {'ticker': 'NVNIW', 'price': '0.0296', 'change_amount': '0.0124', 'change_percentage': '72.093%', 'volume': '10'}, {'ticker': 'BFLY+', 'price': '0.0283', 'change_amount': '0.0113', 'change_percentage': '66.4706%', 'volume': '113690'}, {'ticker': 'LCW+', 'price': '0.16', 'change_amount': '0.0599', 'change_percentage': '59.8402%', 'volume': '485'}, {'ticker': 'EVGRW', 'price': '0.0589', 'change_amount': '0.0214', 'change_percentage': '57.0667%', 'volume': '15400'}, {'ticker': 'BNIXR', 'price': '0.14', 'change_amount': '0.0506', 'change_percentage': '56.5996%', 'volume': '2293'}, {'ticker': 'LIXTW', 'price': '0.062', 'change_amount': '0.0211', 'change_percentage': '51.5892%', 'volume': '1826'}, {'ticker': 'GOVXW', 'price': '0.0679', 'change_amount': '0.0229', 'change_percentage': '50.8889%', 'volume': '2868'}, {'ticker': 'RELIW', 'price': '0.0798', 'change_amount': '0.0267', 'change_percentage': '50.2825%', 'volume': '12010'}], 'top_losers': [{'ticker': 'SEPAW', 'price': '0.01', 'change_amount': '-0.05', 'change_percentage': '-83.3333%', 'volume': '647297'}, {'ticker': 'HUBCZ', 'price': '0.02', 'change_amount': '-0.03', 'change_percentage': '-60.0%', 'volume': '65595'}, {'ticker': 'EFTRW', 'price': '0.0012', 'change_amount': '-0.0015', 'change_percentage': '-55.5556%', 'volume': '128170'}, {'ticker': 'PTIXW', 'price': '0.0081', 'change_amount': '-0.0076', 'change_percentage': '-48.4076%', 'volume': '2800'}, {'ticker': 'FREEW', 'price': '0.0308', 'change_amount': '-0.0277', 'change_percentage': '-47.3504%', 'volume': '24118'}, {'ticker': 'NOVVR', 'price': '0.112', 'change_amount': '-0.098', 'change_percentage': '-46.6667%', 'volume': '101'}, {'ticker': 'BCDAW', 'price': '0.0127', 'change_amount': '-0.011', 'change_percentage': '-46.4135%', 'volume': '18752'}, {'ticker': 'BNZIW', 'price': '0.0155', 'change_amount': '-0.0133', 'change_percentage': '-46.1806%', 'volume': '1231'}, {'ticker': 'TCBPW', 'price': '0.0075', 'change_amount': '-0.0061', 'change_percentage': '-44.8529%', 'volume': '131'}, {'ticker': 'SRZNW', 'price': '0.0146', 'change_amount': '-0.0114', 'change_percentage': '-43.8462%', 'volume': '514'}, {'ticker': 'BROGW', 'price': '0.0029', 'change_amount': '-0.002', 'change_percentage': '-40.8163%', 'volume': '111714'}, {'ticker': 'BJDX', 'price': '1.63', 'change_amount': '-1.12', 'change_percentage': '-40.7273%', 'volume': '2316133'}, {'ticker': 'TALKW', 'price': '0.0712', 'change_amount': '-0.0488', 'change_percentage': '-40.6667%', 'volume': '142152'}, {'ticker': 'ONFOW', 'price': '0.151', 'change_amount': '-0.099', 'change_percentage': '-39.6%', 'volume': '2000'}, {'ticker': 'LFLYW', 'price': '0.0157', 'change_amount': '-0.0102', 'change_percentage': '-39.3822%', 'volume': '7017'}, {'ticker': 'GRI', 'price': '1.83', 'change_amount': '-1.14', 'change_percentage': '-38.3838%', 'volume': '736985'}, {'ticker': 'NVACR', 'price': '0.1', 'change_amount': '-0.06', 'change_percentage': '-37.5%', 'volume': '1581'}, {'ticker': 'UKOMW', 'price': '0.012', 'change_amount': '-0.0069', 'change_percentage': '-36.5079%', 'volume': '7816'}, {'ticker': 'LYEL', 'price': '1.305', 'change_amount': '-0.735', 'change_percentage': '-36.0294%', 'volume': '11844634'}, {'ticker': 'CNSP', 'price': '1.84', 'change_amount': '-1.0', 'change_percentage': '-35.2113%', 'volume': '1514923'}], 'most_actively_traded': [{'ticker': 'FFIE', 'price': '0.4585', 'change_amount': '0.1935', 'change_percentage': '73.0189%', 'volume': '638092483'}, {'ticker': 'OPTT', 'price': '0.1802', 'change_amount': '0.0459', 'change_percentage': '34.1772%', 'volume': '396353075'}, {'ticker': 'NVDA', 'price': '126.4', 'change_amount': '0.31', 'change_percentage': '0.2459%', 'volume': '351876614'}, {'ticker': 'RIVN', 'price': '14.74', 'change_amount': '2.78', 'change_percentage': '23.2441%', 'volume': '260663137'}, {'ticker': 'DNA', 'price': '0.2815', 'change_amount': '-0.0386', 'change_percentage': '-12.0587%', 'volume': '135470197'}, {'ticker': 'SQQQ', 'price': '8.18', 'change_amount': '-0.0495', 'change_percentage': '-0.6015%', 'volume': '104476253'}, {'ticker': 'TSLA', 'price': '196.37', 'change_amount': '9.02', 'change_percentage': '4.8145%', 'volume': '94787565'}, {'ticker': 'WENA', 'price': '3.62', 'change_amount': '1.97', 'change_percentage': '119.3939%', 'volume': '88972619'}, {'ticker': 'AAPL', 'price': '213.25', 'change_amount': '4.18', 'change_percentage': '1.9993%', 'volume': '64255658'}, {'ticker': 'AMZN', 'price': '193.61', 'change_amount': '7.27', 'change_percentage': '3.9015%', 'volume': '63927885'}, {'ticker': 'SIRI', 'price': '2.7', 'change_amount': '0.04', 'change_percentage': '1.5038%', 'volume': '55146078'}, {'ticker': 'CCL', 'price': '18.365', 'change_amount': '0.545', 'change_percentage': '3.0584%', 'volume': '54865100'}, {'ticker': 'TSLL', 'price': '9.06', 'change_amount': '0.79', 'change_percentage': '9.5526%', 'volume': '53288569'}, {'ticker': 'NIO', 'price': '4.64', 'change_amount': '0.27', 'change_percentage': '6.1785%', 'volume': '52919162'}, {'ticker': 'MU', 'price': '142.36', 'change_amount': '1.24', 'change_percentage': '0.8787%', 'volume': '45458412'}, {'ticker': 'BAC', 'price': '39.0', 'change_amount': '-0.38', 'change_percentage': '-0.965%', 'volume': '43242507'}, {'ticker': 'F', 'price': '12.105', 'change_amount': '0.015', 'change_percentage': '0.1241%', 'volume': '41336523'}, {'ticker': 'NVD', 'price': '2.11', 'change_amount': '0.0', 'change_percentage': '0.0%', 'volume': '40363655'}, {'ticker': 'SOXL', 'price': '54.75', 'change_amount': '-0.55', 'change_percentage': '-0.9946%', 'volume': '39733369'}, {'ticker': 'AAL', 'price': '11.12', 'change_amount': '-0.01', 'change_percentage': '-0.0898%', 'volume': '39688635'}]}
