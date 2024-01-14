# def silnia(a):

    # return a * silnia(a-1)
#a!=
#1, dla a = 1,0
#a(a-1) dla a>1

# def potegowanie(pod,wyk):
#     if wyk==0:
#         return 1
#
#     else:
#         print(wyk)
#         return(pod*potegowanie(pod, wyk-1))
#
# potegowanie(2,8)

def f(n):
    if n == 1 or n == 0:
        return 1
    else:
        return f(n-1)+f(n-2)

print(f(40))