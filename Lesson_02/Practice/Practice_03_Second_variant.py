# Program founds the numbers, which are divisor of our number
def multipliers(lst):
    temp_list = lst[:]
    answer = 1

    for i in temp_list:
        answer *= i
    return answer


divisor = [1]
sim_div = list()
print('Please enter your number...')
number = int(input())                                 # Input number
for index in range(2, number):                        # Cycle is iterate over all possible value for divide
    while not (number % index):                       # If number does not divide on divisor without rest, the  next value of divisor will be applicable
        number = number / index
        sim_div.append(index)                         # Simple divisor is added to list
    if number == 1:                                     # Calculation will not to continue, if the rest equal to 1
        break
print(sim_div)
for member in range(0, len(sim_div)):                 # Cycle defines all possible multipliers and they are added to list
    iteration = sim_div[:]
    a = iteration.pop(member)
    num = a
    divisor.append(a)                                 # One divisor is added to list of divisors
    divisor.append(multipliers(iteration))
    while iteration:
        divisor.append(a * iteration[0])
        num *= iteration.pop(0)                         # Divisors will have been added until list will be empty
        divisor.append(num)
print(divisor)
temporary = set(divisor)                                  # I used 'set', because it deletes all reiteration.
temporary.add(number)
divisor = list(temporary)
divisor.sort()
print(divisor)
