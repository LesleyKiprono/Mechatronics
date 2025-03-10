import sys

n = len(sys.argv)
print("Total arguments passed:",n)

print(sys.argv[1])


for i in range(1,n):

    sum = sum + int(sys.argv[i])
print(sum)


