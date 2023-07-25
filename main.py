from lpp.repl import start_repl

VERSION='0.1.1'

def main() -> None:
  print('LPP - v='+VERSION)
  print('Para salir ingresa salir().')
  start_repl()

if __name__ == '__main__':
  main()