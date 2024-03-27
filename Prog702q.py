from Cl702q import *

def main():
  try:
    Vehicle = []
    with open("Langdat/prog702q.dat", 'r') as f:
      num = int(f.readline())
      while num != 99:
        name = f.readline()
        numTir = f.readline()
        if num == 1:
          value = int(f.readline())
          p = Car(name, numTir, value)
          Vehicle.append(p)
        elif num == 2:
          Mile = int(f.readline())
          worth = 50,000 - (Mile * .25)
          p = Truck(name, numTir, Mile, worth)
          Vehicle.append(p)
        elif num ==3:
          City = f.readline().strip()
          p = Bus(name, numTir, City)
          Vehicle.append(p)
        num = int(f.readline())
      tot = 0.0
      cnt = 0
      totstus = 0
      large = ""
      sm = "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba"
      for person in people:
        if isinstance(person, Student):
          tot += person.gpa
          cnt += 1
        elif isinstance(person, Teacher):
          totstus += person.numStudents
        elif isinstance(person, Admin):
          fw = person.favWord
          if len(fw) > len(large):
            large = fw
          if len(fw) < len(sm):
            sm = fw
      print("Average student GPA:", round(tot/cnt, 2))
      print("Total number of students taught:", totstus)
      print("Smallest favorite admin word:", sm)
      print("Largest favorite admin word:", large)



  except Exception as e:
    print("Error:", e)
  pass


if __name__ == "__main__":
  main()