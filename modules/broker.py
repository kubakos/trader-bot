import modules.settings
import requests
import datetime


class Oanda(object):

    def __init__(self):
        self.base_url = modules.settings.oanda_api_url
        self.id = modules.settings.oanda_account_id
        self.token = modules.settings.my_oanda_token
        self.client = requests.Session()
        self.client.headers['Authorization'] = 'Bearer ' + self.token

    def summary(self):
        response = self.client.get(
            self.base_url + '/v3/accounts/' + self.id + '/summary')
        if response.status_code == 200:
            return response.json()['account']
        else:
            print("Couldn't get account summary!")

    def universe(self):
        universe = []
        response = self.client.get(
            self.base_url + '/v3/accounts/' + self.id + '/instruments')
        for i in response.json()['instruments']:
            universe.append(i['name'])
        if response.status_code == 200:
            return universe
        else:
            print("Couldn't get list of tradable instruments!")

    def owned_instruments(self):
        instruments = []
        account_info = self.client.get(
            self.base_url + '/v3/accounts/' + self.id)
        for i in account_info.json()['account']['positions']:
            instruments.append(i['instrument'])
        if account_info.status_code == 200:
            return instruments
        else:
            print("Couldn't get list of owned instruments!")

    def open_positions(self):
        account_info = self.client.get(
            self.base_url + '/v3/accounts/' + self.id)
        if account_info.status_code == 200:
            return account_info.json()['account']['positions']
        else:
            print("Couldn't get list of open positions!")

    def open_order(self, direction, unit, instrument, type_of_order='MARKET'):
        if unit > 0:
            if direction == 'SHORT':
                unit = -1.0 * unit
            open_order = {'order': {'type': type_of_order,
                                    'instrument': instrument, 'units': unit}}
            response = self.client.post(self.base_url + '/v3/accounts/' +
                                        self.id + '/orders', json=open_order)
            if response.status_code == 201:
                print('Open order', response.json()[
                    'lastTransactionID'], 'executed successfully at', datetime.datetime.now())
            else:
                print('Open order FAILED at', datetime.datetime.now(),
                      'with error message:', response.json()['errorMessage'] + '!')
        else:
            raise ValueError('Open order unit has to be a positive number!')

    def close_order(self, direction, unit, instrument):
        if unit > 0:
            if direction == 'LONG':
                close_order = {'longUnits': unit}
            elif direction == 'SHORT':
                close_order = {'shortUnits': unit}
            response = self.client.put(self.base_url + '/v3/accounts/' +
                                       self.id + '/positions/' + instrument + '/close', json=close_order)
            if response.status_code == 200:
                print('Close order', unit, instrument,
                      'executed successfully at', datetime.datetime.now())
            else:
                print('Close order FAILED at', datetime.datetime.now(),
                      'with error message:', response.json()['errorMessage'] + '!')
        else:
            raise ValueError('Close order unit has to be a positive number!')

    def candlestick_data(self, days_since, granularity, instrument):
        date = datetime.date.today() - datetime.timedelta(days=days_since)
        parameters = {'from': date, 'granularity': granularity, 'price': 'BAM'}
        response = self.client.get(self.base_url + '/v3/instruments/' +
                                   instrument + '/candles', params=parameters)
        if response.status_code == 200:
            return response.json()['candles']
        else:
            print("Couldn't fetch candlestick data!",
                  response.json()['errorMessage'])

    def set_leverage(self, lev):
        if 0 < lev <= 1:
            set_lev = {'marginRate': lev}
            response = self.client.patch(self.base_url + '/v3/accounts/' +
                                         self.id + '/configuration', json=set_lev)
            if response.status_code == 200:
                print('Leverage set to', str(lev) + '!')
            else:
                print("Couldn't set leverage!",
                      response.json()['errorMessage'])
        else:
            raise ValueError('Leverage has to be between 0 and 1!')
