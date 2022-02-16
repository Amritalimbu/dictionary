# Count the total number of items from the values of the dictionary which are in 
# the form of a list.

# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.



  
    # defining the dictionary
# d = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     'B' : 34,
#     'C' : 12,
#     'D' : [7, 8, 9, 6, 4] }
  
#     # using dict.items()
# count = 0
# for key, value in d.items():
#     if isinstance(value,list):
#         count = count+len(value)
#         print(count)

dict = {
   'Alex': ['subj1', 'subj2', 'subj3'],
   'David': ['subj1', 'subj2'],
   "shdh":["das","e23re"]
}
ctr = sum(map(len, dict.values()))
print(ctr)
