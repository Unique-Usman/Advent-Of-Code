import os


def findMaxElves(file):
    f=open(file, "r")
    elvesList = []
    elvelist = []
    for line in f.readlines():
        if line.strip() == "":
            elvesList.append(elvelist)
            elvelist = []
        else:
            elvelist.append(int(line.strip()))
    maxElvesValue = max(elvesList)
    maxELvesPos = elvesList.index(maxElvesValue) + 1
    return(maxElvesValue[0], maxELvesPos)

def main():
    file = "file.txt"
    print(findMaxElves(file))


if __name__ == "__main__":
    main()
