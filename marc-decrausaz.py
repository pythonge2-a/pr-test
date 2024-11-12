import numpy as np

import matplotlib.pyplot as plt

# Générer des données pour le graphique
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Créer le graphique
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='b', linewidth=2)

# Ajouter des titres et des légendes
plt.title('Graphique de sin(x)', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('sin(x)', fontsize=14)
plt.legend()

# Ajouter une grille
plt.grid(True)

# Afficher le graphique
plt.show()
