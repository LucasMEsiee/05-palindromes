#### Fonction secondaire
"""
Ce module contient des fonctions pour vérifier si une chaîne de 
caractère est un palindrome.
"""
def ispalindrome(p):
    """
    Retourne un booléen exprimant la vérité de "p est un palindrome".

    Args: 
        p: string à tester

    Returns:
        le booléen palindrome.
    """
    # votre code ici
    p = p.lower()
    accents = "àáâäãåçèéêëìíîïñòóôöõùúûüýÿ"
    no_accents = "aaaaaaceeeeiiiinooooouuuuyy"
    # Table permettant de supprimer les caractères inutiles
    table = str.maketrans("","", " -,'?!.;:")
    table2 = str.maketrans(accents,no_accents)
    p = p.translate(table)
    p = p.translate(table2)
    p_inverse = p[::-1]
    #test de la chaîne de caratère
    if p == p_inverse:
        return True
    return False
#### Fonction principale
def main():
    """
    Fonction principale pour tester les fonctions secondaires dont
    ispalindrome
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie",
    "Oh ! cela te perd, répéta l'écho"]:
        print(s, ispalindrome(s))
if __name__ == "__main__":
    main()
