marks_dic = {}

Student_name = input('Enter the Student name => ')

marks_dic.update({'Student Name': Student_name})

English = int(input('Enter the marks of English => '))
Hindi = int(input('Enter the marks of Hindi => '))
Maths = int(input('Enter the marks of Maths => '))
Science = int(input('Enter the marks of Science => '))
SST = int(input('Enter the marks of S.S.T => '))

marks_dic.update({'English': English})
marks_dic.update({'Hindi': Hindi})
marks_dic.update({'Maths': Maths})
marks_dic.update({'Science': Science})
marks_dic.update({'S.S.T': SST})

Total = English+Hindi+Maths+Science+SST

marks_dic.update({'Total marks': Total})

Avg = Total/5

marks_dic.update({'Average marks': Avg})

print('')

print(marks_dic)
print('')
print('')
print('Other form')
for key,value in marks_dic.items():
    print(key,':',value)
print('')
print('')