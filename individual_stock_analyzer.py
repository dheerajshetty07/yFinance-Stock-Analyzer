### Interactive Application for Financial Analysis

### This script will allow users to interactively analyze stocks.

### Ensure individual_stock_analyzer.py and utils_Shetty.py are in the same directory

from utils_Shetty import download_stock_data, calculate_up_days, calculate_realized_gain_loss, calculate_moving_average, plot_stock_data
import pandas as pd
import re
import matplotlib.pyplot as plt
import os
import sys

def validate_ticker(ticker):
    """
    Validate that the ticker is a non-empty string containing only letters, numbers, and certain symbols.
    
    Parameters:
    - ticker (str): Stock ticker to validate.
    
    Returns:
    - str: Validated ticker, or None if invalid.
    """
    if not ticker:
        print("Error: Ticker cannot be empty. Please enter a valid stock ticker (e.g., 'NVDA').")
        print()
        return None
    ticker = ticker.strip().upper()
    if ticker.lower() == 'quit':
        return ticker
    if not re.match(r'^[A-Z0-9.-^]+$', ticker):
        print("Error: Ticker can only contain letters, numbers, '.', '-', or '^' (e.g., 'NVDA', 'AAPL').")
        print()
        return None
    return ticker

def validate_date(date_str):
    """
    Validate that the date string is in 'YYYY-MM-DD' format and within 2024.
    
    Parameters:
    - date_str (str): Date string to validate.
    
    Returns:
    - str: Validated date string, or None if invalid.
    """
    if not date_str:
        print("Error: Date cannot be empty. Please use 'YYYY-MM-DD' format (e.g., '2024-01-01').")
        print()
        return None
    try:
        date = pd.to_datetime(date_str, format='%Y-%m-%d')
        if date.year != 2024:
            print("Error: Date must be in 2024. Please use 'YYYY-MM-DD' format (e.g., '2024-01-01').")
            print()
            return None
        return date_str
    except ValueError:
        print("Please use 'YYYY-MM-DD' format (e.g., '2024-01-01').")
        print()
        return None

def validate_metric(metric):
    """
    Validate the selected metric.
    
    Parameters:
    - metric (str): Metric to validate.
    
    Returns:
    - str: Validated metric, or None if invalid.
    """
    if not metric:
        print("Error: Metric cannot be empty.")
        print()
        return None
    metric = metric.strip().lower()
    valid_metrics = ['up_days', 'gain_loss', 'both']
    if metric not in valid_metrics:
        print(f"Error: Invalid metric. Please choose one of: {', '.join(valid_metrics)}.")
        print()
        return None
    return metric

def validate_plot_choice(choice):
    """
    Validate the plot choice.
    
    Parameters:
    - choice (str): Plot choice to validate.
    
    Returns:
    - bool: True if plot is requested, False if not, None if invalid.
    """
    if not choice:
        print("Error: Plot choice cannot be empty. Please enter 'yes' or 'no'.")
        print()
        return None
    choice = choice.strip().lower()
    if choice not in ['yes', 'no']:
        print("Error: Please enter 'yes' or 'no'.")
        print()
        return None
    return choice == 'yes'

def main():
    # Close any existing plot windows to prevent interference
    plt.close('all')
    
    # Clear the console (may not work in RStudio, but included for completeness)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Welcome to the Stock Analyzer!")
    print("This tool lets you analyze stocks for the year 2024.")
    print("Follow the prompts to analyze a stock, or type 'quit' to exit.")
    print()
    
    while True:
        # Get and validate ticker
        ticker = validate_ticker(input("Enter stock ticker (e.g., 'NVDA', or 'quit' to exit): "))
        if ticker is None:
            continue
        if ticker.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Get and validate dates
        start_date = validate_date(input("Enter start date (YYYY-MM-DD, e.g., '2024-01-01'): "))
        if not start_date:
            continue
        end_date = validate_date(input("Enter end date (YYYY-MM-DD, e.g., '2024-12-30'): "))
        if not end_date:
            continue
        
        # Validate date range
        try:
            if pd.to_datetime(end_date) <= pd.to_datetime(start_date):
                print("Error: End date must be after start date.")
                print()
                continue
        except ValueError:
            print("Error: Invalid date range. Please use 'YYYY-MM-DD' format (e.g., '2024-01-01').")
            print()
            continue
        
        # Get and validate metric
        print("\nAvailable metrics:")
        print("- 'up_days': Number of days the stock price increased")
        print("- 'gain_loss': Percentage change in price")
        print("- 'both': Both metrics above")
        metric = validate_metric(input("Choose a metric to analyze: "))
        if not metric:
            continue
        
        # Get and validate plot choice
        plot_choice = validate_plot_choice(input("Would you like to see a plot of the stock price and 20-day moving average? (yes/no): "))
        if plot_choice is None:
            continue
        
        # Download stock data
        print(f"\nDownloading data for {ticker} from {start_date} to {end_date}...")
        sys.stdout.flush()  # Ensure the "Downloading" message is displayed immediately
        data = download_stock_data(ticker, start_date, end_date)
        if data is None:
            print()
            continue
        
        # Perform analysis
        print(f"\nAnalysis for {ticker}:")
        if metric in ['up_days', 'both']:
            up_days = calculate_up_days(data)
            if up_days is not None:
                print(f"Number of Up Days: {up_days}")
            else:
                print("Number of Up Days: Could not be calculated")
        
        if metric in ['gain_loss', 'both']:
            gain_loss = calculate_realized_gain_loss(data)
            if gain_loss is not None:
                print(f"Realized Gain/Loss: {gain_loss:.2f}%")
            else:
                print("Realized Gain/Loss: Could not be calculated")
        
        # Plot if requested
        if plot_choice:
            data_with_ma = calculate_moving_average(data, window=20)
            if data_with_ma is not None and 'Close' in data_with_ma.columns and '20_Day_MA' in data_with_ma.columns:
                plot_stock_data(data_with_ma, ticker)
                print(f"[Plot for {ticker}]")
                plt.close('all')  # Close the plot immediately to prevent interference
            else:
                print("Error: Could not generate plot due to missing or invalid data.")
        
        print("\n")  # Add extra spacing before the next prompt for clarity

if __name__ == "__main__":
    main()
