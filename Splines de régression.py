import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

# Données avec bruit
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + 0.3 * np.random.randn(100)  # Ajout de bruit

# Calcul de la spline cubique de régression (p=3 pour une spline cubique)
spline_regression = UnivariateSpline(x, y, s=1)  # 's' est le paramètre de lissage

# Affichage des résultats
y_smooth = spline_regression(x)
plt.plot(x, y, 'ro', label='Données avec bruit')
plt.plot(x, y_smooth, label="Spline de régression")
plt.legend()
plt.show()
