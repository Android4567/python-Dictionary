dic = {}
first_name = input('Enter your first name => ')
last_name = input('Enter your last name => ')

dic.update({'name':{'first name':first_name,'last name':last_name}})


English = int(input('Enter the marks of English => '))
Hindi = int(input('Enter the marks of Hindi => '))
Maths = int(input('Enter the marks of Maths => '))
Science = int(input('Enter the marks of Science => '))
SST = int(input('Enter the marks of S.S.T => '))

dic.update({'marks':{'English': English,
'Hindi': Hindi,
'Maths': Maths,
'Science': Science,
'S.S.T': SST,
}})

clas = input('Enter your class => ')
sec = input('Enter your Section => ')

dic.update({'class':{'class': clas,'section': sec} })

roll_no = int(input('Enter your roll number => '))
dic.update({'roll no': roll_no})
print(dic)