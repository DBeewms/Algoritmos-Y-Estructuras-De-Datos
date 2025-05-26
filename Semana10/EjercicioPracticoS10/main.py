"""
Dado una cola con elementos y una pila vacía, desarrollar un programa que procese la cola de forma que:
- Los elementos que se encuentran en posiciones pares (0, 2, 4, ...) permanezcan en la cola.
- Los elementos que se encuentran en posiciones impares (1, 3, 5, ...) se transfieran a la pila.

Consideraciones:
- La posición de los elementos se cuenta a partir de cero (la primera posición es la 0, la segunda es la 1, etc.).
- La operación debe realizarse recorriendo la cola una sola vez.
- Al finalizar, la pila contendrá los elementos impares en orden LIFO y la cola solo los elementos pares en su orden original.
"""

from auxiliar import menu_principal

def main():
    menu_principal()

if __name__ == "__main__":
    main()