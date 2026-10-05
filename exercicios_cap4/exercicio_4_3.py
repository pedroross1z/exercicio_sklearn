from sklearn.metrics import (confusion_matrix, precision_score,
                             recall_score, f1_score, accuracy_score)

y_verdadeiro = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
y_previsto = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

print("Matriz de confusão:")
print(confusion_matrix(y_verdadeiro, y_previsto))

print(f"Precisão: {precision_score(y_verdadeiro, y_previsto):.2f}")
print(f"Recall:   {recall_score(y_verdadeiro, y_previsto):.2f}")
print(f"F1:       {f1_score(y_verdadeiro, y_previsto):.2f}")
print(f"Acurácia: {accuracy_score(y_verdadeiro, y_previsto):.2f}")

print("\nInterpretação:")
print("1. A acurácia de 90% parece boa, mas é inflada pelos 8 casos normais, que são a maioria.")
print("2. O recall de 0.50 mostra que metade dos ataques reais passou despercebida.")
print("3. Num SOC, um falso negativo é uma invasão não detectada, então o recall pesa mais que a acurácia.")
