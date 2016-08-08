class Girl:

    gender = 'female'   #class variable

    def __init__(self, name):
        self.name = name    #instance variable

r = Girl('Rachel')
s = Girl('Sandy')
print(r.gender)
print(s.gender)