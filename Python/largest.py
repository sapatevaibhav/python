a=int(input('Enter 1st no:'))
b=int(input('Enter 2nd no:'))
c=int(input('Enter 3rd no:'))
if a>b and a>c:
    print(a,' is largest')
elif b>a and b>c:
    print(b,' is largest')
else:
    print(c,' is largest')