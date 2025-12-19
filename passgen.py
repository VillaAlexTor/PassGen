import random 
import string

# Validacion de entrada
def obtener_longitud():
    while True:
        try:
            longitud = int(input("Ingrese el tamanio de la contrasenia (8-128): "))
            if 8 <= longitud <= 128:
                return longitud
            else:
                print("La longitud debe estar entre 8 y 128 caracteres")
        except ValueError:
            print("Por favor, ingrese un numero valido")

# Menu de personalizacion de caracteres
def personalizar_caracteres():
    print("\n" + "="*40)
    print("PERSONALIZACION DE CARACTERES")
    print("="*40)
    
    opciones = {
        'mayusculas': False,
        'minusculas': False,
        'digitos': False,
        'especiales': False
    }
    
    while True:
        print("\nSeleccione los tipos de caracteres a incluir:")
        print("="*30)
        print(f"1. Letras MAYUSCULAS [{'X' if opciones['mayusculas'] else ' '}]")
        print(f"2. Letras minusculas [{'X' if opciones['minusculas'] else ' '}]")
        print(f"3. Digitos (0-9) [{'X' if opciones['digitos'] else ' '}]")
        print(f"4. Caracteres especiales [{'X' if opciones['especiales'] else ' '}]")
        print("5. SELECCIONAR TODO")
        print("6. LIMPIAR SELECCION")
        print("7. FINALIZAR y GENERAR")
        print("="*30)
        
        # Mostrar estadisticas actuales
        tipos_seleccionados = sum(opciones.values())
        if tipos_seleccionados > 0:
            print(f"\nTipos seleccionados: {tipos_seleccionados}/4")
        
        try:
            seleccion = input("\nIngrese su opcion (1-7): ").strip()
            
            if seleccion == "1":
                opciones['mayusculas'] = not opciones['mayusculas']
                estado = "activadas" if opciones['mayusculas'] else "desactivadas"
                print(f"> Mayusculas {estado}")
                
            elif seleccion == "2":
                opciones['minusculas'] = not opciones['minusculas']
                estado = "activadas" if opciones['minusculas'] else "desactivadas"
                print(f"> Minusculas {estado}")
                
            elif seleccion == "3":
                opciones['digitos'] = not opciones['digitos']
                estado = "activados" if opciones['digitos'] else "desactivados"
                print(f"> Digitos {estado}")
                
            elif seleccion == "4":
                opciones['especiales'] = not opciones['especiales']
                estado = "activados" if opciones['especiales'] else "desactivados"
                print(f"> Especiales {estado}")
                
            elif seleccion == "5":
                for key in opciones:
                    opciones[key] = True
                print("> Todos los tipos activados")
                
            elif seleccion == "6":
                for key in opciones:
                    opciones[key] = False
                print("> Seleccion limpiada")
                
            elif seleccion == "7":
                # Construir la cadena de caracteres
                caracteres_disponibles = ""
                
                if opciones['mayusculas']:
                    caracteres_disponibles += string.ascii_uppercase
                if opciones['minusculas']:
                    caracteres_disponibles += string.ascii_lowercase
                if opciones['digitos']:
                    caracteres_disponibles += string.digits
                if opciones['especiales']:
                    caracteres_disponibles += string.punctuation
                
                # Verificar seleccion
                if not caracteres_disponibles:
                    print("\n! ADVERTENCIA: No ha seleccionado ningun tipo de caracteres.")
                    print("Se usaran todos los tipos por defecto.")
                    caracteres_disponibles = string.ascii_letters + string.digits + string.punctuation
                    return caracteres_disponibles
                
                # Mostrar resumen
                print("\n" + "-"*30)
                print("RESUMEN DE SELECCION:")
                if opciones['mayusculas']:
                    print(f"- MAYUSCULAS: {len(string.ascii_uppercase)} caracteres")
                if opciones['minusculas']:
                    print(f"- minusculas: {len(string.ascii_lowercase)} caracteres")
                if opciones['digitos']:
                    print(f"- Digitos: {len(string.digits)} caracteres")
                if opciones['especiales']:
                    print(f"- Especiales: {len(string.punctuation)} caracteres")
                print(f"\nTotal combinaciones: {len(caracteres_disponibles)} caracteres")
                print("-"*30)
                
                return caracteres_disponibles
                
            else:
                print("Opcion no valida. Intente de nuevo (1-7).")
                
        except KeyboardInterrupt:
            print("\n\nOperacion cancelada por el usuario.")
            exit()
        except Exception as e:
            print(f"Error inesperado: {e}")

# Programa principal
def main():
    print("="*40)
    print("GENERADOR DE CONTRASENIAS SEGURAS")
    print("="*40)
    
    # Obtener longitud
    longitud = obtener_longitud()
    
    # Personalizar caracteres
    caracteres = personalizar_caracteres()
    
    # Generar la contrasenia
    print("\nGenerando contrasenia...")
    contrasenia = ''.join(random.choice(caracteres) for i in range(longitud))
    
    # Mostrar resultado
    print("\n" + "="*40)
    print("RESULTADO")
    print("="*40)
    print(f"Longitud: {longitud} caracteres")
    print(f"Caracteres posibles: {len(caracteres)}")
    print("-"*40)
    print(f"\nCONTRASENIA GENERADA:")
    print(f"> {contrasenia}")
    print("-"*40)
    
    # Opcion para copiar o regenerar
    while True:
        print("\nOpciones:")
        print("1. Generar otra contrasenia con misma configuracion")
        print("2. Iniciar nueva configuracion")
        print("3. Salir")
        
        opcion = input("\nSeleccione opcion (1-3): ").strip()
        
        if opcion == "1":
            nueva_contrasenia = ''.join(random.choice(caracteres) for i in range(longitud))
            print(f"\nNueva contrasenia: {nueva_contrasenia}")
        elif opcion == "2":
            print("\n" + "="*40)
            main()  # Reiniciar programa
            break
        elif opcion == "3":
            print("\nGracias por usar el generador. ¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

# Ejecutar programa
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma terminado por el usuario.")