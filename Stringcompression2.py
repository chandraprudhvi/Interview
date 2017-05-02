__author__ = '29146'
def string_compression(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, ''.join(compressed), key=len)



print string_compression("aabbcc")


def compress(s):
    res = ""

    count = 1

    # Add in first character
    res += s[0]

    # Iterate through loop, skipping last one
    for i in range(len(s) - 1):
        if (s[i] == s[i + 1]):
            count += 1
        else:
            if (count > 1):
                # Ignore if no repeats
                res += str(count)
            res += s[i + 1]
            count = 1
    # print last one
    if (count >= 1):
        res += str(count)
    return res


print compress("aabbccaabbbbbbbbc")


