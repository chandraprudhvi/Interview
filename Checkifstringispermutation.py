__author__ = '29146'

def ifpermutation():
    string1 = raw_input()
    string2 = raw_input()
    exists ="false"
    if(len(string1) == len(string2)):
        for x in string1:
            print x
            if x in string2:
                exists ="true"
            else:
                exists = "false"

    if exists == "true":
        print "permutation possible"
    else:
        print "permutation notpossible"

#ifpermutation()


a = [1,2,3,4,5,6,7,7,8,8,8,8,8,8]

b =  set(a)


m = {2,3,4,5,6,7,8}

print type(m)



print b
print type(b)