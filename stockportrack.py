prices = {"AAPL": 150, "GOOGL": 2500, "MSFT": 300}
portfolio = {}

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not found!")

total = 0
for stock, quantity in portfolio.items():
    total += prices[stock] * quantity

print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    print(f"{stock}: {quantity} shares x ${prices[stock]} = ${prices[stock] * quantity}")
print(f"Total Investment: ${total}")

# Save to file
with open("portfolio.txt", "w") as f:
    f.write("--- Portfolio Summary ---\n")
    for stock, quantity in portfolio.items():
        f.write(f"{stock}: {quantity} shares x ${prices[stock]} = ${prices[stock] * quantity}\n")
    f.write(f"Total Investment: ${total}\n")

print("Result saved in portfolio.txt!")



