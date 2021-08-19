from polygon import RESTClient


key = "add api key"
valid_symbol_list = pd.DataFrame()
count = 1
    # with RESTClient(key) as client:
exchange = ['XASE', 'XNYS', 'XNAS']
for ex in exchange:
    endpoint = """https://api.polygon.io/v3/reference/tickers?market=stocks&exchange={}&active=true&sort=ticker&order=asc&limit=1000&apiKey=DZ8JvpdnlEhPMQz0WiJC1XnzuBxucJqs""".format(ex)
    while True:
        data = _send_request(endpoint=endpoint)
        print(data['results'])

        for stocks in data['results']:

            if not 'ETF' in stocks['name']:
                print(stocks['ticker'])
                transform.insert_stock_db((stocks['ticker'], stocks['primary_exchange'], stocks['name']))
        try:
            print(data['next_url'])
            endpoint = data['next_url'] + '&apiKey={}'.format(polygon_key)
        except:
            break