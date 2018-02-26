

even=[]
odd=[]

#for printing all numbers from 0 to n (here n is 20)
def printall():
    print("printing numbers from 0 to n")
    for i in range(0,20):
        print(i)

#for printing all even and odd numbers from 0 to n (here n is 20)
def printingevenandodd():
    for i in range(0,20):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("Even are ",even,"\nOdd are ",odd)

#finding a number is even or odd

def finding(a):
    if a%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")

#calling the above functions
printall()
printingevenandodd()
a=int(input("Enter a number "))
finding(a)