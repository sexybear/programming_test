def distance(a,b):
    return abs(a-b)

L = [6,12,18,24,30,42,48]

L_point_1 = {1:18,2:45}

L_point_2 = {1:15,2:40}

L_final_1 = {}
L_final_1[1] = []
L_final_1[2] = []
L_final_2 = {}
L_final_2[1] = []
L_final_2[2] = []

for i in L:
    if distance(i,L_point_1[1]) < distance(i,L_point_1[2]):
        L_final_1[1].append(i)
    elif distance(i,L_point_1[1]) > distance(i,L_point_1[2]):
        L_final_1[2].append(i)
    else:
        L_final_1[1].append(i)
        L_final_1[2].append(i)

L_result_1 = {}
for i in L_final_1.keys():
    L_result_1[i] = 0
    for j in L_final_1[i]:
        L_result_1[i] += (j-L_point_1[i])**2

print "第一组质心划分的结果"
print L_final_1
print "两个簇的平方误差"
print L_result_1
print "总平方误差"
print L_result_1[1]+L_result_1[2]

for i in L:
    if distance(i,L_point_2[1]) < distance(i,L_point_2[2]):
        L_final_2[1].append(i)
    elif distance(i,L_point_2[1]) > distance(i,L_point_2[2]):
        L_final_2[2].append(i)
    else:
        L_final_2[1].append(i)
        L_final_2[2].append(i)

L_result_2 = {}
for i in L_final_2.keys():
    L_result_2[i] = 0
    for j in L_final_2[i]:
        L_result_2[i] += (j-L_point_2[i])**2
        
print "第二组质心的划分结果"
print L_final_2
print "两个簇的总平方误差"
print L_result_2
print "总平方误差"
print L_result_2[1]+L_result_2[2]
