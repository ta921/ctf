from numpy.linalg import solve

left = [[2,1,1,1,1]
    ,[1,2,1,1,1]
    ,[1,1,2,1,1]
    ,[1,1,1,2,1]
    ,[1,1,1,1,2]]

right = [[2504408575853],[2440285994541],[2426159182680],[2163980646766],[2465934208374]]

flags = solve(left,right)
print(flags)
flag = ''

for i in flags:
    flag += int(i).to_bytes(5,'big').decode()

print(flag)
#uiuctf{tr4c1ng^&&_mult5!}