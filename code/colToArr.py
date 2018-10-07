#give a1 b1 for each line return two list of a and b

f = open("rssi_lsq.txt",'r')
a = []
b = []

for line in f.readlines():
    line = line.rstrip().split(" ")
    a.append(line[0])
    b.append(line[1])

f.close

a =list(map(lambda x:float(x),a))
b = list(map(lambda x:float(x),b))
print(a, b)
