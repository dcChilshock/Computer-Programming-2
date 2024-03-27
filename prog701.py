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
          gpa = float(f.readline())\
          p = Student(fn, ln, gpa)
          people.append(p)
        elif num == 2:
          numstu = int(f.readline())
          p = Teacher(fn, ln, numstu)
          people.append(p)
        elif num == 3:
          favword == str(f.readline())
          p = Admin(fn,ln,favword)
          people.append(p)
      num = int(f.readline())
    tot = 0.0
    cnt = 0
    totstus = 0
    large = ""
    sm ="fjglkds;gjnfljgfdlkgnlkdbnldsgjkljgfkjlgdjslkfdjglkghghgdhsg"
    for person in people:
      if isinstance(person, Student):
        tot += person.gpa
        cnt += 1
      elif isinstance(person, Teacher):
        totstus += person.numstu
      elif isinstance(person, Admin):
        fw = person.favword
        if len(fw) > len(large):
          large = fw 
        if len(fw) < len(sm):
          small = fw
          
    print("Average Student Gpa:", round(tot/cnt,2))
    print("Total number of students taught:", totstus)
    print("Smallest favorite admin word:", sm)
    print("Largest favorite admin word:", large)
        
  except Exception as e:
    print("error:")


  pass


if __name__ == "__main__":
  main()