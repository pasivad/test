print("Choose the number of Fibonacci's number")
n = input("n = ")
a1 = 1
a2 = 10
i = 0
counter = 60
if int(n) > 60:
    counter = int(n)
while i < counter-2:
    i = i + 1
    res = a1 + a2
    a1 = a2
    a2 = res
    if i == int(n)-2:
        print("Fibonacci's number (" + str(n) + ") = " + str(res))
    if i == 58:
        print("Fibonacci's number (60) = " + str(res))