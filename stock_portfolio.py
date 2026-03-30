#codealpha_stockportfolio_tracker

prices = {
      "AAPL": 180 ,
      "TSLA": 250 ,
     "GOOGL": 140 ,
      "MSFT": 415 ,
      "NVDA": 875 ,
}

print("-------Stock Portfolio Tracker-------")
print("Stocks:",", ".join(prices.keys()))
print()

total = 0

while True:
    symbol = input("Enter stock (or 'done'): ").upper()

    if symbol == "DONE" :
        break

    if symbol not in prices :
        print("Stock not found.Try Again!")
        continue

    qty = int(input(f"Quantity of {symbol}: "))
    value = prices[symbol] * qty
    total += value 
    print(f" {symbol} X {qty} = ${value}\n")

print(f"\nTotal Investment: ${total}")