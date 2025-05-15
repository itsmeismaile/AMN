import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x):
    """
    Effectue l'interpolation de Lagrange.
    :param x_points: Liste des abscisses des points connus
    :param y_points: Liste des ordonnées des points connus
    :param x: Le point auquel on veut évaluer l'interpolation
    :return: La valeur interpolée en x
    """
    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Exemple d'utilisation
x_points = [1, 2, 3]
y_points = [1, 4, 9]
x_vals = np.linspace(1, 3, 100)
y_vals = [lagrange_interpolation(x_points, y_points, x) for x in x_vals]

plt.plot(x_points, y_points, 'ro', label='Points connus')
plt.plot(x_vals, y_vals, label='Interpolation de Lagrange')
plt.legend()
plt.show()
