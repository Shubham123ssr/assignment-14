#q1
'''
l1=[]
n=int(input("Enter the value of n "))
for i in range(1,n):
    l1.append(i)
    
print(l1)
'''
#q2
'''
l1=[]
n=int(input("Enter the value of n "))
for i in range(1,2*n,2):
    l1.append(i)
print(l1)
'''
#q3
'''
l1=[]
n=int(input("Enter the value of n "))
for i in range(2,2*n+2,2):
    l1.append(i)
print(l1)
'''
#q4
'''
l1=[1,2,5,3,8,0,11,7,20]
print(max(l1))
'''
#q5
'''
l1=[1,2,5,3,8,0,11,7,20]
print(min(l1))
'''
#q6
'''
l1=[1,2,3,4,5]
sum=0;
for i in l1:
    sum+=i
print(sum)
'''
#q7
'''
l1=[-3,0,-1,2,-4,6]
for i in l1:
    if i<0:
        l1.remove(i)
print(l1)
'''
#q8
'''
# initializing the list
random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}

# iterating over the list
for item in random_list:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counr
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1

# printing the frequency
print(frequency)
'''
#q9
'''
# initialize a list
my_list = [1, 2, 3, 1, 5, 4]
 
# find length of the list
list_size = len(my_list)
 
# declare for loop
for itr in range(list_size):
 
      # check the condition
    if(my_list[itr] == 1):
 
          # print the indices
        print(itr)
        
'''
#q10
'''
l1=[-3,0,-1,2,-4,6]
l1.sort()
print(l1)
'''
