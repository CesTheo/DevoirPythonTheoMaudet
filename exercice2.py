import json

class Personne:
    def __init__(self, prenom, age, genre):
        self.prenom = prenom
        self.age = age
        self.genre = genre

    def arrayformat(self):
        return {
            'prenom': self.prenom,
            'age': self.age,
            'genre': self.genre
        }

    def convertjson(self):
        return json.dumps(self.arrayformat())

personne = Personne('Theo', 22, 'masculin')
personne_json = personne.convertjson()
print(personne_json)