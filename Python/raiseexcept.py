a = int(input('first:'))
b = int(input('second:'))
try:
    if b > 0:
        pass
    else:
        raise Exception('error')
except Exception as e:
    print(e)
