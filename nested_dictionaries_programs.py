# 1. Count how many times key 'a' appears in the dictionary d

def countA(d):
    count = 0
    for k, v in d.items():
        if k == "a":
            count+=1
        if isinstance(v, dict):
            count += countA(v)

    return count

d = {
    'a': 1,
    'b': {
        'a': 2,
        'd': {
            'a': 3,
            'x': 5
        }
    }
}
# print(countA(d))

# 2. sum of values of "a"
def sumOfA(d):
    sum = 0
    for key, value in d.items():
        if key == "a":
            sum +=value
        if isinstance(value, dict):
            sum +=sumOfA(value)

    return sum


d = {
    'a': 1,
    'b': {
        'a': 2,
        'd': {
            'a': 3,
            'x': 5
        }
    }
}
# print(sumOfA(d))

# 3.

def sumOfAllValues(d):
    sum = 0
    for key, value in d.items():
        if isinstance(value, (int, float)):
            sum +=value
        if isinstance(value, dict):
            sum +=sumOfAllValues(value)


    return sum

d = {
    'x': 1,
    'y': {'a': 2, 'b': {'c': 3}},
    'z': 4
}
# print(sumOfAllValues(d))

# 4. store all the values in list

def storedValuesInList(d):
    temp = []
    for key, value in d.items():
        if key == "id":
            temp.append(value)
        if isinstance(value, dict):
            temp.append(sumOfAllValues(value))
    return temp


d = {
    'user': {'id': 101, 'name': 'Alice'},
    'meta': {
        'created_by': {'id': 102},
        'owner': {'id': 103}
    }
}

# print(storedValuesInList(d))

# 5. Replace all values of key 'a' with 0
def replaceAllValueOfAToZero(d):
    for key, value  in d.items():
        if key == "a" and not isinstance(value, dict):
            d[key] = 0
        if isinstance(value, dict):
            replaceAllValueOfAToZero(value)

    return d
d = {
    'a': 1,
    'b': {
        'a': {
            'a': 2,
            'e': 3
        }
    }
}
print((replaceAllValueOfAToZero(d)))
