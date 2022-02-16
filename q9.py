# Store the unique letters and their frequency of the letters from the word
#  "MISSISSIPPI" to a dictionary, were the letters are the keys and their 
#  frequencies are the values.


# word = "MISSISSIPPI"
# count = {"M":0,"I":0,"S":0,"P":0}
# for i in word:
# 	if i == "M":
# 		count['M'] = count['M']+1
# 	if i == "I":
# 		count['I'] = count['I']+1
# 	if i == "S":
# 		count['S'] = count['S']+1
# 	if i == "P":
# 		count['P'] = count['P']+1
# print (count)

word="wnneneewwuuuuuuuu"
count={"w":0,"n":0,"e":0,"u":0}
for i in word:
    if i=="w":
        count["w"]=count["w"]+1
    if i=="n":
        count["n"]=count["n"]+1
    if i=="e":
        count["e"]=count["e"]+1
    if i=="u":
        count["u"]=count["u"]+1
print(count)