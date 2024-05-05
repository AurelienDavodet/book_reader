def chunck_text(texte):
    taille_segment = 4096
    segments = []
    debut = 0

    while debut < len(texte):
        # Ne coupe pas au milieu des mots si possible
        fin = debut + taille_segment
        if fin < len(texte) and texte[fin] != " " and texte[fin - 1] != " ":
            fin = (
                texte.rfind(" ", debut, fin) + 1
            )  # Trouve l'espace le plus proche pour éviter de couper un mot

        segments.append(texte[debut:fin].strip())  # Ajoute le segment actuel à la liste
        debut = fin  # Déplace le point de départ pour le prochain segment

    return segments
