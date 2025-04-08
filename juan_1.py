
datos_pacientes = [{'Nombre': 'Maria', 'Edad': 58, 'Sexo': 'M', 'Presion Arterial': '107/82 mmHg', 'Frecuencia Cardiaca': 67, 'Peso': 59.5, 'Altura': 1.51, 'Diabetes': False, 'Hipertension': False},
 {'Nombre': 'Juan', 'Edad': 72, 'Sexo': 'H', 'Presion Arterial': '130/88 mmHg', 'Frecuencia Cardiaca': 78, 'Peso': 75.2, 'Altura': 1.73, 'Diabetes': True, 'Hipertension': False},
 {'Nombre': 'Ana', 'Edad': 45, 'Sexo': 'M', 'Presion Arterial': '110/75 mmHg', 'Frecuencia Cardiaca': 55, 'Peso': 50.8, 'Altura': 1.6, 'Diabetes': False, 'Hipertension': True},
 {'Nombre': 'Pedro', 'Edad': 65, 'Sexo': 'H', 'Presion Arterial': '145/95 mmHg', 'Frecuencia Cardiaca': 85, 'Peso': 82.1, 'Altura': 1.85, 'Diabetes': True, 'Hipertension': False},
 {'Nombre': 'Laura', 'Edad': 38, 'Sexo': 'M', 'Presion Arterial': '120/80 mmHg', 'Frecuencia Cardiaca': 60, 'Peso': 55.3, 'Altura': 1.68, 'Diabetes': False, 'Hipertension': False},
 {'Nombre': 'Carlos', 'Edad': 80, 'Sexo': 'H', 'Presion Arterial': '150/90 mmHg', 'Frecuencia Cardiaca': 92, 'Peso': 88.7, 'Altura': 1.78, 'Diabetes': True, 'Hipertension': True},
 {'Nombre': 'Sofia', 'Edad': 25, 'Sexo': 'M', 'Presion Arterial': '115/78 mmHg', 'Frecuencia Cardiaca': 50, 'Peso': 48.5, 'Altura': 1.55, 'Diabetes': False, 'Hipertension': False},
 {'Nombre': 'Luis', 'Edad': 52, 'Sexo': 'H', 'Presion Arterial': '135/85 mmHg', 'Frecuencia Cardiaca': 70, 'Peso': 68.9, 'Altura': 1.7, 'Diabetes': True, 'Hipertension': False},
 {'Nombre': 'Elena', 'Edad': 68, 'Sexo': 'M', 'Presion Arterial': '125/82 mmHg', 'Frecuencia Cardiaca': 75, 'Peso': 70.1, 'Altura': 1.65, 'Diabetes': False, 'Hipertension': True},
 {'Nombre': 'Miguel', 'Edad': 40, 'Sexo': 'H', 'Presion Arterial': '118/76 mmHg', 'Frecuencia Cardiaca': 62, 'Peso': 60.5, 'Altura': 1.75, 'Diabetes': False, 'Hipertension': False}]

class Paciente:
  
    def __init__(self): #(10%)
        self.__nombre=''
        self.__edad=0
        self.__sexo=''
        self.__presion=''
        self.__frec=0
        self.__peso=0
        self.__altura=0
        self.__diabetes=False
        self.__hiper=False
    #getters
    def ver_nombre(self):
        return self.__nombre
    def ver_edad(self):
        return self.__edad
    def ver_sexo(self):
        return self.__sexo
    def ver_presion(self):
        return self.__presion
    def ver_frec(self):
        return self.__frec
    def ver_peso(self):
        return self.__peso
    def ver_altura(self):
        return self.__altura
    def ver_diabetes(self):
        return self.__diabetes
    def ver_hiper(self):
        return self.__hiper

    # setters   
    def asignar_nombre(self, nombre):
        self.__nombre = nombre
    def asignar_edad(self, edad):
        self.__edad = edad
    def asignar_sexo(self, sexo):
        self.__sexo = sexo
    def asignar_presion(self, presion):
        self.__presion = presion
    def asignar_frec(self, frec):
        self.__frec = frec
    def asignar_peso(self, peso):
        self.__peso = peso
    def asignar_altura(self, altura):
        self.__altura = altura
    def asignar_diabetes(self, diabetes):
        self.__diabetes = diabetes
    def asignar_hiper(self, hiper):
        self.__hiper = hiper

    def __str__(self):
        return (
            f"Nombre: {self.ver_nombre()}\n"
            f"Edad: {self.ver_edad()} años\n"
            f"Sexo: {self.ver_sexo()}\n"
            f"Presión arterial: {self.ver_presion()}\n"
            f"Frecuencia cardíaca: {self.ver_frec()} \n"
            f"Peso: {self.ver_peso()} kg\n"
            f"Altura: {self.ver_altura()} m\n"
            f"Diabetes: {'Sí' if self.ver_diabetes() else 'No'}\n"
            f"Hipertensión: {'Sí' if self.ver_hiper() else 'No'}"
        )
for dato_paciente in datos_pacientes:
    paciente = Paciente()
    paciente.asignar_nombre(dato_paciente['Nombre'])
    paciente.asignar_edad(dato_paciente['Edad'])
    paciente.asignar_sexo(dato_paciente['Sexo'])
    paciente.asignar_presion(dato_paciente['Presion Arterial'])
    paciente.asignar_frec(dato_paciente['Frecuencia Cardiaca'])
    paciente.asignar_peso(dato_paciente['Peso'])
    paciente.asignar_altura(dato_paciente['Altura'])
    paciente.asignar_diabetes(dato_paciente['Diabetes'])
    paciente.asignar_hiper(dato_paciente['Hipertension'])
    
    print(paciente)
    print("-" * 30)
