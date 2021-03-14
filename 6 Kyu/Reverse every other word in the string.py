import re
def reverse_alternate(string):
    string = re.sub(' +', ' ', string)
    string = string.rstrip()
    a= string.split(" ")
    a[-1].rstrip()
    for i in range(len(a)):
        if i%2!=0:
            a[i]=a[i][::-1]
    b = " ".join(a)
    return (b)
