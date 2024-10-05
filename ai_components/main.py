from ai_components.neural_network import NeuralNetwork
import numpy as np

def main():
    # Example usage of the NeuralNetwork class
    input_size = 10
    hidden_size = 20
    output_size = 5

    nn = NeuralNetwork(input_size, hidden_size, output_size)

    # Generate some sample data
    X = np.random.randn(10, input_size)
    y = np.random.randint(0, output_size, size=(10,))

    # Train the neural network
    nn.train(X, y, learning_rate=0.01, epochs=1000)

    # Make a prediction
    test_input = np.random.randn(1, input_size)
    prediction = nn.forward(test_input)
    print(f"Prediction: {prediction}")
    print(f"Predicted class: {np.argmax(prediction)}")

if __name__ == "__main__":
    main()