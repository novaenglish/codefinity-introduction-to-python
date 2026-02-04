prices = [29.99, 45.50, 12.75, 38.20]
discount=[.1,.20,.15,.05]


for index in range(len(prices)):
    if index ==0:
        prices[index]-=prices[index]*discount[index]
        print(f"Updated price for item {index+1}: $ {prices[index]:.2f} ")
        
    elif index==1:
        prices[index]-=prices[index]*discount[index]
        print(f"Updated price for item {index+1}: $ {prices[index]:.2f}")
    elif index==2:
        prices[index]-=prices[index]*discount[index]
        print(f"Updated price for item {index+1}: $ {prices[index]:.2f}")
    else:
        prices[index]-=prices[index]*discount[index]
        print(f"Updated price for item {index+1}: $ {prices[index]:.2f}")
    
        