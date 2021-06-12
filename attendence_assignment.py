## Question

# In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
# You are not allowed to miss classes for four or more consecutive days. 
# Your graduation ceremony is on the last day of the academic year, which is the Nth day.

# Your task is to determine the following:

# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony. 


def func(n,count,maxC):
    # checking the max value of count using max inbuilt funtion because we are making it zero.
    maxC = max(count, maxC)
    
    # if n is zero then exit from the function
    if(n == 0):
        
        # checking maxC if its greater then three(means missing class for four or more consecutive days)
        if(maxC > 3):
            return 1
        return 0
    
    inc = func(n-1, count + 1, maxC)
    exc = func(n-1, 0, maxC)
    
    return inc + exc

# takeing input from user
n = input()

missed_classes =func(int(n), 0, 0)
max_possibility = pow(2, int(n))

# To find the number of ways to attend classes we have to substract missed class possibility from max possibility 
print("The number of ways to attend classes " + str(max_possibility-missed_classes))

# The probability of missing ceremony will be missed_classed divided by max_possibility
print("The probability for miss graduation ceremony will be " + str(missed_classes / max_possibility))
