import numpy as np

# Activation Functions
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def softmax(x):
    exps = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exps / np.sum(exps, axis=1, keepdims=True)

# Loss Function
def cross_entropy_loss(y_pred, y_true):
    n_samples = y_true.shape[0]
    logp = - np.log(y_pred[range(n_samples), y_true])
    loss = np.sum(logp) / n_samples
    return loss

# Initialize the neural network
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))
    
    def forward(self, X):
        # Input to hidden
        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = relu(self.Z1)
        
        # Hidden to output
        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        self.A2 = softmax(self.Z2)
        
        return self.A2
    
    def backward(self, X, y, output, learning_rate):
        n_samples = X.shape[0]
        
        # Calculate gradients
        dZ2 = output
        dZ2[range(n_samples), y] -= 1
        dZ2 /= n_samples
        
        dW2 = np.dot(self.A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)
        
        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * relu_derivative(self.Z1)
        
        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)
        
        # Update weights and biases
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
    
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)
            
            # Compute loss
            loss = cross_entropy_loss(output, y)
            print(f'Epoch {epoch+1}/{epochs}, Loss: {loss}')
            
            # Backward pass and update weights
            self.backward(X, y, output, learning_rate)
    
    def predict(self, X):
        output = self.forward(X)
        return np.argmax(output, axis=1)

# Sample dataset (XOR problem)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0])

# Parameters
input_size = 2
hidden_size = 2
output_size = 2
learning_rate = 0.1
epochs = 10000

# Create and train the neural network
nn = NeuralNetwork(input_size, hidden_size, output_size)
nn.train(X, y, epochs, learning_rate)

# Predict on training data
predictions = nn.predict(X)
print(f'Predictions: {predictions}')
print(f'Actual: {y}')
