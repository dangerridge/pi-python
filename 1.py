import decimal

def pi_spigot(n):
    decimal.getcontext().prec = n + 100
    pi = decimal.Decimal(0)
    for k in range(n):
        pi += decimal.Decimal(1) / decimal.Decimal(16 ** k) * (decimal.Decimal(4) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(1)) - decimal.Decimal(2) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(4)) - decimal.Decimal(1) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(5)) - decimal.Decimal(1) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(6)))
    return str(pi)[:n+2]

n = int(input("Enter the number of digits of pi to calculate: "))
print(f"Pi with {n} digits of accuracy:\n{pi_spigot(n)}")
