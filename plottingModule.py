import yfinance as yf
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go 
import os
import sys
import traceback



def plot_stocks(symbols, start=None, end=None, price_type="Close", log_scale=False, volume=False):
    
    """
    Overview:
        Plots the stock prices or stock volumes for the specified symbols between the specified start and end dates using yfinance and Plotly.
        The log_scale flag indicates if the y-axis should be on a logarithmic scale (for price only).
        The volume flag indicates if the volume should be plotted instead of the price.
        The price_type can be specified to choose the type of price to plot (e.g. 'Open', 'Close', 'High', 'Low').
        The function also offers the option to save the plot to the current directory.
        
    Inputs:
        symbols: List of str
            List of symbols for stocks to plot
        start: str (yyyy-mm-dd)
            Start date for the price data
        end: str (yyyy-mm-dd)
            End date for the price data
        price_type: str
            Type of price to plot (e.g. 'Open', 'Close', 'High', 'Low')
        log_scale: bool
            Flag to indicate if y-axis should be on a logarithmic scale
        volume: bool
            Flag to indicate if volume should be plotted instead of price
            
    Returns:
        df: pd.DataFrame
            DataFrame containing the price or volume data for the specified symbols
        str: str
            Error message if an error occurs
    """

    try: 
        if start and end:
            stocks_data = {symbol: yf.Ticker(symbol).history(start=start, end=end) for symbol in symbols}
            
        else:
            stocks_data = {symbol: yf.Ticker(symbol).history(period='1y') for symbol in symbols}
        
        if volume:
            data = {symbol: stocks_data[symbol]["Volume"] for symbol in symbols}
            title = "Stock Volume"
            yaxis_title = "Volume"
        else:
            data = {symbol: stocks_data[symbol][price_type] for symbol in symbols}
            title=f'Comparison of {price_type} prices'
            yaxis_title = "Indexed Price"
        
        df = pd.DataFrame(data)
        
        df.dropna(inplace=True)
            
        print(df)
        
        if not volume:
            for col in df.columns:
                df[col] = df[col] / df[col].iloc[0] * 100
        
        fig = px.line(df, height=600, width=600, labels={'Date': 'Date', 'Y': 'Dollars USD'}, template="plotly_white")
        first_date = df.index[0].strftime("%Y-%m-%d")

        if not volume:
            subtitle = f'(100={first_date})'
        else:
            if start and end:
                subtitle = f'{first_date}/{end}'
            else:
                subtitle = f'1 year'
        
        fig.update_layout(title_x=0.5, hovermode="x unified")
        
        fig.update_layout(
        title=go.layout.Title(
            text=f"<b>{title}</b><br><sup>{subtitle}</sup>",
            xref="paper",
            x=0.5
        ),
            yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text=yaxis_title
                )
            )
        )
        
        if log_scale:
            fig.update_layout(yaxis_type="log")

        fig.show()
        
        save = input("Save graph to the current folder? (y/n)")

        if save.lower() == 'y':
            
            folder_name = "output"
            save_dir = os.path.isdir(folder_name)
            current_dir = os.getcwd()
            symbols_string = "".join([symbol.replace(",", "") for symbol in symbols])

            if not save_dir:
                os.makedirs(folder_name)
                
            fig.write_image(f"{current_dir}/{folder_name}/{symbols_string}_{price_type}_{start}-{end}_log-{log_scale}_vol-{volume}.png")
            fig.write_html(f"{current_dir}/{folder_name}/{symbols_string}_{price_type}_{start}-{end}_log-{log_scale}_vol-{volume}.html")
            print(f"Image saved to {current_dir}/{folder_name}.")
            
        return df
            
    except Exception as e:
        error_msg = f"Unexpected Error: {e}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        
        return error_msg

if __name__ == '__main__':
    plot_stocks(['AAPL', 'MSFT', 'AMZN'], start='2022-01-01', end='2022-12-31', log_scale=False, volume=True)
