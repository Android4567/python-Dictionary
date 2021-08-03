dic = {'name':'raj','age':'21','roll no': 21}
res = {}
for keys in dic:
    values = (dic[keys])
    res.update({values:keys})
print(res)