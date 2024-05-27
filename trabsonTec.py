path = "odd.txt"

with open(path,'r') as arq:

    commands = arq.read().strip().split('\n')
    machineDescript = commands[0]
    newCommands = []
    
    if machineDescript == ";S":
        initialState = commands[1].split(' ')[0]
        newInitalState = 'init'
        wall = "|"

        for command in commands[1:]:
            newCommand = command.split(' ')
            for _ in newCommand:
                if newCommand[0] == initialState:
                    newCommand[0] = newInitalState 
                elif newCommand[-1] == initialState:
                    newCommand[-1] = newInitalState 
            newCommand = " ".join(newCommand)
            newCommands.append(newCommand)

        deffaultCommands = f"""0 * * l 0\n0 _ {wall} r {newInitalState}\n* {wall} * r *"""

        newCommands.insert(0, deffaultCommands)
    
    else:
        
        initialState = commands[1].split(' ')[0]
        newInitalState = 'init'
        initialSymbol = '&'
        endSymbol = '$'
        allStates = []
        allSymbols = []
        
        for command in commands:
            newCommand = command.split(' ')
            
            if newCommand[0].startswith(';'):
                continue
            
            allStates.append(newCommand[0])
            allSymbols.append(newCommand[1])
            
            if newCommand[0] == initialState:
                    newCommand[0] = newInitalState
            if newCommand[-1] == initialState:
                    newCommand[-1] = newInitalState
            newCommand = " ".join(newCommand)
            newCommands.append(newCommand)
        
        allStates = list(set(allStates))
        allSymbols = list(set(allSymbols))
        
        deffaultCommands = f"""{initialState} 1 {initialSymbol} r n1
{initialState} 0 {initialSymbol} r n2
{initialState} _ {endSymbol} l {newInitalState}
{initialState}2 0 0 r {initialState}2
{initialState}2 1 0 r {initialState}1
{initialState}2 _ 0 r {initialState}
{initialState}1 0 1 r {initialState}2
{initialState}1 1 1 r {initialState}1
{initialState}1 _ 1 r {initialState}
n1 0 1 r {initialState}2
n1 1 1 r {initialState}1
n2 0 0 r {initialState}2
n2 1 0 r {initialState}1"""

        newCommands.insert(0, deffaultCommands)

        commandsComeToEnd = f'{newInitalState} {endSymbol} _ r {newInitalState}{endSymbol}\n{newInitalState}{endSymbol} _ {endSymbol} l {newInitalState}\n{newInitalState} {initialSymbol} {initialSymbol} r {newInitalState}{initialSymbol}\n'
        for state in allStates:
            commandsComeToEnd += f'{state} {endSymbol} _ r {state}{endSymbol}\n'
            commandsComeToEnd += f'{state}{endSymbol} _ {endSymbol} l {state}\n'
            
        allCommands = ''  
        for state in allStates:
            allCommands += f'{state} {initialSymbol} {initialSymbol} r new{state}_\n'
            
            if state == initialState:
                continue
            
            for symbol in allSymbols:
                for symbolAgain in allSymbols:
                    allCommands += f'new{state}{symbol} {symbolAgain} {symbol} r new{state}{symbolAgain}\n'
            
                allCommands += f'new{state}{symbol} {endSymbol} {symbol} r new{state}{endSymbol}\n'
            allCommands += f'new{state}{endSymbol} _ {endSymbol} * bi{state}\n'
            allCommands += f'bi{state} * * l bi{state}\n'
            allCommands += f'bi{state} {initialSymbol} {initialSymbol} r {state}\n'

        newCommands.insert(-1, allCommands)
        newCommands.insert(-1, commandsComeToEnd)
        
    with open(arq.name.split('.')[0] + ".out", 'w') as arq:
        arq.write("\n".join(newCommands))