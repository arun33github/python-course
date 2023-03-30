# i=10
# while i>0:
#     print(i)
#     i=i-1 


input_list=["123","1451","ab","aba","xyx"]
sample=len(input_list)
# print(input_list)
i=0
count=0

while i<sample:
    
    if len(input_list[i])>=2 and input_list[i][-1]==input_list[i][0]:
        
        count+=1
    i=i+1         
print(count)
  