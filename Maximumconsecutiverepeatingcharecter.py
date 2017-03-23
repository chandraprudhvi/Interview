# inp = "abracadaaaaaabra!"  # Word/sentence to be tested
#
# prevchar = ""  # Previous character
# count = 1  # Count of current character
# maxcount = 1  # Most frequent character count
# maxchar = ""  # Most frequent character
#
# for c in inp:
#
#     # If the character is equal to the previous
#     if c == prevchar:
#         count += 1
#         # If not, check if it was bigger than the previous
#     elif count > maxcount:
#
#         # Store the biggest
#         maxcount = count
#         maxchar = prevchar
#
#         # Reset the count
#         count = 1
#     else:
#         # Reset the count
#         count = 1
#
#     prevchar = c
#
# if maxchar == "":
#     print "No consecutive characters found"
# else:
#     print "Most repeated character was: '%c' (%d times)" % (maxchar, maxcount)


string = "aaaannnhhhhhiiuuuuuuuuuuugggggggggg"
#
# p = ""
# max=""
# count = 1
# maxcount = 1
#
# for c in string:
#     if c == p:
#         count+=1
#     elif count>maxcount:
#         maxcount=count
#         m = p
#         count=1
#     else:
#         count = 1
#     p =c
#
# print m ,maxcount

p=""
m=""
count = 1
max = 1

for i in string:
    if i == p:
        count+=1
    elif count > max:
        max = count
        m = p
        count = 1
    else:
        count = 1

    p=i

print m













