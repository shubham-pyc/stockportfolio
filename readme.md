# Stock Portfolio Application
This is a command-line application that calculates the value of a stock portfolio and the maximum profit that can be achieved by buying and selling a stock.

## Requirements
* Python 3
* argparse library
## Usage
The application takes the following arguments:

* -part1: A string representing a list of stocks and their quantities in the format <TICKER>:<QUANTITY>. Example: "FB:12,PLTR:5000".
* -bonus: A string representing a list of stock prices. Example: "7,1,5,3,6,4".
To run the application, open the terminal and navigate to the directory where the script is located. Then run the following command:

```shell
python app.py -part1 "FB:12,PLTR:5000" -bonus "7,1,5,3,6,4"
```


## Functions
The application has two main functions:

### calculate_portfolio_value
This function calculates the value of a stock portfolio based on the list of stocks and their quantities passed as an argument. The current price of each stock is fetched from a sample stocks.json file.

### calculate_max_profit
This function calculates the maximum profit that can be achieved by buying and selling a stock at the optimum time. The list of prices for the stock is passed as an argument. The function returns 0 if the client cannot achieve any profit.

## Output
The application returns the value of the stock portfolio and the maximum profit that can be achieved by buying and selling a stock.



