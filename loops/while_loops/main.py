start_number = 5
countdown_values = []

while start_number >=1:
    countdown_values.append(start_number)
    start_number-=1
if start_number ==0:
    print(f"Discount countdown complete! ")
    print(countdown_values)
    