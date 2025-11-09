# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
    nome_do_ficheiro = 'drawing.txt'
    t.up()

    try:
        with open(nome_do_ficheiro, 'r') as f:
            print('Programa aberto. Desenho iniciado')
            for linha in f:
                linha = linha.strip()

                if not linha:
                    continue

                linha_acima = linha.upper()

                if linha_acima == 'UP':
                    t.up()
                elif linha_acima == 'DOWN':
                    t.down()

                else:
                    try:
                        coordenadas_str = linha.split()

                        if len(coordenadas_str) == 2:
                            x = int(coordenadas_str[0])
                            y = int(coordenadas_str[1])

                            t.goto(x, y)

                        else:
                            print(f"Linha inválida de coordenadas ignorada: '{linha}'")
                    except ValueError:
                        print(f"Coordenadas não são números válidos na linha: '{linha}'")


    except FileNotFoundError:
        print(f"O ficheiro de instruções '{nome_do_ficheiro}' não foi encontrado.")

    # Wait until window is closed
    screen.mainloop()

    print('Programa fechado')


if __name__ == "__main__":
    main()

