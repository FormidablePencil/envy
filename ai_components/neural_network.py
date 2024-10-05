import numpy as np
from typing import List, Tuple

class NeuralNetwork:
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.W1 = np.random.randn(self.hidden_size, self.input_size)
        self.b1 = np.zeros(self.hidden_size)
        self.W2 = np.random.randn(self.output_size, self.hidden_size)
        self.b2 = np.zeros(self.output_size)

    def forward(self, X: np.ndarray) -> np.ndarray:
        self.z1 = np.dot(self.W1, X.T) + self.b1.reshape(1, -1)
        self.a1 = np.maximum(0, self.z1)
        self.z2 = np.dot(self.W2, self.a1) + self.b2.reshape(1, -1)
        self.a2 = self.softmax(self.z2)
        return self.a2.T

    def softmax(self, z: np.ndarray) -> np.ndarray:
        exp_z = np.exp(z)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def train(self, X: np.ndarray, y: np.ndarray, learning_rate: float, epochs: int) -> None:
        for epoch in range(epochs):
            # Forward pass
            self.forward(X.T)

            # Backpropagation
            delta2 = self.a2 - y
            delta1 = np.dot(self.W2.T, delta2.T) * (self.a1 > 0)

            # Update weights and biases
            self.W2 -= learning_rate * np.dot(delta2.T, self.a1)
            self.b2 -= learning_rate * np.sum(delta2, axis=0)
            self.W1 -= learning_rate * np.dot(delta1.T, X.T)
            self.b1 -= learning_rate * np.sum(delta1, axis=0)