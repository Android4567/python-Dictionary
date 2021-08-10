marks_dic = {}
Eng_dic = {}
hindi_dic = {}
maths_dic = {}
avg1 = 0
avg2 =0
avg3 = 0
for i in range(5):
    val1 = int(input(f'Enter the marks of english of student {i+1} => '))
    val2 = int(input(f'Enter the marks of Hindi student {i+1} => '))
    val3 = int(input(f'Enter the marks of maths of student {i+1} => '))
    Eng_dic.update({f'Student {i+1}':val1})
    hindi_dic.update({f'Student {i+1}':val2})
    maths_dic.update({f'Student {i+1}':val3})
    avg1 = avg1 + val1
    avg2 = avg2 + val2
    avg3 = avg3 + val3
avg1 = avg1 / 5
avg2 = avg2 / 5
avg3 = avg3 / 5
marks_dic.update({'English Avg':avg1})
marks_dic.update({'Hindi Avg ':avg2})
marks_dic.update({'Maths Avg':avg3})
print(marks_dic)