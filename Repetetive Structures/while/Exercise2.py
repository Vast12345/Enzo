valor_tecnico = 800_000
valor_videojuego = 1_000_000
valor_animacion = 1_200_000

beca_academic = 0.5
beca_cultural = 0.4

while True:
    code = input("Input your given code: ")
    name = input("Input your given name: ")
    academic = input("Choose your academic proffesion:\n1. Tecnico de sistemas\n2. Tecnico en desarrollo de videojuegos\n3. Tecnico en Animacion Digital\n")
    beca = input("Choose your Beca:\n1. Beca Academico\n2. Beca Cultural\n3. Sin Beca\n")
    
    

    
    if academic == 1:
        if beca == 1:
            beca = beca_academic
            matricula = valor_tecnico * beca
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        elif beca == 2:
            beca = beca_cultural
            matricula = valor_tecnico * beca
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        elif beca == 3:
            matricula = valor_tecnico
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        
    elif academic == 2:
        if beca == 1:
            beca = beca_academic
            matricula = valor_videojuego * beca
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        elif beca == 2:
            beca = beca_cultural
            matricula = valor_videojuego * beca
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        elif beca == 3:
            matricula = valor_videojuego
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        else:
            print("Invalid option")
    elif academic == 3:
        if beca == 1:
            beca = beca_academic
            matricula = valor_animacion * beca
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        if beca == 2:
            beca = beca_cultural
            matricula = valor_animacion * beca
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        if beca == 3:
            matricula = valor_animacion
            print("", "=" * 30)
            print(f"Your valor matricula is {matricula}")
        else:
            print("Invalid option")



