class Human():

#self=> this
    def __init__(self,name):
        self.name= name
    def talk(self,sentence):
        print(f"{self.name}:{sentence}")

    def walk(self):
        print(f"{self.name} is walking")

human1=Human("Methiye")
human1.talk("Merhaba")
human1.walk()

human2=Human("Merve")
human2.talk("Selam")
human2.walk()