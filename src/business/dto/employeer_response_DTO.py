class EmployeerResponseDTO:
    def __init__(self, id:str, name:str, departament_id:str, have_dependents:bool):
        self.id = id
        self.name = name
        self.departament_id = departament_id
        self.have_dependents = have_dependents