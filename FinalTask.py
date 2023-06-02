engAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
colors = ['amber', 'black', 'copper', 'dark blue', 'emerald green', 
          'fairylight', 'gold', 'hazel', 'ivory', 'jade', 'khaki', 
          'maroon', 'neon', 'orange', 'purple', 'quazar', 'red', 
          'silver', 'turquoise', 'ube', 'violet', 'white', 
          'xiketic', 'yellow', 'zappo']
class dragon():
    def __init__(self, height, flammability, color):
        self.height = height
        self.flammability = flammability
        self.color = color.lower()

    def __str__(self):
        return f'Dragon with height {self.height}, danger {self.flammability} and color {self.color}.'
    
    def __repr__(self):
        return f'Dragon({self.height}, {self.flammability}, {self.color})'
    
    def __add__(self, other):
        if isinstance(other, dragon):
            height = int((self.height+other.height)/2)
            flammability = max(self.flammability, other.flammability)
            color = str()
            for i in colors:
                if i[0] == engAlphabet[min(engAlphabet.index(self.color[0]), 
                                           engAlphabet.index(other.color[0]))-1]:
                    color = i
                    break
            return dragon(height, flammability, color)
        else: return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, int):
            return dragon(self.height-self.height//other, 
                          self.flammability+self.flammability%other, 
                          self.color)
        else: return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, dragon):
            return (self.height < other.height and 
                    self.flammability < other.flammability and 
                    engAlphabet.index(self.color[0]) < engAlphabet.index(other.color[0]))
        else: return NotImplemented

    def __le__(self, other):
        if isinstance(other, dragon):
            return (self.height <= other.height and 
                    self.flammability <= other.flammability and 
                    engAlphabet.index(self.color[0]) <= engAlphabet.index(other.color[0]))
        else: return NotImplemented

    def __eq__(self, other):
        if isinstance(other, dragon):
            return (self.height == other.height and 
                    self.flammability == other.flammability and 
                    self.color == other.color)
        else: return NotImplemented

    def __ne__(self, other):
        if isinstance(other, dragon):
            return (self.height != other.height or 
                    self.flammability != other.flammability or 
                    self.color != other.color)
        else: return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, dragon):
            return (self.height > other.height and 
                    self.flammability > other.flammability and 
                    engAlphabet.index(self.color[0]) > engAlphabet.index(other.color[0]))
        else: return NotImplemented

    def __ge__(self, other):
        if isinstance(other, dragon):
            return (self.height >= other.height and 
                    self.flammability >= other.flammability and 
                    engAlphabet.index(self.color[0]) >= engAlphabet.index(other.color[0]))
        else: return NotImplemented
            
    def change_color(self, color):
        if isinstance(color, str):
            self.color = color.lower()
        else: return NotImplemented

drake = dragon(60, 15, 'White')
print(drake)
drake2 = dragon(60, 15, 'yellow')
print(drake2)
print(drake == drake2)
drake.change_color('yellow')
print(drake)
print(drake == drake2)
drago = dragon(31, 34, 'Gold')
print(drago)
salamence = drake + drago
print(salamence)
drago -= 5
print(drago)
print(drake < drago, salamence <= drake2, 
      drago == salamence, drago != drake, 
      salamence > drake, drake2 >= drake)