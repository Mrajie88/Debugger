import numpy as np
from sklearn.neural_network import MLPRegressor

def NN(X,y,shape,lines):
    if(type(shape)== tuple):
        return
    model = MLPRegressor(hidden_layer_sizes=shape)
    model.fit(X,y)

    X_virtual = np.zeros((len(lines),len(lines)))
    temp = range(len(lines))
    X_virtual[temp,temp] = 1

    y_suspect = model.predict(X_virtual)

    return y_suspect

#if __name__ =='__main__':
#    X = [[1,0,1,0,0,0,1],[1,0,0,0,1,1,1]]
#    y = [0,1]
#    print(NN(X,y,(10)))


