# calculator program
"""
print(" Hello i am your calculator"  "Tell me what do you want to do toady");
num1 = float(input("Enter the first Number"))
var1 = input("choose from +,-,*,/")
num2 = float(input("Enter the Second Number"))
if var1 == '+':
    print(num1+num2)
elif var1 == '-':
    print("sum of Two Number"+str(num1-num2))
elif var1 == '*':
    print("The Answer is "+ str(num1*num2))
elif var1 == '/':
    print("The Answer is "+ str(num1/num2))
else:
    print("did not match try again")
"""

# calculator using the function
"""
def sum (num1, num2):
   return (num1 + num2)
def sub (num1, num2):
    print(num1 - num2)

def multi (num1, num2):
    print(num1* num2)
def  div (num1, num2):
    print(num1 + num2)

print(" Hello i am your calculator"  "Tell me what do you want to do toady");
num1 = float(input("Enter the first Number"))
var1 = input("choose from +,-,*,/")
num2 = float(input("Enter the Second Number"))
if var1 == '+':
    print(sum(num1, num2))
elif var1 == '-':
    sub(num1, num2)
elif var1 == '*':
    multi(num1, num2)
elif var1 == '/':
    div(num1, num2)
else:
    print("did not match try again")
"""


# practice
"""""
i = 5
while i <= 0:
    print(i * "*")
    i = i - 1
"""

# Fibonacci series
"""var = 0
var1 = 1
print(var)
for i in range(5):
    var2 = var + var1
    print(var2)
    var = var1
    var1 = var2
    """

""""
# list function
marks = [95, 97, 98]
print(marks[0])
print(marks[-1])
print(marks[0:2])  # 2 is not included
marks.append(99)  # adding in last in list
marks.insert(0, 92)  # inserting in marks list at position 0
print(99 in marks)  # checking whether exist in list or not
print(len(marks))  # checking the length of marks
# using For loops
for score in marks:
   print(score)
# using While loops
while i < len(marks):
   print(marks[i])
   i = i+1

marks.clear()  # clear all the data of list 
"""
# [] - list, # ()- set # {} - set
"""
students = ["ram", "shyam", "kishan", "radha", "Radhika"]
for student in students:
   if student == "kishan":
      continue
   print(student)"""


# dictinory we define desirable keyword : then value

""""
marks = { "english": 95, "chemistry": 98}
print (marks["chemistry"])
marks["physics"] = 97; #entering the new valur in dictinory
print(marks)
marks["physics"] = 97;# changing the marks of physics in dictinory
"""
# pattern printing
""""
i= 0
for i in range (6):
   for j in range(5):
      if (i<=j):
         print('+')
      else:
         print(' ')
   print ('*'*i)
   i=i+1
"""




# fucntion

# type 3 types which is in-built, module,and user defined function
# module function is imported
# import math
# print(dir(math)) # this will print all the function of math module

# from math import sqrt # this will call only sqrt fucntion
# print (sqrt(4))


# user defined fucntion
# syntax - def function name( parameter)


#def print_sum(first, second = 4): #in function we can assign default statement if there is no parameter is passed
    #print(first+second)

#print_sum(1,)

# taking mutiple input using split function
""""
x= [str(x) for x in input("Enter two values: ").split()]
for i in range (len(x)):
    print(x[i]+x[2])
"""""

""""
 # print ("Hello i am your reversed list program")
A = [1,2,3,4,5,6]
start = 0
end = 5
while start < end:
    temp = A[start]   # or  A[start], A[end] = A[end], A[start] without Temp
    A[start] = A[end]
    A[end] = temp
    end -= 1
    start +=1
print("Reversed list is")
print(A)
"""

# Max and min
"""
def minmax(arr: list, n: int):
    min = arr[0]
    max = arr[0]

    # if there are only one elemet
    if n==1:
        min = arr[0]
        max = arr[0]

    # if 2 number are present
    if arr[0] > arr[1]:
        min = arr[1]
        max = arr[0]
    else:
        min = arr[0]
        max = arr[1]

    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        if a[i] < min:
            min = a[i]

    return min,max

a = [0, 1, 2, 3, 4, 5]


min, max  =minmax(a, 6)

print(" The max number is ", max)
print( "The min number is ", min)
"""






# binary search


def binarysearch(arr,n,key):
    s = 0
    e = n
    while s <= e:
        t = t+1
        mid = int((s+e)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid]> key:
            e = mid -1
        else:
            s = mid+1

    print(-1)


arr = [10,20,30,40,50,60]
n = len(arr)
print(n)
key = int(input("enter the valur that you want to find"))
binary = (binarysearch(arr,n, key))
print("number is located at", binary)

#search in sorted and rotated array by recursive binary search
"""""
def searchInRotatedArray(arr, key, left, right):
    if left>right:
        return -1
    mid = int((left+right)/2)
    if arr[mid]== key:
        return mid
    if arr[left]<= arr[mid]:
        if key>= arr[left] & key<=arr[mid]:
            return searchInRotatedArray(arr,key,left,mid-1)
        return searchInRotatedArray(arr, key, mid-1, right)
    print(mid,left,right)
    if key >= arr[mid] & key <= arr[right-1]:
        return searchInRotatedArray(arr, key,mid+1, right)
    return searchInRotatedArray(arr, key, left, mid-1)

arr = [40,50,60,10,20,30,]
right = len(arr)
left = 0
key = 10
search = searchInRotatedArray(arr,key, left, right)
print (search)
"""""


"""""
# contain duplicate and missing number
def printTwoElements(arr, size):
    for i in range(size):
        print("iternation",i)
        print(arr[i])
        print(abs(arr[i]))
        print(arr[abs(arr[i]) - 1])
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
            print("ifff conditon",arr[abs(arr[i]) - 1])
        else:
            print("The repeating element is ", abs(arr[i]))

    for i in range(size):
        if arr[i] > 0:
            print("and the missing element is ", i + 1)


# Driver program to test above function */
arr = [7, 3, 4, 5, 5, 6, 2]
n = len(arr)
printTwoElements(arr, n)


"""""
# chocolate distribution
"""""
def findMinDiff(arr,n ,m):
    arr.sort() #sort the array

    # number of student can't be more than packets
    if n < m:
        return -1

    # largest number of chocolate
    print(arr)
    min_diff = arr[n-1] - arr[0]

    print(min_diff)

    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    for i in range(len(arr) - m + 1):
        print(arr[i + m - 1] - arr[i])
        print(arr[i + m - 1])
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff


arr = [12, 4, 7, 9, 2, 23, 25, 41,
       30, 40, 28, 42, 30, 44, 48,
       43, 50]
m = 7  # Number of students
n = len(arr) # Number of packets
print("Minimum difference is", findMinDiff(arr, n, m)) # Call the Function

"""""

