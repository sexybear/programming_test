L = [6,12,18,24,30,42,48]


def distance(a,b):
    if type(a) == list and type(b) == list:
        return min(abs(min(a)-max(b)),abs(max(a)-min(b)))
    elif type(a) == list and type(b) == int:
        return min(abs(min(a)-b),abs(max(a)-b))
    elif type(a) == int and type(b) == list:
        return min(abs(min(b)-a),abs(max(b)-a))
    else:
        return abs(a-b)
        

def single_linkage():
    global L
    L_dict = {}
    i = 0
    for item in L:
        L_dict[i] = item
        i += 1

    L_distance = {}

    for i in L_dict.keys():
        L_distance[i] = []
        k = 0
        for j in L:
            if i == k:
                L_distance[i].append(0)
            else:
                L_distance[i].append(distance(j,L_dict[i]))
            k = k+1
    temp = float('inf')
    result_store = [0,0]

    for i in L_distance.keys():
        k = 0
        for item in L_distance[i]:
            if item <= temp and item != 0:
                temp = item
                result_store[0] = i
                result_store[1] = k
            k = k+1
    print "建立距离矩阵"
    print "第%d个元素与第%d个元素之间的距离最短，最短距离为%d"%(result_store[0],result_store[1],temp)

    H = []
    if type(L[result_store[0]]) == list:
        H.extend(L[result_store[0]])
    else:
        H.append(L[result_store[0]])
    if type(L[result_store[1]]) == list:
        H.extend(L[result_store[1]])
    else:
        H.append(L[result_store[1]])
    del L[result_store[0]]
    del L[result_store[1]]

    L.append(H)
    print "合并存在最短距离的簇"
    print "现在聚类的状态： ",
    print L
    return L
    


if __name__ == "__main__":

    L_temp = []
    while len(L_temp) != 1:
        print "------------------------------"
        L_temp = single_linkage()

