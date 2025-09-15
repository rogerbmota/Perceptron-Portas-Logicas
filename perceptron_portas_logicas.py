import numpy as np

class Perceptron:
    def __init__(self):
        self.weights = None
        self.bias = None

    def _step_function(self, x):
        return 1 if x >= 0 else 0

    def train(self, inputs, outputs, learning_rate=0.1, epochs=100):
        num_features = inputs.shape[1]

        self.weights = np.random.uniform(-1, 1, num_features)
        self.bias = np.random.uniform(-1, 1)

        print(f"Pesos iniciais: {self.weights}, Bias inicial: {self.bias}")

        for epoch in range(epochs):
            errors = 0
            for i in range(len(inputs)):
                weighted_sum = np.dot(inputs[i], self.weights) + self.bias
                prediction = self._step_function(weighted_sum)
                error = outputs[i][0] - prediction
                
                if error != 0:
                    errors += 1
                    self.weights += learning_rate * error * inputs[i]
                    self.bias += learning_rate * error
            
            if errors == 0:
                print(f"\nConvergência alcançada na época {epoch + 1}!")
                break
        
        print(f"Pesos finais: {self.weights}, Bias final: {self.bias}\n")

    def predict(self, inputs):
        if self.weights is None or self.bias is None:
            raise ValueError("O modelo precisa ser treinado antes de fazer predições.")
            
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return self._step_function(weighted_sum)

if __name__ == '__main__':
    perceptron = Perceptron()

    print("## Treinando para a porta lógica AND ##")
    
    inputs_and = np.array([[0,0], [0,1], [1,0], [1,1]])
    outputs_and = np.array([[0], [0], [0], [1]])

    perceptron.train(inputs=inputs_and,
                     outputs=outputs_and,
                     learning_rate=0.1,
                     epochs=100)

    print("Testando predições para a porta AND:")
    for i in range(len(inputs_and)):
        prediction = perceptron.predict(inputs_and[i])
        print(f"Entrada: {inputs_and[i]}, Saída Esperada: {outputs_and[i][0]}, Predição: {prediction}")