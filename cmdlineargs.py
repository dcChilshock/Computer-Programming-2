import sys #provides access to command line args

def main(args):
  #(c-style "main/entrypoint" function)
  if len(args) <= 0:
    print("HELLO BITCH")
    return
  print("HEloo,sss ", args[0])
  for arg in args:
    print(arg)


if __name__ == "__main__": 
  main(sys.argv[1:])
  #also see the "argparse " python module for more in depth stuff about this