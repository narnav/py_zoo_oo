import json
from Animal import Animal

class Zoo:
    animals=[]
    def __init__(self):
        pass

    def add_animal(self,name="", age=0, danger=True):
        self.animals.append( Animal(name,age,danger))

    def remove_animal(self,victim):
        self.animals.remove(victim)

    def search_animal(self,animal_name):
        for animal in self.animals:
            if type( animal ) is Animal:
                if animal.name== animal_name: return animal
        return None

    def get_animals_as_json_ar(self):
        res=[]
        for animal in self.animals:
            res.append(json.loads( animal.__str__()))
        return res

    def __str__(self) -> str:
        res=""
        for animal in self.animals:
            res+= animal.__str__()
        return res
