#punto2
import datetime 
import random 

class Historia:
    def __init__(self):
        self.__IDHistoria = self.generar_codigo('H')
        self.__IDMascota = None
        self.__fecha = ""
        self.__descrip = ''
        self.__veterinario = ""

    def generar_codigo(self, letra):
        numero = random.randint(0, 99999)
        return f"{letra}{numero:05d}"
    
    # Getters
    def ver_IDHistoria(self):
        return self.__IDHistoria
    def ver_IDMascota(self):
        return self.__IDMascota
    def ver_fecha(self):
        return self.__fecha
    def ver_descrip(self):
        return self.__descrip
    def ver_veterinario(self):
        return self.__veterinario

    # Setters
    def asignar_IDHistoria(self, IDHistoria):
        self.__IDHistoria = IDHistoria
    def asignar_IDMascota(self, IDMascota):
        self.__IDMascota = IDMascota
    def asignar_fecha(self, fecha):
        self.__fecha = fecha
    def asignar_descrip(self, descrip):
        self.__descrip = descrip
    def asignar_veterinario(self, veterinario):
        self.__veterinario = veterinario

    def validarFecha(self, fecha_str):
        try:
            datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            return True
        except ValueError:
            print("Fecha inválida. Usa el formato dd/mm/aaaa.")
            return False
    
    def __str__(self):
        return (
            f"ID Historia Clínica: {self.ver_IDHistoria()}\n"
            f"ID Mascota: {self.ver_IDMascota()}\n"
            f"Fecha: {self.ver_fecha()}\n"
            f"Descripción: {self.ver_descrip()}\n"
            f"Veterinario: {self.ver_veterinario()}"
        )

class Mascota:
    def __init__(self):
        self.__IDMascota = self.generar_codigo('M')
        self.__nombre = ""
        self.__tipo = ""
        self.__raza = ""
        self.__edad = 0
        self.__propietario = ''
        self.__telefono = 0
        self.historias = [] 

    def generar_codigo(self, letra):
        numero = random.randint(0, 99999)
        return f"{letra}{numero:05d}"

    # Getters
    def ver_IDMascota(self):
        return self.__IDMascota
    def ver_nombre(self):
        return self.__nombre
    def ver_tipo(self):
        return self.__tipo
    def ver_raza(self):
        return self.__raza
    def ver_edad(self):
        return self.__edad
    def ver_propietario(self):
        return self.__propietario
    def ver_telefono(self):
        return self.__telefono

    # Setters
    def asignar_IDMascota(self, IDMascota):
        self.__IDMascota = IDMascota
    def asignar_nombre(self, nombre):
        self.__nombre = nombre
    def asignar_tipo(self, tipo):
        self.__tipo = tipo
    def asignar_raza(self, raza):
        self.__raza = raza
    def asignar_edad(self, edad):
        self.__edad = edad
    def asignar_propietario(self, propietario):
        self.__propietario = propietario
    def asignar_telefono(self, telefono):
        self.__telefono = telefono

    def agregar_historia(self, historia):
        self.historias.append(historia)

    def eliminar_historia(self, id_historia):
        self.historias = [h for h in self.historias if h.ver_IDHistoria() != id_historia]

    def mostrar_historias(self):
        if not self.historias:
            print("No hay historias registradas.")
        else:
            for h in self.historias:
                print(h)
                print("-" * 40)

    def __str__(self):
        return (
            f"ID Mascota: {self.ver_IDMascota()}\n"
            f"Nombre: {self.ver_nombre()}\n"
            f"Tipo: {self.ver_tipo()}\n"
            f"Raza: {self.ver_raza()}\n"
            f"Edad: {self.ver_edad()} años\n"
            f"Propietario: {self.ver_propietario()}\n"
            f"Teléfono: {self.ver_telefono()}"
        )

class Veterinaria:
    def __init__(self):
        self.mascotas = {}  # IDMascota : objeto Mascota

    def registrar_mascota(self, mascota):
        self.mascotas[mascota.ver_IDMascota()] = mascota
        print(f"\n ---Mascota registrada con ID {mascota.ver_IDMascota()} --\n")

    def eliminar_mascota(self, id_mascota):
        if id_mascota in self.mascotas:
            del self.mascotas[id_mascota]
            print("\n----Mascota eliminada.-----\n")
        else:
            print("\n--Mascota no encontrada.--\n")

    def mostrar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas registradas.")
        else:
            for mascota in self.mascotas.values():
                print(mascota)
                print("-" * 40)

    def __str__(self):
        if not self.mascotas:
            return "No hay mascotas registradas en la veterinaria."

        resultado = "\n-----Registro de la Veterinaria-----\n"
        for mascota in self.mascotas.values():
            resultado += f"\n{mascota}\n"
            if mascota.historias:
                resultado += "  Historias clínicas:\n"
                for historia in mascota.historias:
                    resultado += f"{historia}\n{'-' * 30}\n"
            else:
                resultado += "  Sin historias clínicas registradas.\n"
        return resultado

def main():
    servicio = Veterinaria()

    while True:
        try:
            opcion = int(input('''\nIngrese una opción:
1- Ingresar una mascota
2- Eliminar una mascota
3- Ingresar una historia
4- Eliminar una historia
5- Mostrar historias de una mascota
6- Mostrar sistema completo
7- Salir
Opción: '''))

            if opcion == 1:
                m = Mascota()
                m.asignar_nombre(input("Nombre de la mascota: "))
                m.asignar_tipo(input("Tipo: "))
                m.asignar_raza(input("Raza: "))
                m.asignar_edad(int(input("Edad: ")))
                m.asignar_propietario(input("Nombre del propietario: "))
                m.asignar_telefono(int(input("Teléfono: ")))

                servicio.registrar_mascota(m)
                print(m)

            elif opcion == 2:
                id_m = input("Ingrese el ID de la mascota a eliminar: ")
                servicio.eliminar_mascota(id_m)

            elif opcion == 3:
                id_m = input("Ingrese el ID de la mascota para ingresar historia: ")
                if id_m in servicio.mascotas:
                    h = Historia()
                    h.asignar_IDMascota(id_m)

                    fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
                    while not h.validarFecha(fecha):
                        fecha = input("Fecha inválida. Ingrese la fecha (dd/mm/aaaa): ")
                    h.asignar_fecha(fecha)

                    h.asignar_descrip(input("Descripción de la consulta: "))
                    h.asignar_veterinario(input("Nombre del veterinario: "))

                    servicio.mascotas[id_m].agregar_historia(h)
                    print("\nHistoria registrada con éxito:")
                    print(h)
                else:
                    print("Mascota no encontrada.")

            elif opcion == 4:
                id_m = input("Ingrese el ID de la mascota: ")
                if id_m in servicio.mascotas:
                    id_h = input("Ingrese el ID de la historia a eliminar: ")
                    mascota = servicio.mascotas[id_m]
                    original = len(mascota.historias)
                    mascota.eliminar_historia(id_h)
                    if len(mascota.historias) < original:
                        print("Historia eliminada correctamente.")
                    else:
                        print("Historia no encontrada.")
                else:
                    print("Mascota no encontrada.")

            elif opcion == 5:
                id_m = input("Ingrese el ID de la mascota: ")
                if id_m in servicio.mascotas:
                    servicio.mascotas[id_m].mostrar_historias()
                else:
                    print("Mascota no encontrada.")

            elif opcion == 6:
                print(servicio)

            elif opcion == 7:
                print("Saliendo del sistema. ¡Hasta pronto!")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
