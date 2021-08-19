from polygon import RESTClient
import json

def main():
    key = "t6HIBdnMS2XzzUDpulqlCImNyvRtCAVD"

    # Create REST client    
    with RESTClient(key) as client:
        result = client.reference_stock_financials("AAPL")
        res = json.dumps(result.__dict__)
        rez = json.loads(res)
        print(rez)
        #returns all financials for a given company

if __name__ == '__main__':
    main()
