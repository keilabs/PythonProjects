class Parent():

    def print_last_name(self):
        print('Yadao')

class Child(Parent):

    def print_first_name(self):
        print('Arvin John')

arvin = Child()
arvin.print_first_name()
arvin.print_last_name()