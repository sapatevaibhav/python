try:
    a=int(input('1:'))
    b=int(input('2:'))
    print(a/b)
except IOError as e:
    print(e)
else:
    print('not')