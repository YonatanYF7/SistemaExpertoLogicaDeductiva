#main.py
from interfaz_de_usuario import obtener_datos_usuario
from motor_de_inferencia import DiagnosticoAutomovil

def main():
    print("\nBienvenido al Sistema Experto de Diagnóstico de Problemas de Automóviles")

    # Recopilación de datos del usuario
    hechos = obtener_datos_usuario()

    # Creación del motor de inferencia
    engine = DiagnosticoAutomovil()
    engine.reset()

    # Declaración de hechos en el motor de inferencia
    for hecho in hechos:
        engine.declare(hecho)

    # Ejecución del motor de inferencia
    print("\nDiagnosticos:")
    engine.run()

    print("\nGracias por usar el Sistema Experto")

if __name__ == "__main__":
    main()
