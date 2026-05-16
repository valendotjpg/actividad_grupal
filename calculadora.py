def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y







def potencia(x,y):
    if y==0:
        return 1
    elif y==1:
        return x
    return x**y



def menu():
    salir = False
    while not salir:
        print("\n=== CALCULADORA ===")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicacion")
        print("4 - Division")
        print("5 - Potencia")
        print("6 - Salir")
        
        operacion = input("\nIngresa la operacion que quieras realizar: ")
        
        if operacion == "6":
            print("¡Hasta luego!")
            salir = True
            break
        
        if operacion in ["1", "2", "3", "4", "5"]:
            try:
                x = float(input("Ingresa el primer numero: "))
                y = float(input("Ingresa el segundo numero: "))
                
                if operacion == "1":
                    resultado = suma(x, y)
                    print(f"Resultado: {x} + {y} = {resultado}")
                elif operacion == "2":
                    resultado = resta(x, y)
                    print(f"Resultado: {x} - {y} = {resultado}")
                elif operacion == "3":
                    resultado = multiplicacion(x, y)
                    print(f"Resultado: {x} * {y} = {resultado}")
                elif operacion == "4":
                    resultado = division(x, y)
                    print(f"Resultado: {x} / {y} = {resultado}")
                elif operacion == "5":
                    resultado = potencia(x, y)
                    print(f"Resultado: {x} ^ {y} = {resultado}")
            except ValueError:
                print("Error: Ingresa numeros validos")
        else:
            print("Opcion invalida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
