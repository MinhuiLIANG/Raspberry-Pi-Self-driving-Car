import numpy as np

'''
@func:
    k_mean_two: k-means algorithm
@para:
    black_index: position of black blocks;
    threshold: range of dead blocks;
    epochs: number of calculating rounds;
'''

def k_mean_two(black_index, threshold, epochs):
    if len(black_index) <= 2:
        return 0,0,1
    center1, center2=black_index[0],black_index[-1]
    class1, class2=[],[]
    for i in range(epochs):
        for item in black_index:
            class1.append(item) if abs(item-center1)<abs(item-center2) else class2.append(item)
        if len(class1):
            center1=np.sum(np.array(class1))/len(class1)
        if len(class2):
            center2=np.sum(np.array(class2))/len(class2)
        class1=[]
        class2=[]
        if abs(center1-center2)<threshold:
            return center1,center2,1
    return center1,center2,2