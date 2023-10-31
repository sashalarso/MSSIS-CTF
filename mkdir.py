import os

# Nombre de dossiers à créer à chaque niveau
niveau1 = 100
niveau2 = 100

# Répertoire racine où commencer
racine = "/home"  # Remplacez par le chemin de votre choix

# Crée les dossiers de niveau 1
for i in range(1, niveau1 + 1):
    dossier_niveau1 = os.path.join(racine, f"dir1_{i}")
    os.makedirs(dossier_niveau1)

    # Crée les dossiers de niveau 2 dans chaque dossier de niveau 1
    for j in range(1, niveau2 + 1):
        dossier_niveau2 = os.path.join(dossier_niveau1, f"dir2_{j}")
        os.makedirs(dossier_niveau2)

print(f"Structure de répertoires créée avec {niveau1} dossiers de niveau 1, chacun contenant {niveau2} dossiers de niveau 2.")

