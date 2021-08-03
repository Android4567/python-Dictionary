# Specify the variable of list
l1 = []
l2 = []

#  Ask for number of keys and values
n = int(input('Enter the count of numbers you want to make dict => '))

# append keys and values in different lists
for i in range(n):
    val1 = input(f'Enter the {i+1} key of dict => ')
    l1.append(val1)
for i in range(n):
    val2 = input(f'Enter the {i+1} value of dict => ')
    l2.append(val2)

# print keys and values
print('Keys is ',l1)
print('Values is ',l2)

# make dictionary by keys and values of two lists
res = {l1[j] : l2[j] for j in range(len(l1))}

# print the dictionary
print('resulted dict is ',res)
