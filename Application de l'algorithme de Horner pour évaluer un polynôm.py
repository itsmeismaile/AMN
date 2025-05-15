def horner(coeffs, x):
    result = coeffs[0]
    for i in range(1, len(coeffs)):
        result = result * x + coeffs[i]
    return result

# Exemple d'utilisation
coeffs = [1, -3, 2]  # x^2 - 3x + 2
x_val = 2
print(f"Valeur du polynôme en x = {x_val}: {horner(coeffs, x_val)}")
