if __name__ == "__main__":
	#execute from Actions.py
	from Locations import BEDROOM, BEGINNING_CORRIDOR, END_CORRIDOR, BATHROOM, WINDOW
	from Character import Character 
else:
	#execute from main.py
	from src.schemas.Locations import BEDROOM, BEGINNING_CORRIDOR, END_CORRIDOR, BATHROOM, WINDOW
	from src.schemas.Character import Character

class GoBeginningCorridor:
	def __init__(self) -> None:
		pass

	def preCondition(self, character:Character) -> bool:
		return True if character.getLocation() == BEDROOM else False

	def postCondition(self) -> str:
		return BEGINNING_CORRIDOR

class GoEndCorridor:
	def __init__(self) -> None:
		pass

	def preCondition(self, character:Character) -> bool:
		return True if character.getLocation() == BEGINNING_CORRIDOR else False

	def postCondition(self) -> str:
		return END_CORRIDOR

class GoBathroom:
	def __init__(self) -> None:
		pass

	def preCondition(self, character:Character) -> bool:
		location = character.getLocation()
		return True if (location == END_CORRIDOR or location == WINDOW) else False

	def postCondition(self) -> str:
		return BATHROOM

class GoWindow:
	def __init__(self) -> None:
		pass

	def preCondition(self, character:Character) -> bool:
		return True if character.getLocation() == BEDROOM else False

	def postCondition(self) -> str:
		return WINDOW


def getActionsAsList():
	actions = []
	actions.append(GoBeginningCorridor())
	actions.append(GoEndCorridor())
	actions.append(GoWindow())
	actions.append(GoBathroom())

	return actions

def getActionsAsDictonary():
	actions = {}
	actions["GoBeginningCorridor"] = GoBeginningCorridor()
	actions["GoEndCorridor"] = GoEndCorridor()
	actions["GoWindow"] = GoWindow()
	actions["GoBathroom"] = GoBathroom()

	return actions