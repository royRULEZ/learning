class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']
    def __init__(self, name, species):
        if species not in Pet.allowed: 
            raise ValueError(f"you can't have a {species} pet!")
        self.name = name
        self.species = species 

    def set_species(Self, species):
        if species not in Pet.allowed: 
            raise ValueError(f"you can't have a {species} pet!")        
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

Pet("Fluffy", "Tiger")