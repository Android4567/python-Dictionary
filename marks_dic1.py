marks_dic = {}
Eng_dic = {}
hindi_dic = {}
maths_dic = {}
avg1 = 0
avg2 =0
avg3 = 0
for i in range(5):
    val1 = int(input(f'Enter the english marks of {i+1} student => '))
    Eng_dic.update({f'Student{i+1}':val1})
    avg1 = avg1+val1
avg1 = avg1 / 5
print('')
for i in range(5):
    val2 = int(input(f'Enter the hindi marks of {i+1} student => '))
    hindi_dic.update({f'Student{i+1}':val2})
    avg2 = avg2+val2
avg2 = avg2 / 5
print('')
for i in range(5):
    val3 = int(input(f'Enter the maths marks of {i+1} student => '))
    maths_dic.update({f'Student{i+1}':val3})
    avg3 = avg3+val3
avg3 = avg3 / 5
print('')
marks_dic.update({'English Avg':avg1})
marks_dic.update({'Hindi Avg':avg2})
marks_dic.update({'Maths Avg':avg3})
print(marks_dic)