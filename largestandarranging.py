a=[]                                        #Creating Blank List
n=int(input("Enter length of list "))       #Asking list's length
print("Enter numbers")                      #Asking Numbers
for i in range(0,n):                        #Running a loop for taking input
    number=int(input())                     #Taking input
    a.append(number)                        #Adding number to a list     


#Function to find largest number in a given list
def largest(listitems):
    return max(listitems)                   #This is to find maximum from a list
    #To find minimum "min(listname)" is used     


#Function for arranging a list inorder
def inorder(listitems):
    newlist=[]                              #Creating a newlist
    for i in range(0,len(listitems)):       #Running a loop of lists length
        newlist.append(min(listitems))      #appending minimum value in newlist
        listitems.remove(min(listitems))    #removing the minimum value from old list
    return newlist                          #returning newlist    

print("Input list items ",a)
print("Largest value is ",largest(a))
print("Arranged list is ",inorder(a))