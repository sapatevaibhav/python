def f1(n):
    if n%2==0:
        print('even')
    def f2(n):
        if n>0:
            print('positive')
    f2(n)
n=int(input("Enter number: "))
f1(n)