import sys
sys.setrecursionlimit(5000)

def sumr(n):
  if n <= 1: return n # base / ending case
  return n + sumr(n-3) #recursive case

def main():
  print(str(sumr(9669))) 
if __name__ == "__main__":
  main()

