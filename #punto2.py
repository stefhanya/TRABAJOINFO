#punto2

import datetime 
import random 
sistema = {
    'M12345': [
        ['Max', 'Perro', 5, 'Labrador', 'Juan Pérez', 555123456],  # Datos mascota
        [
            ['H00001', '10/03/2024', 'Vacunación completa', 'Dr. López'],  # Historia 1
            ['H00004', '25/03/2024', 'Infección en el oído', 'Dr. López']  # Historia 2
        ]
    ],
    'M67890': [
        ['Luna', 'Gato', 3, 'Siames', 'María Gómez', 555654321],
        [
            ['H00002', '15/03/2024', 'Desparasitación', 'Dra. Torres']
        ]
    ],
    'M54321': [
        ['Rocky', 'Perro', 2, 'Bulldog', 'Carlos Ramírez', 555789456],
        [
            ['H00003', '20/03/2024', 'Fractura en la pata', 'Dr. González']
        ]
    ]
}
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
    
    #Getters
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

    def generar_codigo(self, letra):
        numero = random.randint(0, 99999)
        return f"{letra}{numero:05d}"

    #Getters
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
        self.sistema=sistema
        
    def agregar_mascota(self, mascota):
        id_m = mascota.ver_IDMascota()  
        datosm = [
            mascota.ver_nombre(),
            mascota.ver_tipo(),
            mascota.ver_edad(),
            mascota.ver_raza(),
            mascota.ver_propietario(),
            mascota.ver_telefono()
        ]
        self.sistema[id_m] = [datosm,[]]
    
    def eliminarMascota(self, idm):
        if idm in self.sistema:
            del self.sistema[idm]  # línea correcta
            return True
        else: 
            return False

    def agregar_historia(self, historia):
        id_m = historia.ver_IDMascota()
        if id_m not in self.sistema:
            print("No existe una mascota con ese ID.")
            return
        datosh= [
            historia.ver_IDHistoria(),
            historia.ver_fecha(),
            historia.ver_descrip(),
            historia.ver_veterinario()
        ]
        self.sistema[id_m][1].append(datosh)

    def eliminar_historia(self, id_historia):
        for id_mascota, datos in self.sistema.items():
            historias = datos[1]
            for h in historias:
                if h[0] == id_historia:
                    historias.remove(h)
                    print(f"\nHistoria {id_historia} eliminada de la mascota {id_mascota}.")
                    return True
        print("No se encontró una historia con ese ID.")
        return False
    def mostrar_historias_mascota(self, IDMascota):
        if IDMascota not in self.sistema:
            print("Mascota no encontrada.")
        else:
            historias = self.sistema[IDMascota][1]
            if not historias:
                print("Esta mascota no tiene historias registradas.")
            else:
                print(f"\n Historias clínicas de la mascota {IDMascota}:")
                for h in historias:
                    print(f"- ID: {h[0]}, Fecha: {h[1]}, Descripción: {h[2]}, Veterinario: {h[3]}")

    def __str__(self):
        if not self.sistema:
            return "No hay mascotas registradas en el sistema."

        salida = "\n Mascotas registradas con sus historias:\n"
        for id_mascota, datos in self.sistema.items():
            datos_mascota = datos[0]
            historias = datos[1]

            salida += f"\n ID: {id_mascota}\n"
            salida += f"   Nombre: {datos_mascota[0]}\n"
            salida += f"   Tipo: {datos_mascota[1]}\n"
            salida += f"   Edad: {datos_mascota[2]} años\n"
            salida += f"   Raza: {datos_mascota[3]}\n"
            salida += f"   Propietario: {datos_mascota[4]}\n"
            salida += f"   Teléfono: {datos_mascota[5]}\n"

            if historias:
                salida += f"   Historias clínicas:\n"
                for h in historias:
                    salida += f"      - ID: {h[0]}, Fecha: {h[1]}, Descripción: {h[2]}, Veterinario: {h[3]}\n"
            else:
                salida += "    Sin historias registradas.\n"

        return salida

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
6- Mostrar sistema
7- Salir
Opción: '''))

            if opcion == 1:
                m = Mascota()
                m.asignar_nombre(input("Nombre de la mascota: "))
                m.asignar_tipo(input("Tipo (Perro/Gato): "))
                m.asignar_raza(input("Raza: "))
                m.asignar_edad(int(input("Edad: ")))
                m.asignar_propietario(input("Nombre del propietario: "))
                m.asignar_telefono(int(input("Teléfono: ")))

                servicio.agregar_mascota(m)
                print("\nMascota registrada con éxito:")
                print(m)

            elif opcion == 2:
                id_m = input("Ingrese el ID de la mascota a eliminar: ")
                if servicio.eliminarMascota(id_m):
                    print("Mascota eliminada correctamente.")
                else:
                    print("Mascota no encontrada.")

            elif opcion == 3:
                h = Historia()
                id_mascota = input("Ingrese el ID de la mascota: ")
                h.asignar_IDMascota(id_mascota)

                fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
                while not h.validarFecha(fecha):
                    fecha = input("Formato incorrecto. Ingrese la fecha (dd/mm/aaaa): ")
                h.asignar_fecha(fecha)

                h.asignar_descrip(input("Descripción: "))
                h.asignar_veterinario(input("Veterinario: "))
                servicio.agregar_historia(h)
                print("\nHistoria registrada con éxito:")
                print(h)

            elif opcion == 4:
                id_h = input("Ingrese el ID de la historia a eliminar: ")
                if servicio.eliminar_historia(id_h):
                    print("Historia eliminada correctamente.")
                else:
                    print("Historia no encontrada.")

            elif opcion == 5:
                id_m = input("Ingrese el ID de la mascota: ")
                servicio.mostrar_historias_mascota(id_m)

            elif opcion == 6:
                print(servicio)

            elif opcion == 7:
                print("Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
            
        except ValueError:
            print("Entrada no válida. Intenta de nuevo con números.")


if __name__ == "__main__":
    main()
