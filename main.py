from src.schemas.Character import Character
from src.schemas.Actions import getActionsAsList, getActionsAsDictonary

def main() -> None:
	daniel:Character = Character("Daniel", "UAM", False)
	print(daniel, end="\n\n")

	actionsList = getActionsAsList()
	print(actionsList[0].postCondition(), end="\n\n")

	actionsDict = getActionsAsDictonary()
	print(actionsDict["GoBeginningCorridor"].postCondition(), end="\n\n")
	
	for a in actionsList:
		print(a.postCondition())

	print()
	
	for a in actionsDict:
		print(actionsDict[a].postCondition())

if __name__ == "__main__":
	main()