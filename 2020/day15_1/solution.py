values = [1,12,0,20,8,16] 

for i in range(len(values)-1,2019):
    look_val = values[i]
    for l in range(i-1,-1,-1):
        if values[l] == look_val:
            values.append(i-l)
            break
    else:
        values.append(0)
print(values[-1])