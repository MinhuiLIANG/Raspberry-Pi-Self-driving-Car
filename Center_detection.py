import numpy as np
from sklearn.mixture import GaussianMixture
'''
@func:
    K_means: k-means algorithm
@para:
    position: position of black blocks;
    threshold: judge if single line;
    epochs: number of calculating rounds;
@return:
    center_1, center_2: center of the border lines;
    class_res: 1 stands for single line detected, 2 stands for double.
'''

def K_means(position, threshold, epochs):

    if len(position) <= 5:
        return 0,0,0
    
    center_1, center_2=position[0],position[-1]
    class_1, class_2=[],[]
    for i in range(epochs):
        for item in position:
            if abs(item-center_1)<abs(item-center_2):
                class_1.append(item)
            else:
                class_2.append(item)
        if len(class_1):
            center_1=np.sum(np.array(class_1))/len(class_1)
        if len(class_2):
            center_2=np.sum(np.array(class_2))/len(class_2)
        class_1, class_2=[],[]

    if abs(center_1-center_2)<threshold:
        return center_1,center_2,1
        
    return center_1,center_2,2


'''
@func:
    GMM: GMM algorithm
@para:
    position: position of black blocks;
    threshold: judge if single line;
    epochs: number of calculating rounds;
@return:
    center_1, center_2: center of the border lines;
    class_res: 1 stands for single line detected, 2 stands for double.
'''

def GMM(position, threshold, epoch):

    if len(position) <= 5:
        return 0,0,0

    length = len(position)
    position = position.reshape((length,1))
    gm = GaussianMixture(n_components=2, random_state=0, max_iter=epoch*10).fit(position)
    center_1, center_2 = gm.means_
    position = position.reshape(length)

    if abs(center_1-center_2)<threshold:
        return center_1,center_2,1
    
    return center_1,center_2,2