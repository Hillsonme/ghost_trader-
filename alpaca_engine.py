
import alpaca_trade_api as tradeapi
from config import *
import yfinance as yf  # Free fallback data

class RealExecutionEngine:
    def __init__(self):
        self.api = tradeapi.REST(
            ALPACA_PAPER_KEY, 
            ALPACA_PAPER_SECRET, 
            base_url='https://paper-api.alpaca.markets',
            api_version='v2'
        )
        # Check real paper account (this is your "wallet")
        self.account = self.api.get_account()
    
    def get_current_equity(self):
        # This is the REAL live paper balance
        return float(self.account.equity)
    
    def get_price(self, symbol=TARGET_STOCK):
        # Real-time quote from Alpaca
        barset = self.api.get_latest_bar(symbol)
        return barset.c  # Closing price
    
    def execute_order(self, qty, side):  # side: 'buy' or 'sell'
        # REAL ORDER SUBMITTED TO ALPACA PAPER MARKET
        order = self.api.submit_order(
            symbol=TARGET_STOCK,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )
        return order.id  # Proof of execution
    
    def close_all(self):
        # Emergency liquidation if Ghost Terminator triggers
        positions = self.api.list_positions()
        for pos in positions:
            if pos.symbol == TARGET_STOCK:
                self.execute_order(int(pos.qty), 'sell')
