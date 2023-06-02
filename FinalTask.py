engAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
colors = ['amber', 'black', 'copper', 'dark blue', 'emerald green', 'gold', 'hazel', 'ivory', 'jade', 'khaki', 'maroon', 'neon', 'orange', 'purple', 'quazar', 'red', 'silver', 'turquoise', 'ube', 'violet', 'white', 'xiketic', 'yellow', 'zappo']
class dragon():
    def __init__(self, height, flammability, color):
        self.height = height
        self.flammability = flammability
        self.color = color

    def __str__(self):
        return f'Dragon with height {self.height}, danger {self.flammability} and color {self.color}.'
    
    def __repr__(self):
        return f'Dragon({self.height}, {self.flammability}, {self.color})'
    
    def __add__(self, element):
        if isinstance(element, dragon):
            height = int((self.height+element.height)/2)
            flammability = max(self.flammability, element.flammability)
            for i in colors:
                if i[0] == engAlphabet[min(engAlphabet.index(self.color[0]), engAlphabet.index(element.color[0]))-1]:
                    color = i
                    return
            return dragon(height, flammability, color)
    
    def __sub__(self, element):
        if isinstance(element, int):
            return dragon(self.height-self.height//element, self.flammability+self.flammability%element, self.color)
            
    def change_color(self, color):
        self.color = color

drake = dragon(60, 15, 'white')
print(drake)
drake.change_color('brown')
print(drake)
drago = dragon(30, 30, 'gold')
print(drago)
salamence = drake + drago
print(salamence)
drago -= 5
print(drago)