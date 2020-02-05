# Task 2
import numpy

a = 2 * (10 ** (-3))
b = 8.5
n = 2
i = (2, 1, 8.3)

for j in range(len(i)):
    y = numpy.sqrt((i * b) - ((b ** 2) * a))
    z = y * numpy.tan(n / 4) - numpy.e ** (1 + b)
    print(z)

    i = 1
    while i <= 3:
        y = numpy.sqrt((i * b) - ((b ** 2) * a))
        q = y * numpy.tan(n / 4) - numpy.e ** (1 + b)
        i += 0.5
        print(q)

n = (3, -6, 0.2, 2.8)
b = 2
for x in range(len(n)):
    while b <= 3:
        y = numpy.sqrt((i * b) - ((b ** 2) * a))
        w = y * numpy.tan(n[x] / 4) - numpy.e ** (1 + b)
        b += 0.5
        print(w)

