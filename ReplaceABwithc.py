__author__ = '29146'

set = "abhiuabhuiab"


x = list(set)

y =''
c = 0
for i in range(len(x)):
    if ((x[i]=='a') and (x[i+1]=='b')):
        #print x[i] + x[i+1]
        #x[i+2]='c'
        x[i]=''
        x[i+1] ='c'
        print x
        y=''.join(x)



        c+=1
print c

print y


#for i in len(set):
