
#Add two lists
list2 = [1,2,3,4,5,6]
list1 = [1,2,3,4,5,6]

for i in range(len(list2)):
    list2[i] = list2[i]+ list1[i]

print list2

#multiply two lists

list2 = [1,2,3,4,5,6]
list1 = [1,2,3,4,5,6]

for i in range(len(list2)):
    list2[i] = list2[i] * list1[i]

print list2

# Print index and value while reading a list

list2 = [0,1,2,3,4,5,6]
i = 0
while i <len(list2):
    print i, list2[i]
    i+= 1

# read list from the last element and print with index

list2 = [0,1,2,3,4,5,6]

i = len(list2)-1

while i >=0:
    print i ,list2[i]
    i-=1


# use zip to add list

list2 = [1,2,3,4,5,6]
list1 = [1,2,3,4,5,6]

print [sum(x) for x in zip(list2,list1)]

# find the highest occurence of concequetive charecter in a string

a = "aaaaabbbbbccccccccccccccccccdddddd"

p = ""
m = ""
count = 1
maxcount = 1

for c in a:
    if c == p:
        count+=1
    elif count>maxcount:
        maxcount = count
        m = p
        count =1
    else:
        count = 1
    p =c
print m


# If string is a palindrome or not

string = "abbaa"

#print a

l = list(string)


s = len(l)-1
e = 0

while s>e:
    c =l[e]
    l[e] = l[s]
    l[s] = c
    s-= 1
    e+=1

if(string == ''.join(l)):
    print "true"
else:
    print "false "


# remove duplicates

a = "abchdaaahhhjjiiiiioooo"

tes =[]

x = list(a)
for i in range(len(x)-1):
    if x[i] in tes:
        x[i] =''
    else:
        tes.append(x[i])
print ''.join(tes)







