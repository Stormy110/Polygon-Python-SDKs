import datetime

from polygon import RESTClient


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = "add api key"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        
        resp = client.stocks_equities_snapshot_all_tickers()
        
        print(f"Snapshot data for entire market:")

        for result in resp.tickers:
            # dtQuote = ts_to_datetime(result["lastQuote"]["t"])
            # dtTrade = ts_to_datetime(result["lastTrade"]["t"])
            

            # print(f"Day:\n\tO: {result.day['o']}\n\tH: {result.day['h']}\n\tL: {result.day['l']}\n\tC: {result.day['c']}\n\tV: {result.day['v']}\n\tVW: {result.day['av']}\n"
            
            # f"Min:\n\tO: {result.min['o']}\n\tH: {result.min['h']}\n\tL: {result.min['l']}\n\tC: {result.min['c']}V: {result.min['v']}\n\tVW: {result.min['av']}\n"
            
            # f"Last Quote:\n\tAsk Price: {result.last_quote['P']}\n\tBid Price: {result.last_trade['p']}\n"
            
            # f"Last Trade:\n\tPrice: {result.last_trade['p']}\n\tSize: {result.last_trade['s']}\n\tConditions: {result.last_trade['c']}\n")
            
            print(result)

if __name__ == '__main__':
    main()
