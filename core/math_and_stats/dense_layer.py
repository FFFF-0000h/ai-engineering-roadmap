import numpy as np

def relu(x: np.ndarray) -> np.ndarray:
    """Activation function: zeroes out negative values."""
    return np.maximum(0, x)

class DenseLayer:
    """A fully-connected neural network layer from scratch using NumPy."""
    def __init__(self, input_dim: int, output_dim: int):
        # Initialize weights randomly, bias as zeros
        self.weights = np.random.randn(input_dim, output_dim) * 0.01
        self.bias = np.zeros((1, output_dim))
        
    def forward(self, x: np.ndarray) -> np.ndarray:
        """Computes Linear Transformation + ReLU Activation."""
        # Linear step: Y = X * W + b
        linear_output = x @ self.weights + self.bias
        # Non-linear activation step
        return relu(linear_output)

if __name__ == "__main__":
    # Batch of 2 input samples, each with 3 features
    inputs = np.array([[1.0, -2.0, 3.0],
                       [-4.0, 5.0, -1.0]])
    
    # Layer that transforms 3 input features into 4 output features
    layer = DenseLayer(input_dim=3, output_dim=4)
    output = layer.forward(inputs)
    
    print("Input Shape:", inputs.shape)       # (2, 3)
    print("Weight Shape:", layer.weights.shape) # (3, 4)
    print("Output Shape:", output.shape)     # (2, 4)
    print("\nLayer Output:\n", output)
