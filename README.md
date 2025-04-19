# yFinance-Stock-Analyzer Financial Analysis with Python

## Project Overview

The Stock Analyzer is an interactive Python application designed to perform financial analysis on stock market data for the year 2024. Leveraging the yfinance package, this project analyzes stock performance metrics such as up days, realized gain/loss, and 20-day moving averages for user-selected stocks. The application emphasizes code reusability, robust error handling, and professional visualizations using matplotlib.

This project was developed to scale financial analysis with clean, containerized functions and an interactive user interface. It includes a comparative analysis of NVIDIA (NVDA) and Apple (AAPL) stocks, showcasing their performance in 2024.


## Features

**Interactive Analysis**: Users can input a stock ticker, date range (within 2024), and choose metrics (up days, realized gain/loss, or both) to analyze.

**Dynamic Visualizations**: Generates plots of closing prices and 20-day moving averages, with an optional bar chart comparing realized gain/loss across stocks.

**Reusable Functions**: Modular functions in utils_Shetty.py handle data downloading, metric calculations, and plotting, ensuring scalability.

**Robust Error Handling**: Validates user inputs (tickers, dates, metrics) with clear error messages to prevent crashes.

**Professional Reporting**: A Quarto-rendered PDF report (financial_analysis.pdf) presents the analysis of NVDA and AAPL with insights and visualizations.


## Key Insights:

NVDA achieved a 185.44% realized gain with 140 up days, reflecting strong growth in AI and semiconductor markets.

AAPL recorded a 35.85% gain with 142 up days, indicating stability and consistent performance.



## Technologies Used

- Python: Core programming language.
- yfinance: For downloading stock data.
- pandas: For data manipulation and analysis.
- matplotlib: For creating visualizations.
- Quarto: For rendering professional reports.
- Regular Expressions (re): For input validation.
- OS & sys: For console management.

```
stock-analyzer/
├── utils_Shetty.py              # Reusable functions for data downloading, analysis, and plotting
├── individual_stock_analyzer.py # Interactive script for user-driven analysis
├── financial_analysis.qmd       # Quarto file for the NVDA/AAPL analysis report
├── financial_analysis.pdf       # Rendered PDF report
└── README.md                    # Project documentation
```

## Installation & Setup

1. Clone the Repository:

git clone https://github.com/dheerajshetty07/yFinance-Stock-Analyzer.git
cd yFinance-Stock-Analyzer

2. Install Dependencies: Ensure Python 3.8+ is installed, then install the required packages:
pip install yfinance pandas matplotlib

3. Run the Interactive Analyzer:
python individual_stock_analyzer.py

Follow the prompts to input a stock ticker, date range, metric, and plot choice.

View the Report: Open financial_analysis.pdf to explore the NVDA and AAPL analysis, or render financial_analysis.qmd using Quarto.


## Usage

Interactive Mode:

Run individual_stock_analyzer.py and enter a stock ticker (e.g., NVDA), date range (e.g., 2024-01-01 to 2024-12-31), metric (up_days, gain_loss, or both), and whether to display a plot (yes or no).

Type quit to exit.


## Key Achievements

- **Scalability**: Modular functions in utils_Shetty.py are reusable for any stock and date range within 2024.

- **Error Handling**: Comprehensive validation prevents crashes from invalid inputs (e.g., incorrect tickers or date formats).

- **Professional Output**: The Quarto-rendered report is formatted for non-technical audiences, with clear visualizations and insights.

- **Interactive Design:** The individual_stock_analyzer.py script allows dynamic user input, making the tool accessible and flexible.


## Future Enhancements

Add support for multiple simultaneous stock comparisons.

Integrate additional metrics, such as volatility or relative strength index (RSI).

Enhance visualizations with interactive dashboards using Plotly or Dash.

Expand date range flexibility beyond 2024.


## Contact

For inquiries, please reach out via dheerajshetty07@gmail.com or connect on https://www.linkedin.com/in/dheerajshetty-analytics/
