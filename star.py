# *****
# ****
# ***
# **
# *

# n=int(input("enter your value :"))
# m=n
# for index in range(n):
#    # print("*")
#     for index in range(m):
#           print("*",end="")
#     m-=1
#     print()




# *****
#  ****
#   ***
#    **
#     *


# n=int(input("enter your size :"))
# m=n
# s=0
# for index in range(n):
#     for space in range(s):
#         print(" ",end="")
#     for index1 in range(m):
#         print("*",end="")
#     print()
#     m-=1
#     s+=1

#     *
#    **
#   ***
#  ****
# *****



# n=int(input("enter your value: "))
# m=1
# s=n-1
# for index in range(n):
#     for space in range(s):
#      print(" ",end="")
#     for index1 in range(m):
#       print("*",end="")  
#     print()
#     m+=1
#     s-=1


#     *
#    ***
#   *****
 
n=int(input("enter your value :"))
m=n//2
if n%2==0:
   s=2
else:
   s=1
   
   
for index in range(0,n,2):
    for space in range(m):
     print(" ",end="")
    for index1 in range(s):
        print("*",end="")
    print()
    m-=1
    s+=2
    


