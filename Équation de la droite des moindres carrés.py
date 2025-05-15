import numpy as np
import matplotlib.pyplot as plt

# Génération de données simulées
np.random.seed(0)
n = 200
x = np.linspace(-5, 5, n)
e = 0.2 * np.random.randn(n)  # Bruit aléatoire
y = 1 / (1 + x**2) + e  # Fonction avec bruit

# Régression linéaire (moindres carrés)
coeffs = np.polyfit(x, y, 1)  # Degré 1 pour la régression linéaire

# Calcul de la droite de régression
y_fit = np.polyval(coeffs, x)

# Affichage des résultats
plt.scatter(x, y, label='Données avec bruit', color='red')
plt.plot(x, y_fit, label=f'Droite de régression: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}', color='blue')
plt.legend()
plt.show()

print(f"Équation de la droite : y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")
