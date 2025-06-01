# 🎯 Challenge
# - Write a function that computes the sum and average of a list of numbers

def calc_sum_and_avg(n):                    #function
    total = sum(n)                          #calculates sum
    avg = round(total/len(n),2)             #calculates average
    return total,avg

numbers = input("Enter the numbers (separated by space) : ")  #taking values from user

list_num = list(map(float,numbers.split())) # converting them into float and storing in a list

sum,avg = calc_sum_and_avg(list_num)        # calling the function and storing values in variables

print("Sum of given values: ",sum)          # printing sum
print("Average of given values: ",avg)      # printing average