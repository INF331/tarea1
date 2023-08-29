class Usuario:
    #constructor
    def __init__(self, nombre_usuario, email_usuario):
        self.nombre_usuario = nombre_usuario
        self.email_usuario= email_usuario
        self.pass_list = {}
    
    def agregar_constrasena(self, buffer, contrasena, email):
        if self.email_usuario == email :
            self.pass_list[buffer] = contrasena
    
    def eliminar_contrasena(self, email):
        if self.email_usuario == email :
            print("¿Qué constraseña deseas eliminar?")

            for item in range(len(list(self.pass_list.keys()))):
                print("{} .- {}".format(item, self.pass_list))
            
            opcion = int(input("Seleccione: "))
            remover = list(self.pass_list.keys())[opcion]

            try:
                if opcion not in range(len(list(self.pass_list.keys()))):
                    print("seleccione una opción válida")
                
                else:
                    del self.pass_list[remover]
            
            
            except:
                print("Opción no válida")

    def modificar_contraseña(self,email):
        if self.email_usuario == email :
            print("¿Qué constraseña deseas modificar?")

            for item, key in enumerate(self.pass_list.keys()):
                print("{} .- {}".format(item, key))
            
            opcion = int(input("Seleccione: "))
            modificar = list(self.pass_list.keys())[opcion]

            try:
                if opcion not in range(len(self.pass_list.keys())):
                    print("seleccione una opción válida")
                
                else:
                    contraseña_anterior = input("Ingrese contraseña anterior: ")
                    if(self.pass_list[modificar] == contraseña_anterior):
                        contraseña_nueva = input("Ingrese contraseña nueva: ")
                        self.pass_list[modificar]= contraseña_nueva
                        print ('Contraseña cambiada correctamente')  
                    else: 
                        print('La contraseña no ha podido ser modificada, verificar datos enviados')

            except:
                print("Opción no válida")
        else:
            print('La contraseña no ha podido ser modificada, verificar datos enviados')

    def recuperar_contraseña(self, email):
        if self.email_usuario == email :
            print("¿Qué constraseña deseas recuperar?")

            for item, key in enumerate(self.pass_list.keys()):
                print("{} .- {}".format(item, key))
            
            opcion = int(input("Seleccione: "))
            recuperar = list(self.pass_list.keys())[opcion]

            try:
                if opcion not in range(len(self.pass_list.keys())):
                    print("seleccione una opción válida")
                
                else:
                    print("La contraseña es: "+ str(self.pass_list[recuperar]))
            except:
                print("Opción no válida")
        else:
            print('La contraseña no ha podido ser recuperada, verificar datos enviados')

#Usuario de ejemplo
usuario_ej = Usuario('usuario1', 'usuario1@gmail.com')

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