# # %%
# "hey"

ENTRY = 0
t = ENTRY

class PriceOracle():
    def __init__(self, initial):
        self.prices = [initial]
    
    def get(self, t):
        return self.prices[t]
    
    def push(self, price):
        print("price ${} -> ${}".format(self.latest(), price))
        self.prices.append(price)
    
    def latest(self):
        return self.prices[-1]


class FuturesMarket():
    def __init__(self, base_asset, price_oracle):
        self.base_asset = base_asset
        self.contracts = []
        self.price_oracle = price_oracle
    
    def open(self, margin, size):
        future = FutureContract(self, margin, size)
        self.contracts.append(future)
        return future

    def get_price(self, t):
        return self.price_oracle.get(t)
    
    # The excess contract units on one side or the other. 
    # When the skew is positive, longs outweigh shorts; 
    # when it is negative, shorts outweigh longs.
    def skew(self, t):
        return sum([ c.size(t) for c in self.contracts ], 0)
    
    # The total size of all outstanding contracts (on a given side of the market).
    def size(self, t):
        return sum([ abs(c.size(t)) for c in self.contracts ], 0)


class FutureContract():
    def __init__(self, market, margin, size):
        self.market = market
        self.initial_margin = margin
        self._size = size
    
    def margin(self, t):
        return self.initial_margin
    
    def remaining_margin(self, t):
        # TODO
        funding = 0
        return self.initial_margin + self.profit(t) + funding
    
    def leverage(self, t):
        return self.notional_value(t) / self.remaining_margin(t)

    def size(self, t):
        # position size = (margin * leverage) / base asset spot price (entry)
        # q = (m_e * lambda_e) / p_e
        # return self.initial_margin * self.initial_leverage / self.base_asset_spot_price(t)
        return self._size
    
    def position_type(self):
        return 'long' if size(0) > 0 else 'short'

    def notional_value(self, t):
        # notional value = position size * base asset spot price
        # v = qp

        # Entry notional value.
        # return self.size(t) * self.base_asset_spot_price(t)
        
        # Spot notional value.
        return self.size(t) * self.base_asset_spot_price(t)

    def base_asset_spot_price(self, t):
        return self.market.get_price(t)
    
    def profit(self, t):
        # profit = notional value - notional value (entry)
        # r = v - v_e
        return self.notional_value(t) - self.notional_value(ENTRY)
    

def debug_future(future, t):
    return """
margin: ${}
remaining margin: ${}
leverage: {}x
size: {} {}
notional value: ${}
pnl: ${}
""".format(
    future.margin(t),
    future.remaining_margin(t),
    future.leverage(t),
    future.size(t), future.market.base_asset,
    future.notional_value(t),
    future.profit(t)
)




if __name__ == '__main__':

    price_oracle = PriceOracle(200)
    market = FuturesMarket("ETH", price_oracle)
    future = market.open(50., -2.5)


    print("INITIAL VALUES")
    print("Buy a future contract with initial margin of ${} and {}x leverage, spot price is ${}".format(
        future.initial_margin,
        future.leverage(t),
        price_oracle.get(0)
    ))
    print("price: ${}".format(price_oracle.get(t)))
    print(debug_future(future, t))

    print("")
    # update_price(prices[-1] * 5/3.0)
    price_oracle.push(price_oracle.latest() / 3.0)
    print("")
    t += 1

    print("price: ${}".format(price_oracle.get(t)))
    print(debug_future(future, t))


    print("")
    print("")
    print("Market info")
    print("Size: ${}".format(market.size(t)))
    print("Skew: ${}".format(market.skew(t)))