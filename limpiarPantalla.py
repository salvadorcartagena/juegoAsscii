import os
from readchar import readchar,readkey,key

def terminal_clear():
    os.system('cls'if os.name == 'nt' else 'clear')

def main():
    numero = 0
    while numero <= 49:
        res = readchar()        
        if res == "n":            
            numero += 1      
                
        terminal_clear()
        print(f"Número actual: {numero}")
        print("Para continuar el contador presiona N ")
        
if __name__ == "__main__":
    main()