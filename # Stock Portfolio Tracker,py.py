# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300
}

# Initialize total investment
total_investment = 0

# Store details for file saving
portfolio = []

# Number of stocks to input
num_stocks = int(input("Enter number of different stocks you own: "))

# Collect stock info from user
for _ in range(num_stocks):
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {stock} shares: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value
        portfolio.append((stock, quantity, price, value))
    else:
        print(f"Warning: {stock} is not in the price list. Skipping.")

# Display the total investment
print("\nYour Stock Portfolio:")
print("{:<10} {:<10} {:<10} {:<10}".format("Stock", "Quantity", "Price", "Value"))
for stock, qty, price, val in portfolio:
    print(f"{stock:<10} {qty:<10} {price:<10} {val:<10}")
print(f"\nTotal Investment: ${total_investment}")

# Optionally save to file
save_option = input("Do you want to save the result to a file? (yes/no): ").lower()
if save_option == "yes":
    filename = "stock_portfolio.csv"
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty, price, val in portfolio:
            file.write(f"{stock},{qty},{price},{val}\n")
        file.write(f"\nTotal Investment,,,{total_investment}\n")
    print(f"Portfolio saved to '{filename}'.")