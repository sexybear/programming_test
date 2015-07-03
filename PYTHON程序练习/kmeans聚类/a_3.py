L = [6,12,18,24,30,42,48]
Index = {}
if __name__ == "__main__":
    i = 0
    for item in L:
        Index[i] = item
        i = i+1
    print Index

    Group = []
    Group_index = {}

    for item in L:
        Group.append(item)

    for i in Index.keys():
        Group_index[i] = []
        for j in L:
            Group_index[i].append(abs(j-Index[i]))
    print Group_index

    for i in Group_index.keys():
        Group_result = {}
        Group_result[i] = []
        Group_
                            

    
