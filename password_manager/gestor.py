from credencial import Credencial;


class Gestor:
    __credenciales: list = []

    def listar_credenciales(self) -> list:
        credentials:list=[]

        for credencial in self.__credenciales:
            credentials.append(credencial)

        return credentials
    
    def crear_credencial(self) -> Credencial:
        print("Creando credencial")
        servicio: str = input("Agregar el servicio: ")
        usuario: str = input("Agregar el usuario: ")
        contrasena: str = input("Agregar la contraseña: ")

        credencial: Credencial = Credencial(
            in_servicio=servicio,
            in_usuario=usuario,
            in_contrasena=contrasena
        )
        print("Credencial creada!")
        return credencial
    
    def agregar_credencial(self, credencial: Credencial) -> None:
        self.__credenciales.append(credencial)
        print("Credencial agregada!")

    def buscar_credencial(self) -> None:
        
        servicio:str = input("Ingrese el servicio: ")
        
        for credencial in self.__credenciales:
            if credencial.servicio == servicio:
                print("----- CREDENCIAL ------")
                print("Usuario: ", credencial.__usuario)
                print("Servicio: ", credencial.servicio)
                print("Contraseña: *******")
    
    # def showAllInfo(self, credential:Credencial):

    #     print("Usuario: ", credential.)
    #     print("Servicio: ", credential.)