samplelist=['aba','xuxy','abszfgcsdfegcba','1123']
count=0

if len(samplelist[0])>=2 and samplelist[0][0]==samplelist[0][-1]:
    count=count+1

if len(samplelist[1])>=2 and samplelist[1][0]==samplelist[1][-1]:
    count=count+1
if len(samplelist[2])>=2 and samplelist[2][0]==samplelist[2][-1]:
    count=count+1

if len(samplelist[3])>=2 and samplelist[3][0]==samplelist[3][-1]:
    count=count+1

print(count)

# if len(samplelist[0])==samplelist[0][1]:
#         print(samplelist[0]==samplelist[0][1])



# if len(samplelist[1])==samplelist[1][1]:
#         print(samplelist[1]==samplelist[1][-1])


# if len(samplelist[2])==samplelist[2][2]:
#         print(samplelist[2]==samplelist[2][2])


# if len(samplelist[3])==samplelist[2][1]:
#         print(samplelist[2][-1]==samplelist[2][1])



































