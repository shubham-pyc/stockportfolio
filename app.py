import json
import argparse

# Function to calculate the total value of the portfolio
def calculate_portfolio_value(portfolio, stocks_data):
    # Initialize the total value to 0
    total_value = 0

    # Iterate over each stock in the portfolio
    for stock in portfolio:
        # Extract the ticker and quantity for the current stock
        ticker = stock["ticker"]
        quantity = stock["quantity"]

        # Find the matching stock data in the stocks data feed
        matching_stocks = [s for s in stocks_data if s["ticker"] == ticker]

        # If the matching stock is found, update the total value
        if matching_stocks:
            stock_price = matching_stocks[0]["close"]
            total_value += stock_price * quantity
        # If the matching stock is not found, print an error message
        else:
            print(f"Could not find stock price for {ticker}")

    # Return the total value of the portfolio
    return total_value

def calculate_max_profit(prices):
    """
    Calculates the maximum profit that can be achieved by buying and selling a stock at the optimum time.
    """
    min_price = float('inf')  # Initialize the minimum price to infinity
    max_profit = 0  # Initialize the maximum profit to 0
    for price in prices:
        if price < min_price:
            # Update the minimum price if the current price is lower
            min_price = price
        else:
            # Update the maximum profit if the current price is higher than the minimum price
            max_profit = max(max_profit, price - min_price)
    return max_profit if max_profit > 0 else 0

def main():
    # Sample stocks data feed

    parser = argparse.ArgumentParser()
    # Add the -part1 argument to the parser
    parser.add_argument("-part1", help="Enter your portfolio as a comma-separated string of ticker:quantity pairs")
    # Add the -bonus agument to the parser
    parser.add_argument("-bonus", type=str, help="The list of prices for the stock")
    # Parse the arguments
    args = parser.parse_args()

    if args.part1:
        stocks_data = json.load(open("stocks.json"))

        # Initialize the argument parser

        # Extract the portfolio string from the arguments
        portfolio_string = args.part1
        portfolio = []

        # If the portfolio string is not empty, parse it into a list of dictionaries
        if portfolio_string:
            for stock in portfolio_string.split(","):
                ticker, quantity = stock.split(":")
                portfolio.append({"ticker": ticker, "quantity": int(quantity)})

        # Calculate the total value of the portfolio
        total_value = calculate_portfolio_value(portfolio, stocks_data)
        # Print the total value
        print(f"Total portfolio value: {total_value}")
    
    if args.bonus:
        prices = [int(price) for price in args.bonus.split(",")]

        max_profit = calculate_max_profit(prices)
        print("Maximum Profit: ",max_profit)

if __name__ == "__main__":
    main()
