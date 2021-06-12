
def func(n,count,maxC):
    maxC = max(count,maxC)
    if(n==0):
        if(maxC >3):
            return 1
        return 0
    inc = func(n-1,count+1,maxC)
    exc = func(n-1,0,maxC)
    return inc+exc


n = input()
missed_classes =func(int(n),0,0)
max_possibility = pow(2,int(n))
print("The number of ways to attend classes " + str(max_possibility-missed_classes))
print("The probability for miss graduation ceremony will be " + str(missed_classes / max_possibility))