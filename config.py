ALPACA_PAPER_KEY = "PKXXXX..."  # From .env, never hardcode in real push
ALPACA_PAPER_SECRET = "SKXXXX..."

# The Ghost Layer rules
STARTING_PAPER_CASH = 100000  # Alpaca paper gives $100k
MAX_DAILY_LOSS = 5000          # If equity drops $5k from open, halt
MAX_POSITIONS = 1              # Only AAPL ever
TARGET_STOCK = "AAPL"

# Termination logic (invisible)
WALLET_KILL_THRESHOLD = 95000  # If paper equity hits this, die
AUDIT_FOLDER = "audit_dead"
```
