import datetime
import json

from polygon import RESTClient


def main():
    key = "add api key"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        
        result = client.stocks_equities_snapshot_single_ticker("FUBO")
        
        
        day = result.ticker.day
        minute = result.ticker.min
        lastT = result.ticker.last_trade
        lastQ = result.ticker.last_quote
	
    day_json = json.dumps(day.__dict__)

    minute_json = json.dumps(minute.__dict__)

    t_json = json.dumps(lastT.__dict__)

    q_json = json.dumps(lastQ.__dict__)
    
    print(f"Snapshot data for {result.ticker.ticker}:")
    print(f"Current Day: {day_json}")
    print(f"Last Minute: {minute_json}")
    print(f"Last Trade: {t_json}")
    print(f"Last Quote: {q_json}")


if __name__ == '__main__':
    main()