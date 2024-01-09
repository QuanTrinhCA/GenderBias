inputs = list()
print("Input:")

for x in range(5):
    buffer = list()
    for i in input().split():
        buffer.append(int(i))
    for i in input().split():
        buffer.append(int(i))
    inputs.append(buffer)

for x in inputs:
    result = (x[1] * x[2] / x[0]) - x[3]
    if result < 2 and result > -2:
        print("no bias")
    elif result < 5 and result > 2:
        print("some bias against women")
    elif result > -5 and result < -2:
        print("some bias against men")
    elif result > 5:
        print("heavily bias against women")
    else:
        print("heavily bias against men")