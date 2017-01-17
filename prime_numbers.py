prime_num_count = 0 #intitializing count to Zero
#prompt user for input
x = int(input("Enter Number to check: "))
def is_prime(x):
    #ensure 1 and 0 are not treated as prime numbers by returning the boolean False
    if x in (0,1):
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

print ("The Prime Numbers between 0 and "+ str(x) +" is " + str(prime_num_count))

