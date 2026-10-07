# codealpha_stockportfolio_tracker

A simple Python-based Stock Portfolio Tracker that calculates the total investment value of selected stocks.

## Project Description

This project allows users to enter stock names and the quantity of shares they own. The program uses a predefined dictionary of stock prices and calculates the investment value for each stock and the total portfolio value.

## Features

- Predefined stock prices using a Python dictionary
- User input for stock name and quantity
- Calculates individual stock investment
- Calculates total investment value
- Handles invalid stock names
- Simple command-line interface

## Technologies Used

- Python
- Dictionary
- While Loop
- If-Else Conditions
- User Input/Output
- Basic Arithmetic

## How It Works

1. The program displays available stocks.
2. The user enters a stock name.
3. The user enters the quantity of shares.
4. The program calculates:

   `Stock Price × Quantity = Investment`

5. The investment is added to the total portfolio value.
6. The user can enter `done` to finish.
7. The total investment value is displayed.

## Example

```text
Stock Portfolio Tracker

Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN

Enter stock name: AAPL
Enter quantity: 5

Investment in AAPL = 900

Enter stock name: TSLA
Enter quantity: 2

Investment in TSLA = 500

Enter stock name: done

Total investment value = 1400
