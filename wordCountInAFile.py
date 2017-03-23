word = "the a big nee kniw how are you jji nahu akjsk shuhsh a s kmjk big nee kniw a"
# x = word.split()
# print x
# count = 0
# for i in x:
#     count += 1
# print count


wordcount = {}

for x in word.split():
    if x not in wordcount:
        wordcount[x] =1
    else:
        wordcount[x]+=1
print wordcount

for k,x in wordcount.items():
    print k,x
count = 0
print wordcount.values()

for i in wordcount.values():

    count += i
print count

# numbr of distinct words
count1= 0
for i in wordcount.values():

    count1 += 1
print count1

