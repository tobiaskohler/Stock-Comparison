# Stock Price Plotting CLI

This CLI allows users to plot the daily prices of specified stocks between a specified start and end date using `yfinance` and `plotly.express`. The logarithmic scale for the y-axis and type of price to plot (e.g. 'Open', 'Close', 'High', 'Low') can also be specified.

## Usage

The main function `plot_stocks()` accepts the following arguments:

- `symbols`: List of str
  - List of symbols for stocks to plot
- `start`: str (yyyy-mm-dd)
  - Start date for the price data
- `end`: str (yyyy-mm-dd)
  - End date for the price data
- `price_type`: str (default: "Close")
  - Type of price to plot (e.g. 'Open', 'Close', 'High', 'Low')
- `log_scale`: bool (default: False)
  - Flag to indicate if y-axis should be on a logarithmic scale

The function returns a DataFrame containing the price data for the specified symbols and an error message string if an error occurs.

Utilize the inbuild help for more infos on what flag to use:

```bash
init.py -h


Plot multiple assets from Yahoo Finance

options:
  -h, --help            show this help message and exit
  -s SYMBOLS [SYMBOLS ...], --symbols SYMBOLS [SYMBOLS ...]
                        List of stock symbols to plot
  -b START, --start START
                        Start date in YYYY-MM-DD format
  -e END, --end END     End date in YYYY-MM-DD format
  -p PRICE_TYPE, --price_type PRICE_TYPE
                        Price type (Open, High, Low, Close)
  -l LOG_SCALE, --log_scale LOG_SCALE
                        Use logarithmic scale on the y-axis (True or False)
```

## Saving the Plot

After the plot is displayed, the user will be prompted to save the plot to the current directory. If the user chooses to save the plot, the plot will be saved as a .png image and .html file in a new folder called "output". The file names will include the symbols, price type, start date, end date, and log scale information.

## Examples

### 1.
Plot the "Close" prices of Apple (AAPL) and Microsoft (MSFT) between 2020-01-01 and 2020-12-31. The y-axis will be on a logarithmic scale.

```Bash
> init.py -s AAPL MSFT -b 2015-01-01 -e 2020-12-31 -l True
```

This will lead to the follwing output in the terminal:
````
                                 AAPL        MSFT
Date                                             
2020-01-02 00:00:00-05:00   73.561531  156.151932
2020-01-03 00:00:00-05:00   72.846367  154.207565
2020-01-06 00:00:00-05:00   73.426834  154.606171
2020-01-07 00:00:00-05:00   73.081490  153.196503
2020-01-08 00:00:00-05:00   74.257088  155.636673
...                               ...         ...
2020-12-23 00:00:00-05:00  129.406570  217.148041
2020-12-24 00:00:00-05:00  130.404572  218.847717
2020-12-28 00:00:00-05:00  135.068619  221.019028
2020-12-29 00:00:00-05:00  133.270187  220.223175
2020-12-30 00:00:00-05:00  132.133804  217.796463

[252 rows x 2 columns]
Save graph to the current folder? (y/n)
````


By answering with `y` the .png and .html file will get saved in subfolder `output/`. 
If output-folder does not exist, it will get created in your current working directory.

![Example 2 - Output (.png and .html available)](/AAPLMSFT_Close_2015-01-01-2020-12-31_log-True.png)

### 2.

Plot the "Open" prices of Apple (AAPL) and Microsoft (MSFT) between 2020-01-01 and 2020-12-31. The y-axis will be on linear scale.

```Bash
> init.py -s AAPL MSFT -b 2015-01-01 -e 2020-12-31 -p Open -l False
```

![Example 2 - Output (.png and .html available)](/AAPLMSFT_Open_2015-01-01-2020-12-31_log-False.png)
