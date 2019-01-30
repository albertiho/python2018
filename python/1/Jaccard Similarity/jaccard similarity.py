import sys

a, b = list(), list()
setA, setB = set(), set()
k = int(sys.argv[1])

with open(sys.argv[2]) as ra, open(sys.argv[3]) as rb:
  aq, bq = ra.read().split('\n'), rb.read().split('\n')
  
  for d in aq:
    temp = d.split(' ')
    for q in temp:
      if len(q) > 0:
        a.append(q)
  
  for d in bq:
    temp = d.split(' ')
    for q in temp:
      if len(q) > 0:
        b.append(q)

      
for i in range(len(a)):
  if k > 1:
    q = (tuple(a[i-k+1 : i+1]))
  else:
    q = a[i]
  if(len(q) > 0 and q not in setA):
    setA.add(q)
  
for i in range(len(b)):
  if k > 1:
    q = (tuple(b[i-k+1 : i+1]))
  else:
    q = b[i]
  if(len(q) > 0 and q not in setB):
    setB.add(q)

#print((setA))
#print(len(setB))
isc = setA.intersection(setB)
u = setA.union(setB)
jac = round(len(isc)/len(u), 4)
print("JAC({}): {}".format(k, jac))