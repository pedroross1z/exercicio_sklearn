import numpy as np
from sklearn.ensemble import IsolationForest

acessos = np.array([
    [9, 1, 200], [10, 1, 500], [14, 2, 300], [11, 1, 250], [16, 1, 400],
    [3, 40, 900000],
    [10, 1, 350], [15, 2, 280],
    [2, 55, 800000],
])

detector = IsolationForest(contamination=0.25, random_state=42)
resultados = detector.fit_predict(acessos)

for i, (amostra, r) in enumerate(zip(acessos, resultados)):
    status = "ANOMALIA" if r == -1 else "Normal"
    print(f"Amostra {i}: {amostra.tolist()} -> {status}")

print("\nAmostras anômalas:")
for i in np.where(resultados == -1)[0]:
    print(f"Amostra {i}: {acessos[i].tolist()}")
