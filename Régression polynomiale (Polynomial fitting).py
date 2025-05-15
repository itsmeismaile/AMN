import numpy as np
import matplotlib.pyplot as plt

def polynomial_fit(x_points, y_points, degree):
    """
    Ajuste un polynôme aux données à l'aide de la régression polynomiale.
    :param x_points: Liste des abscisses des points connus
    :param y_points: Liste des ordonnées des points connus
    :param degree: Degré du polynôme à ajuster
    :return: Coefficients du polynôme ajusté
    """
    coeffs = np.polyfit(x_points, y_points, degree)
    return coeffs

# Exemple d'utilisation
x_points = np.array([1, 2, 3, 4, 5])
y_points = np.array([1, 4, 9, 16, 25])

degree = 2  # Ajuster un polynôme de degré 2
coeffs = polynomial_fit(x_points, y_points, degree)

# Créer un polynôme à partir des coefficients
poly = np.poly1d(coeffs)

# Générer les valeurs prédites par le polynôme
x_vals = np.linspace(1, 5, 100)
y_vals = poly(x_vals)

plt.scatter(x_points, y_points, color='red', label='Points réels')
plt.plot(x_vals, y_vals, label=f'Ajustement polynomial de degré {degree}')
plt.legend()
plt.show()

print("Coefficients du polynôme : ", coeffs)
