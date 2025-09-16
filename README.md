# Análise dos Testes Perceptron - Portas Lógicas

Para esta atividade, fiz alguns testes com o algoritmo do Perceptron em Python para simular o funcionamento de portas lógicas e ver como diferentes parâmetros afetam o resultado.

## 1. Testando a Taxa de Aprendizagem
Percebi que a taxa de aprendizagem faz muita diferença. Quando usei um valor muito baixo (tipo 0.001), o modelo demorou demais para aprender. Já com um valor muito alto (tipo 1.0), ele ficava instável e não chegava na resposta certa. O valor original de 0.1 funcionou muito bem, sendo rápido e estável.

## 2. Testando a Quantidade de Épocas
Fiz a mesma coisa com o número de épocas. Com poucas épocas (só 10), o Perceptron não teve tempo suficiente para aprender. Com as 100 épocas do exemplo, ele aprendeu a função perfeitamente. Testei com um número bem mais elevado de épocas (5000), mas não mudou o resultado final, só demorou mais, o que mostra que ele já tinha chegado na melhor solução.

## 3. Simulando a Porta Lógica AND
Para fazer o teste com a porta AND, a única coisa que precisei mudar foi a lista de saídas esperadas para [[0], [0], [0], [1]]. O Perceptron conseguiu aprender a função AND sem problemas, porque ela também é "linearmente separável", assim como a porta OR.

## 4. Melhorando o Código
Uma das mudanças que fiz foi extrair a função de ativação para um método separado. Antes, a mesma lógica estava repetida em dois lugares diferentes. Separar a função deixou o código mais organizado e facilitou muito na hora de fazer o próximo passo, que era trocar de função.

## 5. Trocando para a Função Degrau
Por fim, troquei a função Sigmoid pela função Degrau. A função Degrau é mais direta, só retorna 0 ou 1. Para este problema, o resultado final foi o mesmo, e o modelo continuou aprendendo corretamente. Tive a impressão de que com a função Degrau o aprendizado foi até um pouco mais rápido, já que o cálculo do erro fica mais simples.
