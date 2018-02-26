a=[]
n=int(input("Enter length of list "))
print("Enter numbers")
for i in range(0,n):
    number=int(input())
    a.append(number)
def largest(listitems):
    return max(listitems)
def inorder(listitems):
    newlist=[]
    for i in range(0,len(listitems)):
        newlist.append(min(listitems))
        listitems.remove(min(listitems))
    return newlist
print("Input list items ",a)
print("Largest value is ",largest(a))
print("Arranged list is ",inorder(a))