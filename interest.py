value1=int(input("principal:"))
value2=float(input("rate of interest:"))
value3=int(input("time:"))
simpleinterest=value1*value3*value2/100
amount=value1+simpleinterest
# print("principal:"+str(value1))
# print("rate of interest:"+str(value2))
# print("time:"+str(value3))
print("simpleinterest:"+str(simpleinterest))
print("amount:"+str(value1)+str(simpleinterest))
