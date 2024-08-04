import os

def pause():
  input("Pressione Enter para continuar...")
  os.system('clear' if os.name == 'posix' else 'cls')

