from Cl702q import *

def main():
  try:
    vehicle = []
    with open("Langdat/prog702q.txt", 'r') as f:
      num = int(f.readline())
      while num != 99:
        name = f.readline()
        tire = f.readline()
        if num == 1:
          money = int(f.readline())
          p = Car(name,tire,money)
          vehicle.append(p)
        elif num == 2:
          miles = int(f.readline())
          p = Truck(name,tire,miles)
          vehicle.append(p)
        elif num == 3:
          favword == str(f.readline())
          p = Bus(name,tire,city )
          vehicle.append(p)
  except Exception as e:
    print("error:")


  pass


if __name__ == "__main__":
  main()