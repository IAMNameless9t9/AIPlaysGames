import numpy as np

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NN:
    def __init__(self, numOfInput, numOfOutput):
        self.NumOfInputs = numOfInput
        self.NumOfOutputs = numOfOutput
        self.IHWeights = np.random.rand(self.NumOfInputs,self.NumOfInputs)
        self.HOWeights = np.random.rand(self.NumOfInputs,self.NumOfOutputs)
        self.output = np.zeros(self.NumOfOutputs)

    def feedForward(self, x):
        self.hiddenLayer = sigmoid(np.dot(x,self.IHWeights))
        self.output = sigmoid(np.dot(self.hiddenLayer, self.HOWeights))

    def backPropagate(self, y):
        d_HOWeights = np.dot(self.hiddenLayer.T, (2*(y - self.output) * sigmoid_derivative(self.output)))
        d_IHWeights = np.dot(self.hiddenLayer.T, (np.dot(2*(y - self.output) * sigmoid_derivative(self.output), self.HOWeights.T) * sigmoid_derivative(self.hiddenLayer)))

        self.HOWeights += d_HOWeights
        self.IHWeights += d_IHWeights


#if __name__ == "__main__":
#    X = np.array([[0,0,1],
#                  [0,1,1],
#                  [1,0,1],
#                  [1,1,1]])
#    y = np.array([[0],[1],[1],[0]])
#    nn = NeuralNetwork(X,y)#
#
#    for i in range(1500):
#        nn.feedforward()
#        nn.backprop()
#
#    print(nn.output)