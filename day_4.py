# 🎯 Challenge
# - Check if a user-entered number is prime

num = int(input("Enter a number : "))

if num == 0 or num == 1 :
    print(f"{num} is neither prime nor composite")
else:
    is_prime = True
    for i in range(2,num//2):
        if num%i == 0:
            is_prime = False
            break

    print(f"{num} is a prime number ") if is_prime else print(f"{num} is a composite number")







