import sys

a = str(sys.argv[1])

b = [int(i) for i in a.split(",") if i.isdigit()]

nb = int(b[int(sys.argv[2])])

if nb == 0:
	ls = [nb, nb+1]
else:
	ls = [nb-1, nb]

n = 0
while n < 9:
	ls.append(ls[n+1]+ls[n])
	n = n+1

if nb == 0:
	print "On node ", str(sys.argv[2]), " the 10 first Fibonacci numbers beginning with ", str(nb), " are : ", ls[:-1]
else:
	print "On node ", str(sys.argv[2]), " the 10 first Fibonacci numbers beginning with ", str(nb), " are : ", ls[1:]


