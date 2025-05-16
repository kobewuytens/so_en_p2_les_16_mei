for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

for j in range(2, 101):
    is_prime = True
    for k in range(2, int(j**0.5) + 1):
        if j % k == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{j} is een priemgetal.")
    else:
        print(f"{j} is geen priemgetal.")