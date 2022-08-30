import json


class Animal:
    name=""
    age=0
    danger=True

    def __init__(self,name="", age=0, danger=True) -> None:
        self.name=name
        self.age =age
        self.danger=danger

    def __str__(self) :
        return json.dumps( {"Name":self.name, "Age":self.age, "danger":self.danger})