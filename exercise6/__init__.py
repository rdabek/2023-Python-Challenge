from exercise6.currency import ccy

eur = ccy(14)
usd = ccy(23, "USD")

print("First EUR:")
sum1 = eur + usd
print(sum1.currency)
print(sum1.value)

print("Second USD:")
sum2 = usd + eur
print(sum2.currency)
print(sum2.value)