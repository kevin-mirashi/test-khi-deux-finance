import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import seaborn as sns

# 1. Tableau de contingence (Donnees d'observation)
donnees = np.array([
    [10, 50, 10],  # Profil Prudent
    [40, 30, 20],  # Profil Equilibre
    [50, 10, 40],  # Profil Dynamique
])

index_profils = ["Prudent", "Equilibre", "Dynamique"]
colonnes_actifs = ["Actions", "Obligations", "Crypto"]

df = pd.DataFrame(donnees, index=index_profils, columns=colonnes_actifs)

# 2. Test du Khi-deux
chi2, p_value, dof, effectifs_theoriques = chi2_contingency(df)

# Affichage sans caracteres speciaux pour eviter l'erreur CP1252 sur Windows
print(f"Statistique du Khi-deux (Chi2) : {chi2:.4f}")
print(f"p-value : {p_value:.4e}")

# 3. Visualisation
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

df_plot = df.reset_index().melt(
    id_vars="index", var_name="Actif", value_name="Nombre d'investisseurs"
)
df_plot.rename(columns={"index": "Profil"}, inplace=True)

ax = sns.barplot(
    data=df_plot,
    x="Profil",
    y="Nombre d'investisseurs",
    hue="Actif",
    palette="Blues_d",
)

plt.title(
    "Repartition des Choix d'Actifs selon le Profil d'Investisseur\n(Test"
    f" Khi-deux p-value = {p_value:.2e})",
    fontsize=14,
    pad=15,
)
plt.xlabel("Profil d'investisseur", fontsize=12)
plt.ylabel("Effectif", fontsize=12)
plt.legend(title="Type d'Actif")

plt.tight_layout()
plt.savefig("khi2_investisseurs.png", dpi=300)
print("\nGraphique enregistre avec succes : 'khi2_investisseurs.png'")
plt.show()