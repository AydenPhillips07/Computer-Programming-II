from Cl702q import *

def main():
  try:
    Vehicle = []
    with open("Langdat/prog702q.txt", 'r') as f:
      num = int(f.readline())
      while num != 99:
        name = f.readline()
        numTir = f.readline()
        if num == 1:
          worth = int(f.readline())
          p = Car(name, numTir, worth)
          Vehicle.append(p)
        elif num == 2:
          Mile = int(f.readline())
          worth = 50,000 - (Mile * .25)
          p = Truck(name, numTir, Mile, worth)
          Vehicle.append(p)
        elif num ==3:
          City = f.readline().strip()
          worth = 50,000
          p = Bus(name, numTir, City, worth)
          Vehicle.append(p)
        num = int(f.readline())
      totworth = 0.0
      tr = 0
      totstus = 0
      large = ""
      sm = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba"
      for Vehicle in Vehicle:
        if isinstance(Vehicle, Car):
          totworth += Vehicle.worth
          tr += Vehicle.numTir
        elif isinstance(Vehicle, Truck):
          totstus += person.numStudents
        elif isinstance(Vehicle, Bus):
          City = Vehicle.City
          if len(City) > len(large):
            large = City
      
      print("Average student GPA:", round(tot/cnt, 2))
      print("Total number of students taught:", totstus)
      print("Smallest favorite admin word:", sm)
      print("Largest favorite admin word:", large)



  except Exception as e:
    print("Error:", e)
  pass


if __name__ == "__main__":
  main()