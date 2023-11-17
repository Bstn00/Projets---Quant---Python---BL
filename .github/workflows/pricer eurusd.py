import numpy as np
from scipy.stats import norm

# Paramètres du modèle
S0 = 1.0500   # Prix initial de l'actif sous-jacent (EUR/USD)
K = 1.1300    # Prix d'exercice de l'option (EUR/USD)
r = 0.053      # Taux d'intérêt sans risque annuel
T = 1.0       # Durée de l'option en années
sigma = 0.15  # Volatilité annuelle

# Nombre de simulations Monte Carlo
n_simulations = 10000000

# Taille nominale 
nominal_size = 100000  

# Générer des échantillons aléatoires pour le modèle de Black&Scholes
np.random.seed(0)
z = np.random.standard_normal(n_simulations)
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)

# Calcul des payoffs de l'option 
payoffs = np.maximum(ST - K, 0)

# Calcul du prix total de l'option en tenant compte du nominal
option_price = np.exp(-r * T) * np.mean(payoffs) * nominal_size

print(f"Prix total de l'option d'achat (call option) sur EUR/USD : {option_price:.2f} EUR")

