listing = [i for i in range(1000)]
simple_number = []
for Number in listing:
    if Number < 2:
        pass
    elif Number == 2:
        simple_number.append(Number)
    else:
        indicator = 0
        for i in range(2, Number + 1):
            if Number % i == 0 and i != Number:
                break
            elif Number % i == 0 and i == Number:
                indicator = 1
        if indicator == 0:
            pass
        elif indicator == 1:
            simple_number.append(Number)
print(simple_number)

