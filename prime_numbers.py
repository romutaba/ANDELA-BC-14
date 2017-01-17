prime_num_count = 0 #intitializing to Zero
x = int(input("Enter Number to check: "))
def is_prime(x):
    if x >= 2: 
        for y in range(2,x):
            #if ( x % y )==0:
            if not ( x % y ):
                return False
    else:
        return False
    return True
for i in range(0, x):
    if is_prime(i):
        prime_num_count += 1
        print (i, end='' +" ")

print ("The Prime Numbers between 0 and "+ str(x) +" is " + str(prime_num_count))

