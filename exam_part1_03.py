# Multiples of 3 and 5.
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
# • Find the sum of all the multiples of 3 or 5 below 1000. 

def number(n):
    sum_of_all = 0
    for i in range(1,n) :
        if i%3 == 0 or i%5 == 0 :
            sum_of_all += i 
    print(sum_of_all)

number(1000)
