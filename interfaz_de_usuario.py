#interfaz_de_usuario.py
from experta import Fact

# Interfaz de Usuario: función para obtener los datos del usuario
def obtener_datos_usuario():
    def obtener_respuesta(pregunta):
        while True:
            respuesta = input(pregunta).strip().lower()
            if respuesta in ("si", "no"):
                return respuesta
            else:
                print("Entrada inválida. Por favor, responde 'si' o 'no'.")

    hechos = []
    respuesta = obtener_respuesta("¿El motor no arranca? (si/no): ")
    hechos.append(Fact(motor_no_arranca="TRUE" if respuesta == "si" else "FALSE"))

    if respuesta == 'si':
        respuesta = obtener_respuesta("¿Las luces se encienden? (si/no): ")
        hechos.append(Fact(luces_encendidas="TRUE" if respuesta == "si" else "FALSE"))

        if respuesta == 'si':
            respuesta = obtener_respuesta("¿Hay un chirrido al girar la llave? (si/no): ")
            hechos.append(Fact(chirrido_al_girar_llave="TRUE" if respuesta == "si" else "FALSE"))

    respuesta = obtener_respuesta("¿El motor se apaga en marcha? (si/no): ")
    hechos.append(Fact(motor_se_apaga_en_marcha="TRUE" if respuesta == "si" else "FALSE"))

    respuesta = obtener_respuesta("¿Hay humo excesivo? (si/no): ")
    hechos.append(Fact(humo_excesivo="TRUE" if respuesta == "si" else "FALSE"))

    # Nuevas preguntas para ampliar la base de conocimiento
    respuesta = obtener_respuesta("¿El motor se sobrecalienta? (si/no): ")
    hechos.append(Fact(temperatura_alta="TRUE" if respuesta == "si" else "FALSE"))

    respuesta = obtener_respuesta("¿Los frenos no funcionan correctamente? (si/no): ")
    hechos.append(Fact(frenos_no_funcionan="TRUE" if respuesta == "si" else "FALSE"))

    respuesta = obtener_respuesta("¿Hay ruido en el motor? (si/no): ")
    hechos.append(Fact(ruido_en_el_motor="TRUE" if respuesta == "si" else "FALSE"))

    respuesta = obtener_respuesta("¿El sistema eléctrico falla? (si/no): ")
    hechos.append(Fact(sistema_electrico_falla="TRUE" if respuesta == "si" else "FALSE"))

    respuesta = obtener_respuesta("¿El motor vibra al acelerar? (si/no): ")
    hechos.append(Fact(motor_vibra="TRUE" if respuesta == "si" else "FALSE"))

    return hechos
