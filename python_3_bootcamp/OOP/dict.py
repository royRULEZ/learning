class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUISINESS")
        return super().__repr__()
    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE")
    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY? FINE...")
        super().__setitem__(key, value)


data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = "Tokyo"
print(data)