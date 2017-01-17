def main():
    #initiallize fibonacci starting points to zero and one respectively
    a, b = 0, 1
    #input number
    num = int (input ("Please enter the Max number: ") )
    #num = 9
    #compare & output upper fibonacci start point if less than entred num
    while b < num:
        print (b, end='' +" ")
        #reassign a to b and b to the sum of a and b 
        a, b = b , a+b
if __name__ == "__main__":main()
