import datetime

from polygon import RESTClient


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = "add api key"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        date = "2021-08-18"
        resp = client.historic_n___bbo_quotes_v2("ABNB", date, timestamp=1629118800000000000)

        print(f"NBBO quotes for {resp.ticker} on {date}.")

        for result in resp.results:
           
            print(f"Timestamp:{result['t']} \nBid price: {result['p']} \nBid Ask: {result['s']} \nAsk Price: {result['P']} \nAsk Size: {result['S']}")
            


if __name__ == '__main__':
    main()