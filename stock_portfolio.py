# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
"AAPL": 180,
"TSLA": 250,
"GOOGL": 150,
"MSFT": 420,
"AMZN": 190
}

total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker!")
print("\nAvailable stocks:")
for stock, price in stock_prices.items():
print(f"{stock}: ${price}")

while True:
stock = input("\nEnter stock name (or 'done' to finish): ").upper()

if stock == "DONE":
break

if stock not in stock_prices:
print("❌ Stock not available. Please choose from the list.")
continue

quantity = int(input(f"Enter quantity of {stock}: "))

investment = stock_prices[stock] * quantity
total_investment += investment

print(f"✅ Investment in {stock}: ${investment}")

print("\n----------------------------")
print(f"💰 Total Investment: ${total_investment}")
print("----------------------------")

# Save result to a text file
with open("portfolio_result.txt", "w") as file:
file.write("Stock Portfolio Tracker\n")
file.write("-----------------------\n")
file.write(f"Total Investment: ${total_investment}\n")

print("📄 Result saved in portfolio_result.txt")