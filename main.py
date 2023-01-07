# This is a sample Python script.
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tradingview_ta import get_multiple_analysis, Interval
from binance.spot import Spot
# print(dir(binance))
balance = 100


# def sell(symbol):
#     ...
#
#
# def buy(symbol):
#     ...


def buy_or_sell(what, symbol, time):

    spot = Spot()
    price = float(spot.ticker_price(symbol)['price'])

    with open(f"result/{symbol}.csv", "r") as file:
        last_reader = list(csv.DictReader(file))

    if last_reader:
        last_reader = last_reader[-1]
    else:
        with open(f"result/{symbol}.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([symbol, price, what, time])
        return

    old_price = float(last_reader['price'])
    ten_minus = old_price - old_price * 0.02
    ten_plus = old_price * 0.02 + old_price
    print(f'symdol: {symbol}, price:{price}, what: {what}')
    if last_reader['event'] == what and ten_plus <= price >= ten_minus :
        with open(f"result/{symbol}.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([symbol, price, what, time])
    elif last_reader['event'] != what:
        with open(f"result/{symbol}.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([symbol, price, what, time])
        # if what == 'STRONG_SELL':
        #     ten = price * 0.03 - price
        #     print('STRONG_SELL')
        # else:
        #     print('STRONG_BUY')
        # if what == what and ten >= price:
        #     return
    # fild_name = ['symbol', "price", 'event', 'time']
    # with open(f"result/{symbol}.csv", "a") as file:
    #     writer = csv.writer(file)
    #     writer.writerow([symbol, price, what, time])
    # client = Client(Config.binance_key, Config.binance_secret_key)



def main():
    print('Start!')
    symbols = ["BINANCE:XRPUSDT", "BINANCE:BTCUSDT", "BINANCE:ETHUSDT", "BINANCE:BNBUSDT"]
    while True:

        analysis = get_multiple_analysis(screener="crypto", interval=Interval.INTERVAL_1_HOUR,
                                         symbols=symbols)

        for analys in analysis:
            symbol = analysis[analys].symbol
            summary = analysis[analys].summary

            if summary['RECOMMENDATION'] == 'STRONG_SELL' or summary['RECOMMENDATION'] == 'STRONG_BUY':
                buy_or_sell(summary['RECOMMENDATION'], symbol, Interval.INTERVAL_15_MINUTES)
    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
