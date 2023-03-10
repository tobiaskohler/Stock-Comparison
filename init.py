import argparse
import ast
from plottingModule import plot_stocks


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Plot multiple assets from Yahoo Finance')
    parser.add_argument("-s", "--symbols", type=str, nargs='+', help="List of stock symbols to plot")
    parser.add_argument("-b", "--start", type=str, help="Start date in YYYY-MM-DD format")
    parser.add_argument("-e", "--end", type=str, help="End date in YYYY-MM-DD format")
    parser.add_argument("-p", "--price-type", type=str, default="Close", help="Price type (Open, High, Low, Close)")
    parser.add_argument('-l', '--log-scale', type=str, help='Use logarithmic scale on the y-axis (True or False)', default='False')
    parser.add_argument('-v', '--volume', type=str, help='Plot daily volume instead of price (True or False). Works with LOG_SCALE', default='False')

    args = parser.parse_args()
    log_scale = ast.literal_eval(args.log_scale)
    volume = ast.literal_eval(args.volume)
    
    plot_stocks(args.symbols, start=args.start, end=args.end, price_type=args.price_type, log_scale=log_scale, volume=volume)