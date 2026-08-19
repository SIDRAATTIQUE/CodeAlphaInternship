import csv

def stock_tracker():
    # Hardcoded dictionary for stock prices
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "MSFT": 400.0,
        "GOOGL": 140.0,
        "AMZN": 175.0
    }

    portfolio = {}
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    while True:
        symbol = input("\nEnter stock symbol (or 'done' to calculate total): ").upper().strip()
        if symbol == "DONE":
            break
        
        if symbol not in stock_prices:
            print("Stock symbol not found in predefined list. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Invalid input! Please enter a valid integer for quantity.")

    # Calculate Total Value
    total_value = 0.0
    print("\n--- Portfolio Summary ---")
    summary_lines = []
    
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        value = price * qty
        total_value += value
        line = f"{symbol}: {qty} shares @ ${price:.2f} each = ${value:.2f}"
        summary_lines.append(line)
        print(line)

    print(f"\nTotal Investment Value: ${total_value:.2f}")

    # Optional File Handling: Save results
    save = input("\nWould you like to save the results to a file? (txt/csv/no): ").lower().strip()
    if save == 'txt':
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("========================\n")
            for line in summary_lines:
                f.write(line + "\n")
            f.write(f"\nTotal Investment Value: ${total_value:.2f}\n")
        print("Saved to portfolio_summary.txt!")
    elif save == 'csv':
        with open("portfolio_summary.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price_Per_Share", "Total_Value"])
            for symbol, qty in portfolio.items():
                price = stock_prices[symbol]
                writer.writerow([symbol, qty, price, price * qty])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_value])
        print("Saved to portfolio_summary.csv!")

if __name__ == "__main__":
    stock_tracker()