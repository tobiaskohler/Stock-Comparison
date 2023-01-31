import yfinance as yf
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go 
import os
import sys
import traceback



def plot_stocks(symbols, start=None, end=None, price_type="Close", log_scale=False):
    
    """
    Overview:
        Plots the stock prices for the specified symbols between the specified start and end dates using yfinance and Plotly.
        The log_scale flag indicates if the y-axis should be on a logarithmic scale.
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
            
    Returns:
        df: pd.DataFrame
            DataFrame containing the price data for the specified symbols
        str: str
            Error message if an error occurs

    """

    try: 
        if start and end:
            stocks_data = {symbol: yf.Ticker(symbol).history(start=start, end=end)[price_type] for symbol in symbols}
            
        else:
            stocks_data = {symbol: yf.Ticker(symbol).history(period='1y')[price_type] for symbol in symbols}
        
        df = pd.DataFrame(stocks_data)
        df.dropna(inplace=True)
        print(df)
        
        for col in df.columns:
            df[col] = df[col] / df[col].iloc[0] * 100
        
        fig = px.line(df, height=600, width=600, labels={'Date': 'Date', 'Y': 'Dollars USD'}, template="plotly_white")
        
        title=f'Comparison of {price_type} prices'
        subtitle = f'(100={start})'
        
        fig.update_layout(title_x=0.5, hovermode="x unified")
        fig.update_layout(
        title=go.layout.Title(
            text=f"<b>{title}</b><br><sup>{subtitle}</sup>",
            xref="paper",
            x=0.5
        ),
            yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="Indexed Price"
                )
            )
        )
        
        if log_scale:
            fig.update_layout(yaxis_type="log", yaxis=dict(title="Indexed Price (log scale)"))


        
        fig.show()
        
        save = input("Save graph to the current folder? (y/n)")

        if save.lower() == 'y':
            
            folder_name = "output"
            save_dir = os.path.isdir(folder_name)
            current_dir = os.getcwd()
            symbols_string = "".join([symbol.replace(",", "") for symbol in symbols])

            if not save_dir:
                os.makedirs(folder_name)
                
            fig.write_image(f"{current_dir}/{folder_name}/{symbols_string}_{price_type}_{start}-{end}_log-{log_scale}.png")
            fig.write_html(f"{current_dir}/{folder_name}/{symbols_string}_{price_type}_{start}-{end}_log-{log_scale}.html")
            print(f"Image saved to {current_dir}/{folder_name}.")
            
        return df
            
    except Exception as e:
        error_msg = f"Unexpected Error: {e}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        
        return error_msg