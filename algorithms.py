#gcd(m,n)=gcd(n,m mod n)
def euclide_algorithm() -> None:
    """
    Get user input for m and n and calculate the GCD using the Euclidean algorithm.
    """
    num: int = int(input("Give a number for n: "))
    num2: int = int(input("Give a number for m: "))
    while(num != 0 and num2 != 0):
        print("n is ",num)
        print("m is ",num2)
        remain=num%num2
        quotient=num/num2
        print("The remain is ",remain)
        print("The quotient is ",quotient)
        num2=num
        print("m is ",num2)
        num=remain
        print("n is ",num)
        return num2,num
    
    
def main():
    euclide_algorithm()

if __name__=="__main__":
    main()