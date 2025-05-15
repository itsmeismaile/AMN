import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import comb

class SurfaceBezier:
    def __init__(self, points_controle):
        """Initialisation avec les points de contrôle"""
        self.points = np.array(points_controle, dtype=float)
        self.m, self.n = self.points.shape[0]-1, self.points.shape[1]-1
    
    def polynome_bernstein(self, i, n, t):
        """Calcul du polynôme de Bernstein"""
        return comb(n, i) * (t**i) * ((1-t)**(n-i))
    
    def evaluer(self, u, v):
        """Évaluation de la surface au point (u,v)"""
        result = np.zeros(3)
        for i in range(self.m+1):
            for j in range(self.n+1):
                bu = self.polynome_bernstein(i, self.m, u)
                bv = self.polynome_bernstein(j, self.n, v)
                result += bu * bv * self.points[i,j]
        return result
    
    def afficher(self, resolution=25):
        """Visualisation 3D de la surface"""
        fig = plt.figure(figsize=(12, 9))
        ax = fig.add_subplot(111, projection='3d')
        
        # Génération des points de la surface
        u = np.linspace(0, 1, resolution)
        v = np.linspace(0, 1, resolution)
        U, V = np.meshgrid(u, v)
        
        surface_points = np.zeros((resolution, resolution, 3))
        for i in range(resolution):
            for j in range(resolution):
                surface_points[i,j] = self.evaluer(U[i,j], V[i,j])
        
        # Affichage surface
        ax.plot_surface(
            surface_points[:,:,0], 
            surface_points[:,:,1], 
            surface_points[:,:,2],
            rstride=1, cstride=1,
            cmap='viridis', alpha=0.8,
            antialiased=True
        )
        
        # Affichage points de contrôle
        ax.scatter(
            self.points[:,:,0].flatten(),
            self.points[:,:,1].flatten(),
            self.points[:,:,2].flatten(),
            color='red', s=50, depthshade=False
        )
        
        # Affichage réseau de contrôle
        # Lignes horizontales
        for i in range(self.m+1):
            ax.plot(
                self.points[i,:,0],
                self.points[i,:,1],
                self.points[i,:,2],
                'r-', linewidth=0.8, alpha=0.5
            )
        # Lignes verticales
        for j in range(self.n+1):
            ax.plot(
                self.points[:,j,0],
                self.points[:,j,1],
                self.points[:,j,2],
                'r-', linewidth=0.8, alpha=0.5
            )
        
        # Configuration du graphique
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Surface bicubique de Bézier avec réseau de contrôle')
        plt.tight_layout()
        plt.show()

# Définition des 16 points de contrôle pour une surface bicubique (4x4)
points_controle = [
    [[0, 0, 0],   [1, 0, 2],   [2, 0, -1],  [3, 0, 0]],
    [[0, 1, 1],   [1, 1, 3],   [2, 1, 0],   [3, 1, 1]],
    [[0, 2, -1],  [1, 2, 1],   [2, 2, 2],   [3, 2, -1]],
    [[0, 3, 0],   [1, 3, -1],  [2, 3, 1],   [3, 3, 0]]
]

# Création et affichage de la surface
surface = SurfaceBezier(points_controle)
surface.afficher(resolution=30)
