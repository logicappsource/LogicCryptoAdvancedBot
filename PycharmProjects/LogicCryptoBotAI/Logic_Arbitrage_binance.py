import binance
import time
api_key = asd
api_secret = fdf

client = Client(api_key, api_secret)


def run():
    # Initialize Arbitrage Binance Bot
    initialize_arb()
    # Get Binance Wallet Balance
    # Perform Arbitrage function
    # Data output (logfile) in txt file - Start of trades, times, balance,
    pass


def initialize_arb():
    list_of_symbols = ['ETHBTC']
    print("Logic Binance Arbitrage function Running")
    time.sleep(5)
    try:
        status = client.get_system_status() # uncomment - performance
        print("\nExchange Status: ", status)

        # Account Withdrawal History Info
        withdraws = client.get_withdraw_history()
        print("\nClient Withdraw History: ", withdraws)

        for symbol in list_of_symbols:
            market_depth(symbol)
    except:
        print("FAILURE INITIALIZE")


def market_depth(sym, num_entries=20):
    #Get market depth
    #Retrieve and format market depth (order book) including time-stamp
    i=0     #Used as a counter for number of entries
    print("Order Book: ", convert_time_binance(client.get_server_time()))
    depth = client.get_order_book(symbol=sym)
    print(depth)
    print(depth['asks'][0])
    ask_tot=0.0
    ask_price =[]
    ask_quantity = []
    bid_price = []
    bid_quantity = []
    bid_tot = 0.0
    place_order_ask_price = 0
    place_order_bid_price = 0
    max_order_ask = 0
    max_order_bid = 0
    print("\n", sym, "\nDepth     ASKS:\n")
    print("Price     Amount")
    for ask in depth['asks']:
        if i<num_entries:
            if float(ask[1])>float(max_order_ask):
                #Determine Price to place ask order based on highest volume
                max_order_ask=ask[1]
                place_order_ask_price=round(float(ask[0]),5)-0.0001
            #ask_list.append([ask[0], ask[1]])
            ask_price.append(float(ask[0]))
            ask_tot+=float(ask[1])
            ask_quantity.append(ask_tot)
            #print(ask)
            i+=1
    j=0     #Secondary Counter for Bids
    print("\n", sym, "\nDepth     BIDS:\n")
    print("Price     Amount")
    for bid in depth['bids']:
        if j<num_entries:
            if float(bid[1])>float(max_order_bid):
                #Determine Price to place ask order based on highest volume
                max_order_bid=bid[1]
                place_order_bid_price=round(float(bid[0]),5)+0.0001
            bid_price.append(float(bid[0]))
            bid_tot += float(bid[1])
            bid_quantity.append(bid_tot)
            #print(bid)
            j+=1
    return ask_price, ask_quantity, bid_price, bid_quantity, place_order_ask_price, place_order_bid_price
    #Plot Data

if __name__ == "__main__":
    run()