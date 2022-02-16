# import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d =dict( sorted(d.items()))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)



# a={"b":"b","f":"f","a":"a","c":"c"}
# b=dict(sorted(a.items()))
# c=dict(sorted(a.items(),reverse=True))
# print(b)
# print(c)

x={"7":3,"3":2,"1":0,"5":9}
y=dict(sorted(x.items()))
z=dict(sorted(x.items(),reverse=True))
print(y)
print(z)