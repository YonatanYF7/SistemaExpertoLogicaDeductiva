#motor_de_inferencia.py
from experta import KnowledgeEngine, Fact, DefFacts, Rule

class DiagnosticoAutomovil(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="diagnosticar")

    @Rule(Fact(action='diagnosticar'), Fact(motor_no_arranca="TRUE"), Fact(luces_encendidas="FALSE"))
    def regla_bateria(self):
        print("Revise la batería.")

    @Rule(Fact(action='diagnosticar'), Fact(motor_no_arranca="TRUE"), Fact(luces_encendidas="TRUE"), Fact(chirrido_al_girar_llave="TRUE"))
    def regla_motor_arranque(self):
        print("Revise el motor de arranque.")

    @Rule(Fact(action='diagnosticar'), Fact(motor_se_apaga_en_marcha="TRUE"))
    def regla_sistema_combustible(self):
        print("Revise el sistema de combustible.")

    @Rule(Fact(action='diagnosticar'), Fact(humo_excesivo="TRUE"))
    def regla_sistema_escape(self):
        print("Revise el sistema de escape.")

    @Rule(Fact(action='diagnosticar'), Fact(motor_no_arranca="TRUE"), Fact(luces_encendidas="TRUE"), Fact(chirrido_al_girar_llave="FALSE"))
    def regla_problema_desconocido(self):
        print("El problema podría ser más complejo. Se recomienda una revisión completa del sistema de arranque.")

    @Rule(Fact(action='diagnosticar'), Fact(motor_no_arranca="FALSE"), Fact(motor_se_apaga_en_marcha="TRUE"), Fact(humo_excesivo="FALSE"))
    def regla_problema_combustible(self):
        print("Podría haber un problema en la bomba de combustible o en los inyectores.")

    @Rule(Fact(action='diagnosticar'), Fact(humo_excesivo="TRUE"), Fact(motor_no_arranca="FALSE"))
    def regla_aceite_motor(self):
        print("Verifique el nivel y la calidad del aceite del motor. Podría haber una fuga.")

    @Rule(Fact(action='diagnosticar'), Fact(temperatura_alta="TRUE"))
    def regla_refrigeracion(self):
        print("Revise el sistema de refrigeración.")

    @Rule(Fact(action='diagnosticar'), Fact(frenos_no_funcionan="TRUE"))
    def regla_frenos(self):
        print("Revise el sistema de frenos.")

    @Rule(Fact(action='diagnosticar'), Fact(ruido_en_el_motor="TRUE"))
    def regla_ruido_motor(self):
        print("Revise las correas del motor y los niveles de aceite.")

    @Rule(Fact(action='diagnosticar'), Fact(sistema_electrico_falla="TRUE"))
    def regla_sistema_electrico(self):
        print("Revise el alternador y el sistema eléctrico.")

    @Rule(Fact(action='diagnosticar'), Fact(motor_vibra="TRUE"))
    def regla_motor_vibra(self):
        print("Revise los soportes del motor y el sistema de transmisión.")
