#punto2
class Historia:

    def __init__(self):
        self.__IDHistoria=0
	    self.__IDMascota=0
        self.__fecha=0	
        self.__descrip=''
        self.__veterinario = "" 

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
        self.__IDHhistoria=0
        self.__nombre= " "
        self.__tipo=" "
        self.__raza=" "
        self.__edad=0
        self.__propietario=''
        self.__telefono=0

    #Getters
    def ver_IDHhistoria(self):
        return self.__IDHhistoria
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
    def asignar_IDHhistoria(self, IDHhistoria):
        self.__IDHhistoria = IDHhistoria
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
            f"ID Historia Clínica: {self.ver_IDHhistoria()}\n"
            f"Nombre: {self.ver_nombre()}\n"
            f"Tipo: {self.ver_tipo()}\n"
            f"Raza: {self.ver_raza()}\n"
            f"Edad: {self.ver_edad()} años\n"
            f"Propietario: {self.ver_propietario()}\n"
            f"Teléfono: {self.ver_telefono()}"
        )
# de aquu para abajo es un codigo reusado de un ejercicio que hicimos en clase
#para que nos guiemos y tomemos cosas si es necesario 

    def validarFecha(self, fecha_str):
        try:
            datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            return True
        except ValueError:
            print("Fecha inválida. Usa el formato dd/mm/aaaa.")
            return False
    
    def eliminarMedicamento(self,d):
        while True:
            print('MEDICAMENTOS DE LA MASCOTA')
            print(d.__verLista_Medicamentos)
            x=input('Ingrese el nombre del medicamento a eliminar:')
            if x in d.__lista_Medicamentos:
                d.__lista_medicamentos.remove(x) 
                return True
            else:
                print('El medicamento no corresponde a los disponibles, Ingrese de nuevo...')
                continue
    def verificarMedicamento(self, nombre_medicamento):
        for med in self.__lista_medicamentos:
            if med.verNombre() == nombre_medicamento:
                return True
        return False
    def __str__(self):
        tipo_str = "Felino" if self.verTipo() == "1" else "Canino"
        return f'Nombre: {self.verNombre()} \n Historia: {self.verHistoria()} \n Tipo: {tipo_str}\n--------------'

    

class Veterinaria:
    def __init__(self):
        self.__lista_mascotas = []
        self.__dict_canino={}
        self.__dict_felino={}
    
    def ingresar_dictCanFelino(self, mascota):
        tipo = mascota.verTipo()
        if tipo == '1':
            self.__dict_felino[mascota.verHistoria()] = mascota
        elif tipo == '2':
            self.__dict_canino[mascota.verHistoria()] = mascota

    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None
    
    def verCaninoFelino(self):
        print('-------FELINOS--------')
        if not self.__dict_felino:
            print('No hay pacientes felinos por el momento :(')
        else:
            for mascota in self.__dict_felino.values():
                print(f"- {mascota}")

        print('-------CANINOS--------')
        if not self.__dict_canino:
            print('No hay pacientes caninos por el momento :(')
        else:
            for mascota in self.__dict_canino.values():
                print(f"- {mascota}")

        
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)

                if masc.verTipo() == "1":
                    if historia in self.__dict_felino:
                        del self.__dict_felino[historia]
                elif masc.verTipo() == "2":
                    if historia in self.__dict_canino:
                        del self.__dict_canino[historia]

                return True  # Eliminado con éxito
        return False  # No se encontró

    def verMedicamento(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos()
        return None


def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            while True:

                if servicio_hospitalario.verNumeroMascotas() >= 10:
                    print("No hay espacio ...") 
                    continue
                historia=int(input("Ingrese la historia clínica de la mascota: "))
                #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
                if servicio_hospitalario.verificarExiste(historia) == False:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    while True:
                        tipo = input("Ingrese el tipo de mascota (1. felino o 2. canino): ")
                        if tipo == "1" or tipo == "2":
                            break
                        else:
                            print("OPCIÓN NO VÁLIDA. Intente nuevamente.")
                    peso=int(input("Ingrese el peso de la mascota: "))
                    
                    mas= Mascota()
                    mas.asignarNombre(nombre)
                    mas.asignarHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    while True:
                            fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                            if mas.validarFecha(fecha):
                                mas.asignarFecha(fecha)
                                nm = int(input("¿Cuántos medicamentos desea registrar?: "))
                                lista_med=[]

                                for i in range(nm):
                                    nm = input(f"Ingrese el nombre del medicamento #{i+1}: ")
                                    
                                    if mas.verificarMedicamento(nm):
                                        print("\n<< Ese medicamento ya está siendo administrado a la mascota, ingrese uno nuevo >>".upper())
                                    else:
                                        dosis = int(input("Ingrese la dosis: "))
                                        medicamento = Medicamento()
                                        medicamento.asignarNombre(nm)
                                        medicamento.asignarDosis(dosis)
                                        # Lo agregas directamente a la lista de la mascota
                                        mas.verLista_Medicamentos().append(medicamento)
                                break

                            else:
                                continue
                    
                    servicio_hospitalario.ingresarMascota(mas)
                    servicio_hospitalario.ingresar_dictCanFelino(mas)

                    print('---MASCOTA INGRESADA CON EXITO---')
                    break
                else:
                    print("Ya existe la mascota con el numero de historia clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))
            servicio_hospitalario.verCaninoFelino()

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            x=input('''Desea salir?
                   1. SI 
                   2. NO
                   ''')
            if x=='1':
                print("Usted ha salido del sistema de servicio de hospitalización...")
                break
            elif x=='2':
                print('Regresó al sistema----')
                continue
            else:
                print("Usted ingresó una opción no válida, intentelo nuevamente...")
                continue

        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()