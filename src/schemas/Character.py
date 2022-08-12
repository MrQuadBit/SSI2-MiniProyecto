class Character:
	__name:str = ""
	__location:str = ""
	__safe:bool = False

	def __init__(self, name:str, location:str, safe:bool) -> None:
		self.__name = name
		self.__location = location
		self.__safe = safe

	def __str__(self) -> str:
		safe:str = "seguro" if self.__safe else "inseguro"
		return f"Hola me llamo {self.__name}, estoy en {self.__location} y me encuentro {safe}"

	#Setters
	def setName(self, name:str) -> None:
		self.__name = name

	def setLocation(self, location:str) -> None:
		self.__location = location

	def setSafe(self, safe:str) -> None:
		self.__safe = safe

	#Getters
	def getName(self, name:str) -> None:
		return self.__name

	def getLocation(self, location:str) -> None:
		return self.__location

	def getSafe(self, safe:str) -> None:
		return self.__safe