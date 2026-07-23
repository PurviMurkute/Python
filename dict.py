a = {
 "key": "value",
 "harry": "code",
 "marks": 100,
 "list": [1, 2, 9]
 }

print(a["key"])  # Output: value
print(a, type(a))  # Output: 100 <class 'dict'>
print(a.items())  # Output: dict_items([('key', 'value'), ('harry', 'code'), ('marks', 100), ('list', [1, 2, 9])])
print(a.keys())  # Output: dict_keys(['key', 'harry', 'marks', 'list'])