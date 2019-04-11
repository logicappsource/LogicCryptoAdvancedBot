#import save_historical_data
import ccxt
import time
import matplotlib.pyplot as plt
import random
from pprint import pprint
#address = client.get_deposit_address(asset='BTC')


def run():
    # Initialize Function - Set Initial Conditions for Bot
    arbitrage()
    time.sleep(20)
    initialize()
    # Diversify function - collect all balances accross exchange, than  diversify them
    #diversify()
    portfolio = 10 # BTC
    # Active Trader - 'Scalping', swing trading ,arbitrage
    while 1:
        ActiveTrader()


def arbitrage(cycle_number=25, cycle_time=3):
    # Crate Triangular Function
    print("Arbitrage function Running")
    coins = ['BTC', 'LTC', 'ETH'] # Currencies to Arbitrage
    for exch in ccxt.exchanges:
        exch1 = getattr(ccxt, exch)()
        symbols = exch1.symbols
        if symbols is None:
            print("\n ----------------------------\nNext Exchange\n--------------------------")
        elif len(symbols)<15:
            print("\n-----------------------------\nNeed more Pairs (Next Exchange)\n------------------")
        else:
            print(exch1)
            exchange1_info = dir(exch1)
            print("-----------------Exchange:", exch1.id)
            #pprint(exchange1_info)
            print(exch1.symbols) # List all currencies
            time.sleep(5)

            # Find Currencies Trading pairs to Trade
            pairs = []
            for sym in symbols:
                for symbol in coins:
                    if symbol in sym:
                        pairs.append(sym)
            #print(pairs)
            # From Coin 1 to Coin 2 - ETH/BTC - Bid
            # From Coin 2 to Coin 3 - ETH/LTC - Ask
            # From Coin 3 Coin 1 - BTC/LTC - Bid
            arb_list = ['ETH/BTC'] #['ETH/BTC', 'ETH/LTC', 'BTC/LTC']
            # Find 'closed loop' of currency pairs
            j=0
            while 1:
                if j == 1:
                            final = arb_list[0][-3:] + '/' + str(arb_list[1][-3:])
                            print(final)
                            #if final in symbols:
                            arb_list.append(final)
                            break
                time.sleep(3)
                for sym in symbols:
                    if j % 2 == 0:
                        if arb_list[j][0:3] == sym[0:3]: # Comparing top pairs of currencies based on positions
                            if arb_list[j] == sym: # Comparing bottom pairs
                                pass
                            else:
                                arb_list.append(sym)
                                print(arb_list)
                                j+=1
                                break
                    if j % 2 == 1:
                        if arb_list[j][-3:] == sym[-3:]: # back po -> end
                            if arb_list[j] == sym:
                                pass
                            else:
                                arb_list.append(sym)
                                j+=1
                                break
                #time.sleep(.5)
            print('Arbitrage list = Symbols = ', arb_list)
            time.sleep(3)
            # Determine Rates for our 3 currency pairs - order book
            i=0
            list_exchange_rate_list = []
            # Create Visualization of Currency Exchange Rate Value - Over time
                 # Determine Cycle Number (When data is taken) and time when taken
            for i in range(0, cycle_number):
                exch_rate_list = []
                for sym in arb_list:
                    if sym in symbols:
                        depth = exch1.fetch_order_book(symbol=sym)
                        #pprint(depth)
                        time.sleep(3)
                        if i % 2 == 0:
                            exch_rate_list.append(depth['bids'][0][0])
                        else:
                            exch_rate_list.append(depth['asks'][0][0])
                    else:
                        exch_rate_list.append(0)
                        time.sleep(cycle_time)
                exch_rate_list.append(time.time()) # configure to human readable time format
                print(exch_rate_list)
        # Compare to determine if Arbitrage oppertunities exists
                if exch_rate_list[0] < exch_rate_list[1] / exch_rate_list[2]:
                    print("Arbitrage Possibility -- $$$$$$$$$$$")
                else:
                    print("No Arbitrage Possibility -- %%%%%%")
                    # Format data(list) into List format (List of lists)
                list_exchange_rate_list.append(exch_rate_list)

            print(list_exchange_rate_list)
            # Create lists from Lists for matplotlib format
            rateA = []
            rateB =[]
            time_list = []
            for rate in list_exchange_rate_list:
                rateA.append(rate[0])
                rateB.append(rate[1] / rate[2])
                time_list.append(rate[3])
            # Use Matplotlib to plot data
            fig, ax = plt.subplots()
            plt.plot(rateA, time_list, color='red', label='{}'.format(arb_list[0]))
            plt.plot(rateB, time_list, color='green', label='{} / {}'.format(arb_list[1], arb_list[2]))
            # Show graph - with lbls
            ax.set(xlabel='Date', ylabel='Exchange Rate', title='Exchange: {}'.format(exch)) # id ?
            plt.legend()
            plt.show()


def diversify():
    #    Diversify to do (Diversify will diversify portfolio):
                # Collect Amounts in Wallets(availible for trading)
    for exch2 in ccxt.exchanges:
        # Change to incorporate requiring API`s keys & phrases (from Python Script)
        exch = getattr(ccxt, exch2)()
        print(exch.fetchBalance())
    # Diversify into pre-described amounts
                  # 50% btc , 5% each of 8 next-top coins, 10x 1% pf micro caps
    pass


def ActiveTrader():
    # Active trader continious Loop of calling trader functions such as scalping &
            # Arbitrage function
    # Scalping Function
    # Swing Trading Function
    # Arbitrage function
    pass


def initialize():
    # Active trade - Continiuous Loop of calling trader functions such as scalping &
    # arbitrage function
    # get system status
    # Create List of Crypto Pairs to Watch
    all_symbols = []
    # list_of_symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT','BNBBTC', 'ETHBTC', 'LTCBTC']
    micro_cap_coins = ['ICXBNB', 'BRDBNB', 'NAVBNB', 'RCNBNB']
    # time_horizon = "Short"
    # Risk = "High"
    print("\n\n---------------------------------------------------------\n\n")
    print("Logic Crypto Trader Bot Python Script\nCreated 2019 - LogicAppSource")
    print("Quick 'run-through' will be performed to introduce you to the functionality")
    time.sleep(5)
    i = 0
    try:
             #Get Status of Exchange & Account
        print("\nList fo availible Exchanges for trading: \n \n")
        print("Total Number of exchanges: ", len(ccxt.exchanges))
        print("All Exhcanges ", ccxt.exchanges) # BUg web3 ? prob python -v  remove surbitcoin or theocean

             #Get Exchange Info for All Listed Exchanges
        for exchange1 in ccxt.exchanges:
            list_of_symbols = []
            if i>0:
                break # break out of the statement
            exchange = getattr(ccxt, exchange1)()
            print("\n\nExchange: ", exchange.id)
            print("\nSet Exchange Info (Limits): ", exchange.rateLimit)
            print("\nLoad Market: ", exchange.load_markets)
            symbols = exchange.symbols

            if symbols is None:
                print("\nNo Symbols Loaded\n\n")
            else:
                print("------------------\nNumber of Symbols: ", len(symbols))
                print("Exchange & Symbols :")
                print(exchange.id, "-                   ", symbols)
                print("-------------------------------------------")
                for sym in symbols:
                    list_of_symbols.append(sym)
                    all_symbols.append(sym)
                currencies = exchange.currencies
                rand_sym = random.choice(list_of_symbols)
                market_depth(rand_sym, exchange) #exchange  == CHANGE
                visualize_market_depth(sym=rand_sym, exchange=exchange)
                scalping_orders(exchange, rand_sym)
                i+=1 # break out of initialize statement
                time.sleep(4)

             # print("\nExchange Info (Limits): ", info)
        # place a test market buy order, to place an actual order use the create_order function

            # Get Info about Coins in Watch List
        # coin_prices(list_of_symbols)
        # coin_tickers(list_of_symbols)
        # for symbol in list_of_symbols:
        #    market_depth(symbol)


             # Get recent trades
        # trades = client.get_recent_trades(symbol='BNBBTC')
        # print("\nRecent Trades: ", trades)
        # print("Local Time: ", time.localtime())
        # print("Recent Trades Time: ", convert_time_binance(trades[0]['time']))

             # Get historical trades
        # try:
        # hist_trades = client.get_historical_trades(symbol='BNBBTC')
        # print("\nHistorical Trades: ", hist_trades)
        # except:
        # print('\n \n \nATTENTION: NON VALID CONNECTION WITH BINANCE \n \n \n')

             # Get aggregate trades
        # agg_trades = client.get_aggregate_trades(symbol='BNBBTC')
        # print("\nAggregate Trades: ", agg_trades)

        #Example Visualizations of Coins
        """ 
        save_historical_data.save_historic_klines_csv('BTCUSDT', "1 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_1MINUTE)
        save_historical_data.save_historic_klines_csv('ETHBTC', "6 months ago UTC", "now UTC", Client.KLINE_INTERVAL_1DAY)
        save_historical_data.save_historic_klines_csv('BRDBNB', "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_3MINUTE)
        save_historical_data.save_historic_klines_csv('BTCUSDT', "12 months ago UTC", "now UTC", Client.KLINE_INTERVAL_1WEEK)
        save_historical_data.save_historic_klines_csv('ETHUSDT', "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_15MINUTE)

        #Visualize All Micro Cap Coins for 8 hour period and 3 minute Candlestick
        for coin in micro_cap_coins:
            save_historical_data.save_historic_klines_csv(coin, "8 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_3MINUTE)
            save_historical_data.save_historic_klines_csv(coin, "24 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_15MINUTE)
            save_historical_data.save_historic_klines_csv(coin, "1 month ago UTC", "now UTC", Client.KLINE_INTERVAL_1DAY)
            """
        print("INITIALIZE SUCCESSFUL")
    except():
        print("\n \n ATTENTION: !VALID CONNECTION WITH LogicCryptoBot \n \n")
        pass

        #Account Withdrawal History Info
        #withdraws = client.get_withdraw_history()
        #print("\nClient Withdraw History: ", withdraws)

    #for coin in micro_cap_coins:
        #scalping_orders(coin, 1, 1)


def convert_time_binance(gt):
    #Converts from Binance Time Format (milliseconds) to time-struct
    #From Binance-Trader Comment Section Code
    #gt = client.get_server_time()
    print("Binance Time: ", gt)
    print(time.localtime())
    aa = str(gt)
    bb = aa.replace("{'serverTime': ","")
    aa = bb.replace("}","")
    gg=int(aa)
    ff=gg-10799260
    uu=ff/1000
    yy=int(uu)
    tt=time.localtime(yy)
    #print(tt)
    return tt


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


def scalping_orders(coin, wait=1, tot_time=1):
    #Function for placing 'scalp orders'
    #Calls on Visualizing Scalping Orders Function
    ap, aq, bp, bq, place_ask_order, place_bid_order, spread, proj_spread, max_bid, min_ask = visualize_market_depth(wait, tot_time, coin)
    print("Coin: {}\nPrice to Place Ask Order: {}\nPrice to place Bid Order: {}".format(coin, place_ask_order, place_bid_order))
    print("Spread: {} % Projected Spread {} %".format(spread, proj_spread))
    print("Max Bid: {} Min Ask: {}".format(max_bid, min_ask))
    #Place Orders based on calculated bid-ask orders if projected > 0.05% (transaction fee)
    #Documentation: http://python-binance.readthedocs.io/en/latest/account.html#orders
    """
    if proj_spread > 0.05:
        quant1=100          #Determine Code Required to calculate 'minimum' quantity
        #Place Bid Order:
        bid_order1 = client.order_limit_buy(
            symbol=coin,
            quantity=quant1,
            price=place_bid_order)
        #Place Ask Order
        ask_order1 = client.order_limit_sell(
            symbol=coin,
            quantity=quant1,
            price=place_ask_order)
    #Place second order if current spread > 0.05% (transaction fee)
    """


def visualize_market_depth(wait_time_sec='1', tot_time='1', sym='ICXBNB', precision=5):
    cycles = int(tot_time)/int(wait_time_sec)
    start_time = time.asctime()
    fig, ax = plt.subplots()
    for i in range(1,int(cycles)+1):
        ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order = market_depth(sym)

        #print(ask_price)
        plt.plot(ask_pri, ask_quan, color = 'red', label='asks-cycle: {}'.format(i))
        plt.plot(bid_pri, bid_quan, color = 'blue', label = 'bids-cycle: {}'.format(i))

        #ax.plot(depth['bids'][0], depth['bids'][1])
        max_bid = max(bid_pri)
        min_ask = min(ask_pri)
        max_quant = max(ask_quan[-1], bid_quan[-1])
        spread = round(((min_ask-max_bid)/min_ask)*100,5)   #Spread based on market
        proj_order_spread = round(((ask_order-bid_order)/ask_order)*100, precision)
        price=round(((max_bid+min_ask)/2), precision)
        plt.plot([price, price],[0, max_quant], color = 'green', label = 'Price - Cycle: {}'.format(i)) #Vertical Line for Price
        plt.plot([ask_order, ask_order],[0, max_quant], color = 'black', label = 'Ask - Cycle: {}'.format(i))
        plt.plot([bid_order, bid_order],[0, max_quant], color = 'black', label = 'Buy - Cycle: {}'.format(i))
        #plt.plot([min_ask, min_ask],[0, max_quant], color = 'grey', label = 'Min Ask - Cycle: {}'.format(i))
        #plt.plot([max_bid, max_bid],[0, max_quant], color = 'grey', label = 'Max Buy - Cycle: {}'.format(i))
        ax.annotate("Max Bid: {} \nMin Ask: {}\nSpread: {} %\nCycle: {}\nPrice: {}"
                    "\nPlace Bid: {} \nPlace Ask: {}\n Projected Spread: {} %".format(max_bid, min_ask, spread, i, price, bid_order, ask_order, proj_order_spread),
                    xy=(max_bid, ask_quan[-1]), xytext=(max_bid, ask_quan[0]))
        if i==(cycles+1):
            break
        else:
            time.sleep(int(wait_time_sec))
    #end_time = time.asctime()
    ax.set(xlabel='Price', ylabel='Quantity',
       title='Binance Order Book: {} \n {}\n Cycle Time: {} seconds - Num Cycles: {}'.format(sym, start_time, wait_time_sec, cycles))
    plt.legend()
    plt.show()
    return ask_pri, ask_quan, bid_pri, bid_quan, ask_order, bid_order, spread, proj_order_spread, max_bid, min_ask


def coin_prices(watch_list):
    #Will print to screen, prices of coins on 'watch list'
    #returns all prices
    prices = client.get_all_tickers()
    print("\nSelected (watch list) Ticker Prices: ")
    for price in prices:
        if price['symbol'] in watch_list:
            print(price)
    return prices


def coin_tickers(watch_list):
    # Prints to screen tickers for 'watch list' coins
    # Returns list of all price tickers
    tickers = client.get_orderbook_tickers()
    print("\nWatch List Order Tickers: \n")
    for tick in tickers:
        if tick['symbol'] in watch_list:
            print(tick)
    return tickers


def portfolio_management(deposit = '10000', withdraw=0, portfolio_amt = '0', portfolio_type='USDT', test_acct='True'):
    """The Portfolio Management Function will be used to track profit/loss of Portfolio in Any Particular Currency (Default: USDT)"""
    #Maintain Portfolio Statistics (Total Profit/Loss) in a file
    pass


def Bollinger_Bands():
    #This Function will calculate Bollinger Bands for Given Time Period
    #EDIT: Will use Crypto-Signal for this functionality
    #https://github.com/CryptoSignal/crypto-signal
    pass


def buy_sell_bot():
    pass


def position_sizing():
    pass


def trailing_stop_loss():
    pass


#Place Limit Order
"""
order = client.order_limit_buy(
    symbol='BNBBTC',
    quantity=100,
    price='0.00001')
order = client.order_limit_sell(
    symbol='BNBBTC',
    quantity=100,
    price='0.00001')
"""


"""
#trade aggregator (generator)
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')
# iterate over the trade iterator
for trade in agg_trades:
    pass
    #print(trade)
    # do something with the trade data
# convert the iterator to a list
# note: generators can only be iterated over once so we need to call it again
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')
agg_trade_list = list(agg_trades)
# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
#for kline in klines:
    #print(kline)
"""

#place an order on Binance
"""
order = client.create_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')
"""

if __name__ == "__main__":
    run()