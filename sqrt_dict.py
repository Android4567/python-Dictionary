l1 = []
n = int(input('Enter the count of values you want to write => '))
for i in range(n):
    val1 = int(input(f'Enter the {i+1} value => '))
    l1.append(val1)

l2 =[]
for i in l1:
    val2 = i*i
    l2.append(val2)
    val2 = 0

res = {l1[j] : l2[j] for j in range(len(l1))}
print('Resulted dictionary is ',res)




