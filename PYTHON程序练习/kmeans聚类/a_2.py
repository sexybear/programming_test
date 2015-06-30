L1 = []
L2 = {}
L = [6,12,18,24,30,42,48]
result = 0

def distance(a,b):
    return abs(float(a-b))

def k_means():
    global L1
    global L2
    global L
    result = 0.0
    L_result = {}
    L_means = []
    temp = 0
    for i in L2.keys():
        for j in L2[i]:
            temp += j
        L_means.append(float(temp/len(L2[i])))
        temp = 0
    
    for i in range(0,2):
        L2[i] = []
    for i in L:
        if distance(i,L_means[0]) < distance(i,L_means[1]):
            L2[0].append(i)
        elif distance(i,L_means[0]) > distance(i,L_means[1]):
            L2[1].append(i)
        else:
            L2[0].append(i)
            L2[1].append(i)
    for i in L2.keys():
        L_result[i] = 0
        for j in L2[i]:
            L_result[i] += (float(j-L_means[i]))**2
    result = float(L_result[0]+L_result[1])
    #print result
    return result

if __name__ == "__main__":
    print "请输入初始质心"
    for i in range(0,2):
        L1.append(int(raw_input()))
        L2[i] = []
    print "初始质心组为"
    print L1

    for i in L:
        if distance(i,L1[0]) < distance(i,L1[1]):
            L2[0].append(i)
        elif distance(i,L1[0]) > distance(i,L1[1]):
            L2[1].append(i)
        else:
            L2[0].append(i)
            L2[1].append(i)

    L_result = {}
    for i in L2.keys():
        L_result[i] = 0
        for j in L2[i]:
            L_result[i] += (j-L1[i])**2
    result = L_result[0]+L_result[1]

    print "初始划分"
    print L2
    print "总平方误差"
    print result
    
    for i in range(0,10):
        result_temp = k_means()
        if abs(result_temp-result)<0.1:
            result = result_temp
            break
        elif result_temp < result:
            result = result_temp

    print "最终划分"
    print L2
    print "最终总平方误差"
    print result
        
        
        
