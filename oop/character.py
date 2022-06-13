class Character():
    def __init__(self, super_name, sh_name):
        self.name=super_name
        self.h_name=sh_name

    def superpower(self,power):
        self.sp=power
    
    def call(self):
        print(self.sp)