prime_num_count = 0 #intitializing count to Zero
#prompt user for input
x = int(input("Enter Number to check: "))
def is_prime(x):
    #ensure Negative Numbers, 0 and 1 aren't treated as prime numbers by returning the boolean False
    if x <= 1:
        return False
    #checking for non-prime numbers between 2 and user input
    for y in range (2, x):
        if not (x % y):
            return False
    #return True if prime 
    return True
#printing prime numbers fouynd between range of zero and user input
for i in range(0, x):
    if is_prime(i):
        prime_num_count += 1
        print (i, end='' +" ")

print ("The Prime Numbers between 0 and "+ str(x) +" are " + str(prime_num_count))


"""
Asymptotic Analysis
The Big O Notation denotes the above code's Worst Case scenario as O(N). Since the 
algorithm used grows linearly in DIRECT PROPORTION to the size of input data set. 

The code first checks if the input data is more than one. If not it stops execution of
the next line and returns False. This uses constant time denoted by O(1)

If the input is greater than 1, the code checks if the number isn't divisible, this is also uses constant time O(1) 

The final command that prints out the prime numbers within the given range as provided by user input
is executed in O(N). This is a linear algorithm because each prime number in the range has to be checked
and executed.Algorithm use therefore increases proportionally to the input figure


"""
