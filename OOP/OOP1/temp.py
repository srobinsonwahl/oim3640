class Cat:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        """overload the internal str"""
        return 'this is a cat'
    
messi = Cat('Messi')
print(messi)