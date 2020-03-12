def build_image(Num):

    listing = [i for i in range(3,Num+2, 2)]
    listing.insert(0, 1)
    max_value = max(listing)
    function = lambda item, MAX: (MAX-item)/2
    output = [(int(function(j, max_value)), j,  int(function(j, max_value))) for j in listing]
    print(output)
    result = ''.join(' ' * item[0] + '*' * item[1]+' ' * item[2] + '\n' for item in output)
    print(result[:-1])
    revers_listing = output[::-1]
    revers_result = ''.join(' ' * item[0] + '*' *item[1] + ' ' * item[2] + '\n' for item in revers_listing[1:])
    print(revers_result)



print('Please enter the number. It should be more as zero and odd')

Number = int(input())

if Number > 0 and Number % 2:
    result = build_image(Number)
elif Number == 1:
    print('*')
else:
    print('Wrong number, it should not divide to 2 and it does not be low as 0')
