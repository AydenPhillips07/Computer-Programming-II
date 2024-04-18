from Cl701g import *

def main():
  try:
    people = []
    with open("Langdat/prog701g.dat", 'r') as f:
      num = int(f.readline())
      while num != 99:
        fn = f.readline()
        ln = f.readline()
        if num == 1:
          gpa = float(f.readline())
          p = Student(fn, ln, gpa)
          people.append(p)
        elif num == 2:
          numStu = int(f.readline())
          p = Teacher(fn, ln, numStu)
          people.append(p)
        elif num ==3:
          favW = f.readline().strip()
          p = Admin(fn, ln, favW)
          people.append(p)
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