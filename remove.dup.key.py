# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
temp = []
res = dict()
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
  
# printing result 
print("The dictionary after values removal : " + str(res)) 