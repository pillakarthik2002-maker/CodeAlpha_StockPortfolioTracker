# Stock Portfolio Tracker
stock_prices = {
    "APPLES": 180,
    "BANANA": 250,
    "ORANGE": 140,
    "GRAPES": 300,
    "MANGO": 150
}

total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Added {stock_name} - Investment: ${investment}")
    else:
        print("Stock not available!")

print("\n💰 Total Investment Value: $", total_investment)

# Optional: Save result to file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_investment}")
    print("Result saved to portfolio.txt")
