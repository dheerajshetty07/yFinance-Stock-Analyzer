import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def download_stock_data(ticker, start_date, end_date):
    """
    Download stock data for a given ticker and date range.
    
    Parameters:
    - ticker (str): Stock ticker symbol (e.g., 'AAPL').
    - start_date (str): Start date in 'YYYY-MM-DD' format.
    - end_date (str): End date in 'YYYY-MM-DD' format.
    
    Returns:
    - pd.DataFrame: Stock data with Date as the index, or None if an error occurs.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
        if data.empty:
            raise ValueError(f"No data found for ticker: {ticker}")
        # Flatten multi-index columns if present
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[0] for col in data.columns]
        return data
    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")
        return None

def calculate_up_days(data):
    """
    Calculate the number of 'up days' (days where the closing price increased).
    
    Parameters:
    - data (pd.DataFrame): Stock data with 'Close' column.
    
    Returns:
    - int: Number of up days, or None if an error occurs.
    """
    try:
        data['Daily_Return'] = data['Close'].pct_change()
        up_days = data[data['Daily_Return'] > 0].shape[0]
        return up_days
    except KeyError:
        print("Error: 'Close' column not found in data.")
        return None

def calculate_realized_gain_loss(data):
    """
    Calculate the realized gain/loss over the period.
    
    Parameters:
    - data (pd.DataFrame): Stock data with 'Close' column.
    
    Returns:
    - float: Realized gain/loss as a percentage, or None if an error occurs.
    """
    try:
        if 'Close' not in data.columns:
            raise ValueError("'Close' column not found in data.")

        # Extract scalar values explicitly to avoid FutureWarning
        initial_price = data['Close'].iloc[0].item()
        final_price = data['Close'].dropna().iloc[-1].item()
        
        if pd.isna(initial_price) or pd.isna(final_price):
            raise ValueError("Initial or final price is NaN.")
        
        return ((final_price - initial_price) / initial_price) * 100

    except Exception as e:
        print(f"Error calculating gain/loss: {e}")
        return None

def calculate_moving_average(data, window=20):
    """
    Calculate the moving average for a given window.
    
    Parameters:
    - data (pd.DataFrame): Stock data with 'Close' column.
    - window (int): Number of days for the moving average.
    
    Returns:
    - pd.DataFrame: Data with moving average column added, or None if an error occurs.
    """
    try:
        data[f'{window}_Day_MA'] = data['Close'].rolling(window=window).mean()
        return data
    except KeyError:
        print("Error: 'Close' column not found in data.")
        return None

def plot_stock_data(data, ticker):
    """
    Plot the stock's closing price and moving average.
    
    Parameters:
    - data (pd.DataFrame): Stock data with 'Close' and moving average columns.
    - ticker (str): Stock ticker symbol.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data['Close'], label='Closing Price')
        plt.plot(data['20_Day_MA'], label='20-Day Moving Average')
        plt.title(f'{ticker} Stock Price and Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
    except KeyError:
        print("Error: Required columns ('Close' or '20_Day_MA') not found in data.")
