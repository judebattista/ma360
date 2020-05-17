import math

a = 0
b = 0
c = 0

size = 10000

#triangles = [(n**2 + n)/2 for n in range(1, size + 1)]
#print(triangles)

bcand = [1, 3, 5, 7]
#bcand = [2*(n**2 + n) for n in range(1, size+1)]
#print(bcand)

triples = []
missing = []
for b in bcand:
    foundTrip = False
    for a in range(1, size+1):
        c2 = a**2 + b**2
        c = math.sqrt(c2)
        if c.is_integer():
            triples.append((a, b, int(c)))
            foundTrip = True
    if foundTrip == False:
        print('failed candidate: {0}'.format(b))
        missing.append(b)
'''
print('Valid triples:')
for triple in triples:
    print(triple)
'''

print('Candidate b values missing triples: {0}'.format(missing[0]))

