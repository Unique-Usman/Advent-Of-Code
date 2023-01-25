import os


def findMaxElves(file):
    f=open(file, "r")
    elvesList = []
    elvelist = []  

    #reading the line and appending the value in intger form to a elvelist, if the value is "" the elveslist will append to the bigger list elvesList and empties
    for line in f.readlines():
        if line.strip() == "":
            elvesList.append(elvelist)
            elvelist = []
        else:
            elvelist.append(int(line.strip()))

    #summing each value in each sub list and update the maxELvesValue to list of the individual sum of it sublist.
    for index,elve in enumerate(elvesList):
        elvesList[index] = sum(elve)
        
    maxElvesValue = max(elvesList)
    return(maxElvesValue)

def main():
    file = "file.txt"
    print(findMaxElves(file))


if __name__ == "__main__":
    main()
