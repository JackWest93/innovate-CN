class Character():
    def __init__(self, super_name, sh_name):
        self.name=super_name
        self.h_name=sh_name

    def superpower(self,power):
        self.super=power
    
    def call(self):
        print(self.super)