class Dog:
  def __init__(self, name, weight, bark):
    self.dogName = name
    self.dogBark = bark
    self.dogWeight = weight
  def bark(self, loudness):
    print(self.dogName + " says:")
    for i in range(loudness):
      print(self.dogBark)



roksy = Dog("Roksy", 20, 'woof')
roksy.bark(5)

python = Dog("python", 20, 'ruf')
python.bark(2)
















