dict1={"name":"raju","marks":56}
i=0
while i<len(dict1):
    u=input("enter the key :")
    if u in dict1:
        print("exits")
    else:
        print("not exit")
        break
    i=i+1