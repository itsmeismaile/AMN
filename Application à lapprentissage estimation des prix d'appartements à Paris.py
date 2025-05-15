import numpy as np
import matplotlib.pyplot as plt

# Données fictives sur les prix des appartements (en fonction de la superficie)
superficie = np.array([30, 50, 70, 90, 110, 130, 150])  # Superficie en m²
prix = np.array([150000, 200000, 250000, 300000, 350000, 400000, 450000])  # Prix en euros

# Régression polynomiale pour ajuster les prix en fonction de la superficie
degree = 2
coeffs = np.polyfit(superficie, prix, degree)

# Calcul des prix prédits
prix_predits = np.polyval(coeffs, superficie)

# Affichage des résultats
plt.scatter(superficie, prix, color='red', label='Données réelles')
plt.plot(superficie, prix_predits, color='blue', label=f'Modèle de régression (degré {degree})')
plt.xlabel('Superficie (m²)')
plt.ylabel('Prix (euros)')
plt.legend()
plt.show()

# Affichage des coefficients du modèle
print("Coefficients du modèle : ", coeffs)
