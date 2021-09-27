a = [0.1, 0.2, 0.4, 0.8, 0.9]
b = [0.2, 0.2, 0.2, 0.2, 0.2]
prob = 0
print("Percentage of getting the side 'H' by flipping coin (H,H,H,T,H,T,H,H)")
for j in range(3):
    for i in range(5):
        prob = prob + (a[i]*b[i])
    print("Before " + str(j+1) + " flip = " + "{:.3f}".format(prob))
    for i in range(5):
        b[i] = (b[i] * a[i]) / prob
    prob = 0

for j in range(1):
    for i in range(5):
        prob = prob + ((a[i])*b[i])
    print("Before 4 flip = " + "{:.3f}".format(prob))
    for i in range(5):
        b[i] = (b[i] * (1-a[i])) / (1-prob)
    prob = 0

for j in range(1):
    for i in range(5):
        prob = prob + (a[i]*b[i])
    print("Before 5 flip = " + "{:.3f}".format(prob))
    for i in range(5):
        b[i] = (b[i] * a[i]) / prob
    prob = 0

for j in range(1):
    for i in range(5):
        prob = prob + ((a[i])*b[i])
    print("Before 6 flip = " + "{:.3f}".format(prob))
    for i in range(5):
        b[i] = (b[i] * (1-a[i])) / (1-prob)
    prob = 0

for j in range(3):
    for i in range(5):
        prob = prob + (a[i]*b[i])
    print("Before " + str(j+7) + " flip = " + "{:.3f}".format(prob))
    for i in range(5):
        b[i] = (b[i] * a[i]) / prob
    prob = 0