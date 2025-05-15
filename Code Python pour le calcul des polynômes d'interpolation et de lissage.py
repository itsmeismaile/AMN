import numpy as np
import matplotlib.pyplot as plt

# Données simulées
np.random.seed(0)
n = 200
x = np.linspace(-5, 5, n)
e = 0.2 * np.random.randn(n)  # Bruit
y = 1 / (1 + x**2) + e  # Fonction avec bruit

# Régression polynomiale (polynôme de degré 3 pour l'interpolation)
degree = 3
coeffs = np.polyfit(x, y, degree)

# Calcul des valeurs du polynôme ajusté
y_poly = np.polyval(coeffs, x)

# Affichage des résultats
plt.scatter(x, y, color='red', label='Données avec bruit')
plt.plot(x, y_poly, label=f'Polynôme de degré {degree}', color='blue')
plt.legend()
plt.show()


