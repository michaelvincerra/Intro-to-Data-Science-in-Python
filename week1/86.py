# create an empty list over which iteration occurs.

my_list1 = []

for number in range(0,1000):
    # NOTE !!!: '%' is the MODULUS or DIVIDE BY FUNCTION
    # For ODD Numbers, change 2 to 1 below.
    if number % 2 == 1:
        #append function here basically appends numbers from 2 to 1000 stepping by 2. Even numbers
        my_list1.append(number)


# THIS IS A 'LIST COMPREHENSION', WHICH SOLVES SAME PROB AS ABOVE BUT MUCH MORE COMPACT
# NOTE: USE OF "NUMBER" IN FORMULA IS ONLY A PLACEHOLDER!!!

my_list2 = [number for number in range(0,1000) if number % 2 == 0]


print my_list1
print my_list2