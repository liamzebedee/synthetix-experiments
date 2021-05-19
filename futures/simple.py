# # %%
# "hey"

ENTRY = 0

# class FuturesMarket():
#     def __init__(self, base_asset):

#     def get_price(self, t):
#         return p

class FutureContract():
    def __init__(self, margin, size, base_asset):
        self.initial_margin = margin

        self.base_asset = base_asset
        self._size = size
        # self.size = self._size(ENTRY)
    
    @staticmethod
    def open(margin, size, base_asset):
        return FutureContract(margin, size, base_asset)
    
    def margin(self, t):
        return self.initial_margin
        # if t == ENTRY:
        #     return self.initial_margin
        # else:
        #     # remaining margin
        #     return self.notional_value(ENTRY) / self.leverage(ENTRY)
    
    def remaining_margin(self, t):
        # TODO
        funding = 0
        return self.initial_margin + self.profit(t) + funding
    
    def leverage(self, t):
        return self.notional_value(t) / self.remaining_margin(t)

    def size(self, t):
        return self._size
    # def size(self, t):
    #     return self.initial_margin * self.initial_leverage / self.base_asset_spot_price(t)
    
    def position_type(self):
        return 'long' if size(0) > 0 else 'short'

    def notional_value(self, t):
        # Entry notional value.
        # return self.size(t) * self.base_asset_spot_price(t)
        
        # Spot notional value.
        return self.size(t) * self.base_asset_spot_price(t)

    def base_asset_spot_price(self, t):
        return prices[t]
    
    def profit(self, t):
        return self.notional_value(t) - self.notional_value(ENTRY)



# Margin is 20% of spot price ($100).
# Leverage is 5x.
prices = [2000]
t = ENTRY

def update_price(price):
    print("price ${} -> ${}".format(prices[-1], price))
    prices.append(price)

future = FutureContract.open(50., -2.5, 'ETH')


print("INITIAL VALUES")
print("Buy a future contract with initial margin of ${} and {}x leverage, spot price is ${}".format(
    future.initial_margin,
    future.leverage(t),
    prices[0]
))
print("price: ${}".format(prices[t]))
print("margin: ${}".format(future.margin(t)))
print("remaining margin: ${}".format(future.remaining_margin(t)))
print("leverage: {}x".format(future.leverage(t)))
print("size: {} {}".format(future.size(t), future.base_asset))
print("notional value: ${}".format(future.notional_value(t)))
print("pnl: ${}".format(future.profit(t)))

print("")
# update_price(prices[-1] * 5/3.0)
update_price(prices[-1] / 3.0)
print("")
t += 1

print("price: ${}".format(prices[t]))
print("margin: ${}".format(future.margin(t)))
print("remaining margin: ${}".format(future.remaining_margin(t)))
print("leverage: {}x".format(future.leverage(t)))
print("size: {} {}".format(future.size(t), future.base_asset))
print("notional value: ${}".format(future.notional_value(t)))
print("pnl: ${}".format(future.profit(t)))


# print('leverage (technical): ${}'.format(
#     future.notional_value(t) / future.margin(t)
# ))


# print("pnl: ${}".format(future.profit(t)))

# print("")
# print("T+1 VALUES")
# t = 1
# print("price: ${}".format(prices[t]))
# print("margin: ${}".format(future.margin(t)))
# print("leverage: {}x".format(future.leverage(t)))
# print("notional value: ${}".format(future.notional_value(t)))
# print("size: ${}".format(future.size(t)))
# print("pnl: ${}".format(future.profit(t)))


# profit = notional value - notional value (entry)
# r = v - v_e

# notional value = position size * base asset spot price
# v = qp

# position size = (margin * leverage) / base asset spot price (entry)
# q = (m_e * lambda_e) / p_e



# p_e = base_asset_spot_price_entry = 100

# m_e = margin = 10
# lambda_e = leverage =  

# %%
