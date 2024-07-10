#base_de_conocimiento.py
from experta import Fact, Rule

def obtener_hechos_iniciales():
    return [Fact(action="diagnosticar")]

def obtener_reglas():
    return [
        Rule(Fact(action='diagnosticar'), Fact(motor_no_arranca="TRUE"), Fact(luces_encendidas="FALSE"),
             salience=1,
             action=lambda self: self.declare(Fact(diagnostico="Revise la batería."))),

        Rule(Fact(action='diagnosticar'), Fact(motor_no_arranca="TRUE"), Fact(luces_encendidas="TRUE"), Fact(chirrido_al_girar_llave="TRUE"),
             action=lambda self: self.declare(Fact(diagnostico="Revise el motor de arranque."))),

        Rule(Fact(action='diagnosticar'), Fact(motor_se_apaga_en_marcha="TRUE"),
             action=lambda self: self.declare(Fact(diagnostico="Revise el sistema de combustible."))),

        Rule(Fact(action='diagnosticar'), Fact(humo_excesivo="TRUE"),
             action=lambda self: self.declare(Fact(diagnostico="Revise el sistema de escape."))),

        Rule(Fact(action='diagnosticar'), Fact(motor_no_arranca="TRUE"), Fact(luces_encendidas="TRUE"), Fact(chirrido_al_girar_llave="FALSE"),
             action=lambda self: self.declare(Fact(diagnostico="El problema podría ser más complejo. Se recomienda una revisión completa del sistema de arranque."))),

        Rule(Fact(action='diagnosticar'), Fact(motor_no_arranca="FALSE"), Fact(motor_se_apaga_en_marcha="TRUE"), Fact(humo_excesivo="FALSE"),
             action=lambda self: self.declare(Fact(diagnostico="Podría haber un problema en la bomba de combustible o en los inyectores."))),

        Rule(Fact(action='diagnosticar'), Fact(humo_excesivo="TRUE"), Fact(motor_no_arranca="FALSE"),
             action=lambda self: self.declare(Fact(diagnostico="Verifique el nivel y la calidad del aceite del motor. Podría haber una fuga."))),

        # Nuevas reglas para ampliar la base de conocimiento
        Rule(Fact(action='diagnosticar'), Fact(temperatura_alta="TRUE"),
             action=lambda self: self.declare(Fact(diagnostico="Revise el sistema de refrigeración."))),

        Rule(Fact(action='diagnosticar'), Fact(frenos_no_funcionan="TRUE"),
             action=lambda self: self.declare(Fact(diagnostico="Revise el sistema de frenos."))),

        Rule(Fact(action='diagnosticar'), Fact(ruido_en_el_motor="TRUE"),
             action=lambda self: self.declare(Fact(diagnostico="Revise las correas del motor y los niveles de aceite."))),

        Rule(Fact(action='diagnosticar'), Fact(sistema_electrico_falla="TRUE"),
             action=lambda self: self.declare(Fact(diagnostico="Revise el alternador y el sistema eléctrico."))),

        Rule(Fact(action='diagnosticar'), Fact(motor_vibra="TRUE"),
             action=lambda self: self.declare(Fact(diagnostico="Revise los soportes del motor y el sistema de transmisión.")))
    ]
