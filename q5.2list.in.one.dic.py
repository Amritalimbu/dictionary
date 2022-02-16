# Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements of the 2nd list are the corresponding values.

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,8]
a=zip(list1,list2)
b=dict(a)
print(b)

a="manpreet","dipali","sawati"
b=100,101,102
c=dict(zip(a,b))

print(c)




# keys_list = ["a", "b"]
# values_list = [1, 2]
# zip_iterator = zip(keys_list, values_list)
# # Get pairs of elements

# a_dictionary = dict(zip_iterator)
# # Convert to dictionary

# print(a_dictionary)