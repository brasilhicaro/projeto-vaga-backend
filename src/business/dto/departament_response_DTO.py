"""
Class responsible for
defining the departament
response DTO
"""
class DepartamentResponseDTO:

    """
    Method responsible for
    initializing the class
    """
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name