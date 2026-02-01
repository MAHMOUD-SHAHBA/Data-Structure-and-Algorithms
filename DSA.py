# Data Structure and Algorithms
# :: 1 :: Time Complexity and Space Complexity
n = 10
count = 0
for i in range(n):
    print(i)
    count += 1 # O(n)

# ------------------------
k = 10
count = 0
for i in range(k):
    for j in range(k):
        print( i , " |" , j )
        count += 1
    print()
print("Loop Ended") # O(n)*O(n)  = O(n**2)
# -----------------------------------------
# Check if sum of a and b equal to c
def check(a,b,c):
    for i in range(b):
        for j in range(b):
            if i != j and a[i] + a[j] == c:
                return True
            
    return False
a = [1,2,3,4,5]
c = 0
b = len(a)
if check(a,b,c) :
    print("True")
else:
    print("False")  # O(n**2)
#------------------------------------------
count = 0
i = n
while i > 0 :
    for j in range(i):
        print(i)
        count += 1
        i /= 2
       