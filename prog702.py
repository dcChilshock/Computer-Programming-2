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
          p = Bus(name,tire,city)
          vehicle.append(p)
      num = int(f.readline())
    mil = 0.0
    cnt = 0
    totstus = 0
    large = ""
    sm = "fjglkds;gjnfljgfdlkgnlkdbnldsgjgfkjlgdjslkfdjglkghghgdhsg"
    for vehicle in vehicle:
      if isinstance(vehicle, Car):
        tot += vehicle.money
        cnt += 1

      elif isinstance(vehicle, Truck):

      elif isinstance(vehicle, Bus):
  except Exception as e:
    print("error:")


  pass


if __name__ == "__main__":
  main()