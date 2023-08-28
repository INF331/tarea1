class Usuario:
    #constructor
    def __init__(self, nombre_usuario, contraseña_usuario, email_usuario, pregunta_1, respuesta_1, pregunta_2, respuesta_2):
        self.nombre_usuario = nombre_usuario
        self.contraseña_usuario = contraseña_usuario
        self.email_usuario= email_usuario
        self.pass_list = {}
        self.pregunta_recuperacion_1= pregunta_1
        self.respuesta_recuperacion_1= respuesta_1
        self.pregunta_recuperacion_2= pregunta_2
        self.respuesta_recuperacion_2= respuesta_2
    
    def agregar_constrasena(self, buffer, contrasena, email):
        if self.email_usuario == email :
            self.pass_list[buffer] = contrasena
    
    def eliminar_contrasena(self, email):
        if self.email_usuario == email :
            print("¿Qué constraseña deseas eliminar?")

            for item in range(len(list(self.pass_list.keys()))):
                print("{} .- {}".format(item, self.pass_list))
            
            opcion = int(input("Seleccione: "))
            remover = list(self.pass_list.keys()[opcion])

            try:
                if opcion not in range(len(list(self.pass_list.keys()))):
                    print("seleccione una opción válida")
                
                else:
                    del self.pass_list[remover]
            
            
            except:
                print("Opción no válida")

    def modificar_contraseña(self,nueva_contraseña, contraseña_anterior, email):
        #validacion_correo & contraseña
        if (self.email_usuario == email):
            if(self.contraseña_usuario == contraseña_anterior):
                self.contraseña_usuario= nueva_contraseña
                print ('Contraseña cambiada correctamente')

        else:
            print('La contraseña no ha podido ser modificada, verificar datos enviados')

    def recuperar_contraseña(self, email, respuesta_1, respuesta_2):
        #validacion_correo & contraseña
        if (self.email_usuario == email):
            if(self.respuesta_recuperacion_1 == respuesta_1):
                if(self.respuesta_recuperacion_2 == respuesta_2): 
                    print('Datos verificados correctamente')
                    print('La contraseña recuperada es:'+ self.contraseña_usuario) 
                else: 
                    print('Respuesta invalida')
            else: 
                print('Respuesta invalida')

        else:
            print('La contraseña no ha podido ser modificada, verificar datos enviados')

  


#Usuario de ejemplo
usuario_ej = Usuario('usuario1', 'contraseña1', 'usuario1@gmail.com','Pregunta 1', 'Respuesta 1','Pregunta 2', 'Respuesta 2')

try:
    accion = float(input('¿Qué desea hacer?:\n (1) Registro \n (2) Modificar contraseña \n (3) Recuperar contraseña \n (4)Eliminar contraseña \n'))
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
        contraseña_antigua = input('Ingrese su contraseña antigua: ')
        contraseña_nueva = input('Ingrese su contraseña nueva: ')
        #Hay que cambiar esta linea cuando juntemos los programas!!!!
        usuario_ej.modificar_contraseña(contraseña_nueva, contraseña_antigua, correo)

    elif (accion == 3):
        correo = input('Ingrese su correo para recuperar contraseña: ')
        print(usuario_ej.pregunta_recuperacion_1)
        respuesta_1 = input('Ingrese su respuesta: ')
        print(usuario_ej.pregunta_recuperacion_2)
        respuesta_2 = input('Ingrese su respuesta: ')
        #Hay que cambiar esta linea cuando juntemos los programas!!!!
        usuario_ej.recuperar_contraseña(correo, respuesta_1, respuesta_2)
    
    elif (accion == 4):
        correo = input("Ingrese su correo para eliminar una contraseña: ")
        #Eliminar esto después
        usuario_ej.eliminar_contrasena(correo)

except ValueError:
   exit('Opción no valida')



