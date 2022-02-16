# dict1={1:10,2:20}
# dict2={3:30,2:40}
# dict3={5:50,6:60}




dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={7:43,8:70}
dic1.update(dic2)
dic1.update(dic3)
dic1.update(dic4)
print(dic1)


dic1={1:10, 2:20}
dic2={3:30, 2:40}
dic3={5:50,6:60}
dic4 = {}
for i in (dic1, dic2, dic3): dic4.update(i)
print(dic4)