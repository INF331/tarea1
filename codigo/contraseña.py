import hashlib

class Usuario:
    #constructor
    def __init__(self, email_usuario):
        self.email_usuario= email_usuario
        self.pass_list = {}
        self.cargar_datos()
        
    def cargar_datos(self):
        try:
            with open('contraseñas.txt', 'r') as archivo:
                texto = archivo.readlines()
                for linea in texto:
                    if linea.startswith(f'Usuario: {self.email_usuario}'):
                        contenido = linea.strip().split(", ")
                        for partes in contenido:
                            if "Plataforma: " in partes:
                                plataforma = partes.split(": ")[1]
                            elif "Contraseña: " in partes:
                                contrasena = partes.split(": ")[1]
                        self.pass_list[plataforma] = contrasena
        except FileNotFoundError:
            pass
        
    def encriptado_contrasena(self, contrasena):
        encriptado=hashlib.sha256(contrasena.encode())
        return encriptado.hexdigest()
    
    def agregar_constrasena(self, buffer, contrasena, email):
            self.pass_list[buffer] = self.encriptado_contrasena(contrasena)
            self.guardar_contrasena(buffer, self.pass_list[buffer]) 

    def guardar_contrasena(self, buffer, contrasena_encriptada):
        with open('contraseñas.txt', 'a') as file:
            file.write(f'Usuario: {self.email_usuario}, Plataforma: {buffer}, Contraseña: {contrasena_encriptada}\n')
    
    def actualizar_txt(self):
        try:
            with open('contraseñas.txt', 'r') as archivo:
                lineas = archivo.readlines()
            
            with open('contraseñas.txt', 'w') as archivo:
                for linea in lineas:
                    if not linea.startswith(f'Usuario: {self.email_usuario}'): #Filtro por correo usuario
                        archivo.write(linea)
            
            with open('contraseñas.txt', 'a') as archivo:
                for plataforma, contrasena in self.pass_list.items():
                    archivo.write(f'Usuario: {self.email_usuario}, Plataforma: {plataforma}, Contraseña: {contrasena}\n')
        except FileNotFoundError:
            pass

    def eliminar_contrasena(self, email):
        if self.email_usuario == email :
            print("¿Qué constraseña deseas eliminar?")

            opciones = list(self.pass_list.keys())
            for indice, plataforma in enumerate(opciones):
                print(f"{indice + 1}. {plataforma}")
            
            opcion = int(input("Seleccione: ")) - 1 

            try:
                if opcion not in range(len(opciones)):
                    print("Seleccione una opcion válida.")
                
                else:
                    remover = opciones[opcion]
                    del self.pass_list[remover]
                    self.actualizar_txt()
            except:
                print("Opción no válida")

    def modificar_contraseña(self,email):
        if self.email_usuario == email :
            print("¿Qué constraseña deseas modificar?")

            opciones = list(self.pass_list.keys())
            for indice, plataforma in enumerate(opciones):
                print(f"{indice + 1}. {plataforma}")
            
            opcion = int(input("Seleccione: ")) - 1

            try:
                if opcion not in range(len(opciones)):
                    print("seleccione una opción válida")
                
                else:
                    modificar = opciones[opcion]
                    contraseña_anterior = input("Ingrese contraseña anterior: ")

                    if modificar in self.pass_list:
                        if self.pass_list[modificar] == self.encriptado_contrasena(contraseña_anterior):
                            contraseña_nueva = input("Ingrese contraseña nueva: ")
                            self.pass_list[modificar]= self.encriptado_contrasena(contraseña_nueva)
                            self.actualizar_txt()
                            print ('Contraseña cambiada correctamente')  
                    else: 
                        print('La contraseña no ha podido ser modificada, verificar datos enviados')

            except:
                print("Opción no válida")
        else:
            print('La contraseña no ha podido ser modificada, verificar datos enviados')

    def recuperar_contraseña(self, email):
        if self.email_usuario == email :
            opciones = list(self.pass_list.keys())

            print("¿Qué constraseña deseas recuperar?")

            for indicee, plataforma in enumerate(opciones):
                print(f'{indicee + 1}. {plataforma}')
           
            opcion = int(input("Seleccione: ")) - 1

            try:
                if opcion in range(len(opciones)):
                    recuperar = opciones[opcion]
                    contrasena_encriptada = self.pass_list[recuperar]
                    contrasena_desincriptada = self.desencriptar(contrasena_encriptada)
                    print(f"La contraseña para {recuperar} es: {contrasena_desincriptada}")
                else:
                    print('Opción no válida.')
            except:
                print("Opción no válida")
        else:
            print('La contraseña no ha podido ser recuperada, verificar datos enviados')

#Usuario de ejemplo
usuario_ej = Usuario('usuario1@gmail.com')

try:
    accion = float(input('¿Qué desea hacer?:\n (1) Registro \n (2) Modificar contraseña \n (3) Recuperar contraseña \n (4) Eliminar contraseña \n'))
    if (accion not in [1,2,3,4]):
        print('Opción no valida')

    elif (accion == 1):
        correo = input("Ingrese su correo para agregar una contraseña: ")
        nombre = input("Ingrese a la plataforma que pertenece esta contraseña: ")
        contrasena = input("Ingrese la contraseña: ")
        #Eliminar esto
        usuario_ej.agregar_constrasena(nombre, contrasena, correo)

    elif (accion == 2):
        correo = input('Ingrese su correo para modificar contraseña: ')
        #Hay que cambiar esta linea cuando juntemos los programas!!!!
        usuario_ej.modificar_contraseña(correo)

    elif (accion == 3):
        correo = input('Ingrese su correo para recuperar contraseña: ')
        #Hay que cambiar esta linea cuando juntemos los programas!!!!
        usuario_ej.recuperar_contraseña(correo)
    
    elif (accion == 4):
        correo = input("Ingrese su correo para eliminar una contraseña: ")
        #Eliminar esto después
        usuario_ej.eliminar_contrasena(correo)

except ValueError:
   exit('Opción no valida') 

