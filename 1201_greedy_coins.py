def coins(denominations: list, amount: int) -> dict:
    detail = {}
    for di in denominations:
        if di <= amount:
            detail[di] = amount // di
            amount = amount % di

    return detail


denominations = [50, 20, 10, 5, 1]
print("40:", coins(denominations, 40))
print("87:", coins(denominations, 87))

denominations = [50, 25, 20, 10, 5, 1]
print("40:", coins(denominations, 40))
print("87:", coins(denominations, 87))

# test
