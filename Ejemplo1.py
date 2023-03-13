class Persona1:
    pass
    def idioma():
        return 'luis habla en aleman'
    
class Persona2:
    def idioma():
        return 'Pedro habla en ruso'
    

persona1 = Persona1
persona2 = Persona2
print(persona1.idioma())
print(persona2.idioma())