f=open("text.txt","r")
# name="arun"
# password="1433"
# line=name+":"+password
# f.write(line)
# f.close()

print(f.writable())

for line in f:
    print(line,end="")