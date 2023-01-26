


def findTotal(file):
    f=open(file, "r") #opening the file
    total_score = 0 #initiating the total score
    score_of_shape = {"X" : 1, "Y": 2, "Z" : 3} #the value of each shape X for rock, Y for paper and Z for scissors
    for line in f.readlines():
        elve, player = line.strip().split(' ')
        if player == "X":
            if elve == "A":
                total_score += score_of_shape[player] + 3
            elif elve == "B":
                total_score += score_of_shape[player] + 0
            else:
                total_score += score_of_shape[player] + 6
        elif player == "Y":
            if elve == "A":
                total_score += score_of_shape[player] + 6
            elif elve == "B":
                total_score += score_of_shape[player] + 3
            else:
                total_score += score_of_shape[player] + 0
        else:
            if elve == "A":
                total_score += score_of_shape[player] + 0
            elif elve == "B":
                total_score += score_of_shape[player] + 6
            else:
                total_score += score_of_shape[player] + 3
    return total_score



def main():
    file="file.txt"
    result  = findTotal(file)
    print(result)


if __name__ == "__main__":
    main()

