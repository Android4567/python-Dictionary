l1 = []

n = int(input('Enter the count of values you want to write => '))
for i in range(n):
    val1 = int(input(f'Enter the {i+1} value => '))
    if val1 % 5 == 0:
        l1.append(val1)
    else:
        continue
l2 =[]
for i in l1:
    if i%5 == 0:
        val2 = i*i
        l2.append(val2)
    else:
        val2 = 0
res = {}
for keys,values in l1,l2:
        res.update({f'{keys} : {values}'})

print('Resulted dictionary of values divisible 5 is ',res)
