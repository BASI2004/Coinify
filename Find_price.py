from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_stuff(start=1, end=7):

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start': start,
        'limit': end,
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'c578dcd0-d5bd-4540-9272-224416f53b31',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data["data"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


if __name__ == "__main__":
    print(get_stuff(1, 7))
    price_btc0 = str(get_stuff()[0]['quote']['USD']['price'])
    btc_price_change0 = str(get_stuff()[0]['quote']
                            ['USD']['percent_change_24h'])
    price_btc1 = str(get_stuff()[1]['quote']['USD']['price'])
    btc_price_change1 = str(get_stuff()[1]['quote']
                            ['USD']['percent_change_24h'])
    price_btc2 = str(get_stuff()[2]['quote']['USD']['price'])
    btc_price_change2 = str(get_stuff()[2]['quote']
                            ['USD']['percent_change_24h'])
    price_btc3 = str(get_stuff()[3]['quote']['USD']['price'])
    btc_price_change3 = str(get_stuff()[3]['quote']
                            ['USD']['percent_change_24h'])
    price_btc4 = str(get_stuff()[4]['quote']['USD']['price'])
    btc_price_change4 = str(get_stuff()[4]['quote']
                            ['USD']['percent_change_24h'])

    print(price_btc0, " + ", price_btc1, " + ", price_btc2,
          " + ", price_btc3, " + ", price_btc4, " + ", )
