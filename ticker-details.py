from polygon import RESTClient
import json


def main():
    key = "t6HIBdnMS2XzzUDpulqlCImNyvRtCAVD"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        
        resp = client.reference_ticker_details_vx("BABA")
        results = json.dumps(resp.__dict__)
        rezzults = json.loads(results)
        rez = rezzults['results']

        print(f"Company: {rez['name']}\nTicker: {rez['ticker']}\nOutstanding Shares: {rez['outstanding_shares']}\nMarket Cap: {rez['market_cap']}")
       


if __name__ == '__main__':
    main()
