#!/usr/bin/python3

def getOldPosition(prevStages, stage):
    return prevStages[stage - 1].index(solveMemory(prevStages, stage))

def solveMemory(prevStages, stage):
    options = prevStages[stage - 1]
    display = int(options[0])
    if stage == 1:
        if display == 1: return options[2]
        if display == 2: return options[2]
        if display == 3: return options[3]
        if display == 4: return options[4]
    if stage == 2:
        if display == 1: return '4'
        if display == 2: return options[getOldPosition(prevStages, 1)]
        if display == 3: return options[1]
        if display == 4: return options[getOldPosition(prevStages, 1)]
    if stage == 3:
        if display == 1: return solveMemory(prevStages, 2)
        if display == 2: return solveMemory(prevStages, 1)
        if display == 3: return options[3]
        if display == 4: return '4'
    if stage == 4:
        if display == 1: return options[getOldPosition(prevStages, 1)]
        if display == 2: return options[1]
        if display == 3: return options[getOldPosition(prevStages, 2)]
        if display == 4: return options[getOldPosition(prevStages, 2)]
    if stage == 5:
        if display == 1: return solveMemory(prevStages, 1)
        if display == 2: return solveMemory(prevStages, 2)
        if display == 3: return solveMemory(prevStages, 4)
        if display == 4: return solveMemory(prevStages, 3)


def main(_):
    print("=== On the Subject of Memory ===")
    print("Enter all 5 numbers consecutively (like 14321), or 'b' to go back a stage.")

    prevStages = []
    while len(prevStages) < 5:
        numbers = input("Stage " + str(len(prevStages)+1) + ": ").strip()
        if numbers == 'b' and len(prevStages) > 0:
            prevStages.pop()
            continue
        if len(numbers) != 5:
            print("Dummy, that's not 5 numbers! I need all 5, try again")
            continue
        prevStages.append(list(numbers))
        print(solveMemory(prevStages, len(prevStages)))

if __name__ == '__main__':
    main({})
