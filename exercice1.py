import random

class Citation:
    def __init__(self, texte):
        self.texte = texte

    #retour en string quand la classe est appellé
    def __str__(self):
        return self.texte

class Citations:
    def __init__(self):
        self.citations = [
            Citation("L'homme est un loup pour l'homme."),
            Citation("Rien de grand ne s'est accompli dans le monde sans passion."),
            Citation("On n'est pas sérieux, quand on a dix-sept ans"),
            Citation("Science sans conscience n'est que ruine de l'âme."),
            Citation("Il y a deux histoires : l'histoire officielle, menteuse, qu’on enseigne, puis l'Histoire secrète, où sont les véritables causes des événements."),
        ]
    #fonction random pour choisir une citations
    def citation_aleatoire(self):
        return random.choice(self.citations)

#recupere les citations
citations = Citations()
#avec les citations déja prise on execute une fonction aléatoire
citation = citations.citation_aleatoire()
#affichage de la citation
print(citation)