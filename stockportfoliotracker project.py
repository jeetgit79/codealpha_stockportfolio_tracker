stock_prices = {
    "AAPL": 180,
    "TSLA":250,
    "GOOGL":150,
    "MSFT":400,
    "AMZN":180,
}
total_investment = 0
print("stock portfolio tracker")
print("available stocks:",",".join(stock_prices.keys()))
while True:
    stock = input("enter stock name or'done' to finish):").upper()
    if stock == "done":
        break
    if stock in stock_prices:
        quantity = int(input("enter quantity:"))
        investment = stock_prices[stock]* quantity 
        total_investment += investment
        print("investment in", stock,"=",investment)
    else:
        print("stock not found!")
        print("\ntotal investment value=,total_investment")
        