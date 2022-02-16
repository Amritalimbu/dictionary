a={"a":2,"b":4}
for i,j in a.items():
    u=input("enter the key")
    if u in a.keys():
        print("yes exist")
    else:
        print("not exist")