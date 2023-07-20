# Найдите сумму цифр трехзначного числа.

n = int (input("n: "))

if n > 99 and n < 1000:
    m = round((n/10)%10)
    res = (n//100) + m + (n%10)
else:
    print("error")

print(res)