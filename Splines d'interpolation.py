import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Données d'exemple
x = np.linspace(0, 10, 10)
y = np.sin(x)  # Valeurs en fonction de x

# Calcul de la spline cubique
spline = CubicSpline(x, y)

# Évaluation de la spline sur des points plus fins
x_fine = np.linspace(0, 10, 100)
y_fine = spline(x_fine)

# Affichage
plt.plot(x, y, 'ro', label='Points de données')
plt.plot(x_fine, y_fine, label="Spline cubique d'interpolation")
plt.legend()
plt.show()
