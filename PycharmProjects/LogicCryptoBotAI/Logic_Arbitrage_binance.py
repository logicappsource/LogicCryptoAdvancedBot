import binance
import time
api_key = asd
api_secret = fdf

client = Client(api_key, api_secret)


def run():
    # Initialize Arbitrage Binance Bot

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


if __name__ == "__main__":
    run()