class Jugador:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        self.goles = 0
        self.partidos = 0
    def agregar_estadistica(self, goles):
        self.goles += goles
        self.partidos += 1
    def mostrar_info(self):
        print(f" {self.nombre} | posicion: {self.posicion} | goles: {self.goles} | partidos: {self.partidos}")
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        print(f"jugador {jugador.nombre} agregado al equipo {self.nombre}.\n")
    def mostrar_jugadores(self):
        if not self.jugadores:
            print(f"no hay jugadores registrados en {self.nombre}.")
        else:
            print(f"\n jugadores del equipo {self.nombre}:")
            for jugador in self.jugadores:
                jugador.mostrar_info()
            print()
def menu():
    equipos = []
    while True:
        print("sistema deportivo")
        print("1. crear equipo")
        print("2. agregar jugador a equipo")
        print("3. mostrar jugadores de un equipo")
        print("4. registrar goles de un jugador")
        print("5. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            nombre_equipo = input("nombre del equipo: ")
            equipo = Equipo(nombre_equipo)
            equipos.append(equipo)
            print(f"equipo {nombre_equipo} creado.\n")
        elif opcion == "2":
            nombre_equipo = input("nombre del equipo: ")
            equipo = next((e for e in equipos if e.nombre.lower() == nombre_equipo.lower()), None)
            if equipo:
                nombre_jugador = input("nombre del jugador: ")
                posicion = input("posicion del jugador: ")
                jugador = Jugador(nombre_jugador, posicion)
                equipo.agregar_jugador(jugador)
            else:
                print("equipo no encontrado.\n")
        elif opcion == "3":
            nombre_equipo = input("nombre del equipo: ")
            equipo = next((e for e in equipos if e.nombre.lower() == nombre_equipo.lower()), None)
            if equipo:
                equipo.mostrar_jugadores()
            else:
                print("equipo no encontrado.\n")
        elif opcion == "4":
            nombre_equipo = input("nombre del equipo: ")
            equipo = next((e for e in equipos if e.nombre.lower() == nombre_equipo.lower()), None)
            if equipo:
                nombre_jugador = input("nombre del jugador: ")
                jugador = next((j for j in equipo.jugadores if j.nombre.lower() == nombre_jugador.lower()), None)
                if jugador:
                    try:
                        goles = int(input(f"goles anotados por {jugador.nombre}: "))
                        jugador.agregar_estadistica(goles)
                        print(f"estadistica actualizada para {jugador.nombre}.\n")
                    except ValueError:
                        print("goles invalidos.\n")
                else:
                    print("jugador no encontrado.\n")
            else:
                print("equipo no encontrado.\n")
        elif opcion == "5":
            print("saliendo del sistema...")
            break
        else:
            print("opcion invalida.\n")
menu()