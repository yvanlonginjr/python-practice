"""
Python Core Mechanics
=====================
Five essential mechanics with annotations and mini challenges.

Mechanics covered:
  1. Loops + enumerate
  2. Dictionaries
  3. Sorting
  4. List comprehensions
  5. Strings
"""

# =============================================================================
# MECHANIC 1: LOOPS + ENUMERATE
# =============================================================================
# enumerate() gives you (index, value) pairs — avoids manual index tracking.
# Use when you need both position and value inside a loop.

prices = [101.5, 98.2, 103.7, 99.1, 105.0]

print("--- Loops + enumerate ---")
for i, price in enumerate(prices):
    print(f"Bar {i}: ${price}")

# enumerate with a start offset
for i, price in enumerate(prices, start=1):
    print(f"Candle {i}: ${price}")

# Mini challenge: print only bars where price > 100
print("\nBars above $100:")
for i, price in enumerate(prices):
    if price > 100:
        print(f"  Bar {i}: ${price}")


# =============================================================================
# MECHANIC 2: DICTIONARIES
# =============================================================================
# Dicts map keys to values. O(1) average lookup — core to most quant problems.
# Use .get() for safe access, .items() to iterate key-value pairs.

portfolio = {
    "NQ": {"qty": 2, "entry": 19800},
    "ES": {"qty": 1, "entry": 5050},
    "GC": {"qty": 3, "entry": 2350},
}

print("\n--- Dictionaries ---")
for ticker, info in portfolio.items():
    print(f"{ticker}: {info['qty']} contracts @ {info['entry']}")

# Safe access with default
pnl = {"NQ": 1500, "ES": -200}
print(f"\nNQ P&L: {pnl.get('NQ', 0)}")
print(f"GC P&L: {pnl.get('GC', 0)}")  # returns 0 if key missing

# Counting with dict (frequency map pattern)
trades = ["BUY", "SELL", "BUY", "BUY", "SELL", "BUY"]
count = {}
for t in trades:
    count[t] = count.get(t, 0) + 1
print(f"\nTrade counts: {count}")

# Mini challenge: find ticker with highest entry price
max_ticker = max(portfolio, key=lambda t: portfolio[t]["entry"])
print(f"Highest entry: {max_ticker} @ {portfolio[max_ticker]['entry']}")


# =============================================================================
# MECHANIC 3: SORTING
# =============================================================================
# sorted() returns a new list. list.sort() mutates in place.
# key= accepts any function — use lambda for quick inline keys.

print("\n--- Sorting ---")
closes = [103.2, 98.5, 101.0, 99.8, 105.3]

ascending = sorted(closes)
descending = sorted(closes, reverse=True)
print(f"Ascending:  {ascending}")
print(f"Descending: {descending}")

# Sort list of dicts by a field
signals = [
    {"ticker": "NQ", "score": 0.82},
    {"ticker": "ES", "score": 0.65},
    {"ticker": "GC", "score": 0.91},
]
ranked = sorted(signals, key=lambda s: s["score"], reverse=True)
for rank, s in enumerate(ranked, 1):
    print(f"  #{rank} {s['ticker']} — score {s['score']}")

# Mini challenge: sort tickers in portfolio by qty descending
by_qty = sorted(portfolio.items(), key=lambda x: x[1]["qty"], reverse=True)
print(f"\nBy position size: {[t for t, _ in by_qty]}")


# =============================================================================
# MECHANIC 4: LIST COMPREHENSIONS
# =============================================================================
# Compact syntax for building lists. Replaces most map/filter patterns.
# Format: [expression for item in iterable if condition]

print("\n--- List Comprehensions ---")

# Basic: square numbers 1-10
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# Filtered: only even squares
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Applied to prices: normalize to returns
returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]
print(f"Returns: {[round(r, 4) for r in returns]}")

# Nested comprehension: all (i, j) pairs where i < j
pairs = [(i, j) for i in range(4) for j in range(4) if i < j]
print(f"Pairs: {pairs}")

# Mini challenge: extract tickers with qty >= 2
heavy = [t for t, info in portfolio.items() if info["qty"] >= 2]
print(f"Positions >= 2 contracts: {heavy}")


# =============================================================================
# MECHANIC 5: STRINGS
# =============================================================================
# Strings are immutable sequences. Key methods: split, join, strip, replace,
# upper/lower, startswith/endswith, f-strings for formatting.

print("\n--- Strings ---")

ticker = "  NQ Futures  "
clean = ticker.strip()
print(f"Stripped: '{clean}'")
print(f"Upper: '{clean.upper()}'")

# split and join
csv_row = "NQ,2,19800,LONG"
parts = csv_row.split(",")
print(f"Parts: {parts}")
rejoined = " | ".join(parts)
print(f"Rejoined: {rejoined}")

# f-strings with formatting
entry = 19842.50
stop = 19750.00
risk = entry - stop
print(f"\nEntry: {entry:,.2f}")
print(f"Stop:  {stop:,.2f}")
print(f"Risk:  {risk:.2f} points")

# String checks
tags = ["LONG_NQ", "SHORT_ES", "LONG_GC", "FLAT_ZB"]
longs = [t for t in tags if t.startswith("LONG")]
print(f"\nLong positions: {longs}")

# Mini challenge: parse "TICKER_DIRECTION" into a dict
parsed = {}
for tag in tags:
    parts = tag.split("_", 1)
    parsed[parts[1]] = parts[0]
print(f"Parsed: {parsed}")
