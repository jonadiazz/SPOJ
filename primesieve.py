
import math
import time
start_time = time.time()

n = 1000
low_bound = n - 1000000
low_bound = 0

a = range(low_bound,n)
sqrt_max = int(math.sqrt(n))
print sqrt_max

#a[0:n:3] = [0] * ((n-1)//3 + 1)

for i in range( 2, sqrt_max ):
    a[low_bound:n:i] = [0] * ((n-1)//i + 1)

print a
print
a = filter(None, a)
print a
print("--- %s seconds ---" % (time.time() - start_time))