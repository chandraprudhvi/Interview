__author__ = '29146'


a= raw_input()

charc = {}


for i in a:
    if i in charc:
        charc[i]+= 1
    else:
        charc[i] = 1




if len(a) % 2 ==0:
    odd_count=0
    for i in charc.values():
       if i % 2 != 0:
           odd_count += 1
    if odd_count >= 1:
        print "Not cpalindrome"
    else:
        print "its palindrome"
else:

    odd_count = 0
    for i in charc.values():
        if i %2 !=0:
            odd_count += 1
    if odd_count > 1:
        print "Not palindrome"
    else:
        print "its palindrome"
