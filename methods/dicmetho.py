dic = {
    'ename':'aryan',
    'add':'bhopal',
    'contact' :1234456564,
    'education ':'garduacte'


}

# print(dic)

# print(dic.keys())
# print(dic.values())
# print(f'the dictionry is {dic}and the remove data is \n {dic.popitem()}')

dic1 = dic.copy()
# print(dic1)

print(dic1.clear())
print(dic.setdefault('ename'))
print(dic1.setdefault('name'))
print(dic1.setdefault('name','rahul'))
print(dic1)

dic1.update({'name':'rahul'})
print(dic1)

print(dic.items())
print(dic.get('ename'))
print(dic1.pop('name'))
print(dic1)