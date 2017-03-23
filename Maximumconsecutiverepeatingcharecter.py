__author__ = '29146'
import re
word = "aaabbhhnnnnnnn"

mostrepeated = ''
count=1
precount=1
length=""
for i in range(1,len(word)):
    if word[i-1]==word[i]:
       count+=1


    else :

        count=1
if(count>precount):
    mostrepeated=word[i]

precount=count

print mostrepeated





