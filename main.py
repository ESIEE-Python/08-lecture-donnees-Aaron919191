#### Imports et définition des variables globales
import random

FILENAME = "listes.csv"

#### Fonctions secondaires
def read_data(filename):
    """retourne le contenu du fichier <filename>

        Args:
            filename (str): nom du fichier à lire

        Returns:
            list: le contenu du fichier (1 list par ligne)
        """
    data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip().split(";")
            try:
                data.append([int(x) for x in line])
            except ValueError:
                print("Erreur : Une ligne contient des éléments non numériques.")
                data.append([])
    return data

def get_list_k(data, k):
    if k >= 0 and k < len(data):
        return data[k]
    return None

def get_first(l):
    if l:
        return l[0]
    return None

def get_last(l):
    if l:
        return l[-1]
    return None

def get_max(l):
    if l:
        return max(l)
    return None

def get_min(l):
    if l:
        return min(l)
    return None

def get_sum(l):
    if l:
        return sum(l)
    return None

#### Fonction principale
def main():
    data = read_data(FILENAME)
    print("Données chargées :")
    for i, l in enumerate(data):
        print(f"Liste {i}: {l}")

    k = 1
    selected_list = get_list_k(data, k)

    if selected_list:
        print("\n")
        print(f"Liste sélectionnée (indice {k}): {selected_list}")
        print(f"Premier élément : {get_first(selected_list)}")
        print(f"Dernier élément : {get_last(selected_list)}")
        print(f"Valeur maximale : {get_max(selected_list)}")
        print(f"Valeur minimale : {get_min(selected_list)}")
        print(f"Somme des éléments : {get_sum(selected_list)}")
    else:
        print(f"Impossible de sélectionner une liste avec l'indice {k}.")


if __name__ == "__main__":
    main()