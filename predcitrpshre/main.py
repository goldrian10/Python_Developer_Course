#!/usr/bin/env python
# -- coding: utf-8 --
import sys


def private_history_branch_predictor(s, history):

    # Initial states for the counter
    # 2^s for the bits

    misses = 0 # How many times we missed
    hits = 0 # How many times we hit
    history = pow(2, history) - 1
    historyBuffer = history

    correctTaken = 0
    incorrectTaken = 0
    correctNotTaken = 0
    incorrectNotTaken = 0

    i = 0
    BHT = []
    PHT = []
    for x in range((2**s)):
        PHT.append(history)
        BHT.append(0)

    for line in sys.stdin:
        i = i + 1
        #Some of the addresses are longer than the other ones so we need some filtration
        #Masking the bits
        lineLength = line[11] # Reads the 10 position of the array
        #To avoid taking a blank space, since some are smaller
        if lineLength == " ":
            buffer = int(line[0:11])
        else:
            buffer = int(line[0:10])

        mask = buffer & ((2**s)-1)

        history = PHT[mask]


        address = history ^ mask

        temp = BHT[address]
        state = BHT[address]

        ###############12 spaces numbers##################
        ### Not taken branches ###
        # 0 = 00 which is strong not taken
        # 1 = 01 which is weakly not taken
        # 2 = 10 which is weakly taken
        # 3 = 11 which is strong taken

        if line[10] == " ":
            if ((temp == 0) & (line[11] == "N")):
                hits = hits + 1
                correctNotTaken = correctNotTaken + 1
                PHT[mask] = ((history << 1) & (historyBuffer))

            if ((temp == 1) & (line[11] == "N")):
                hits = hits + 1
                state = state - 1  # we got it correct so we go back to strong not taken
                BHT[address] = state
                correctNotTaken = correctNotTaken + 1
                PHT[mask] = ((history << 1) & (historyBuffer))

            # Weakly taken state but we missed
            if ((temp == 2) & (line[11] == "N")):
                misses = misses + 1
                state = state - 1
                BHT[address] = state
                incorrectNotTaken = incorrectNotTaken + 1
                PHT[mask] = ((history << 1) & (historyBuffer))

            # Strong taken state but we missed
            if ((temp == 3) & (line[11] == "N")):
                misses = misses + 1
                state = state - 1
                BHT[address] = state
                PHT[mask] = ((history << 1) & (historyBuffer))
                incorrectNotTaken = incorrectNotTaken + 1

            ########### Taken branches ###################

            if ((temp == 0) & (line[11] == "T")):
                misses = misses + 1
                state = state + 1
                BHT[address] = state
                PHT[address] = (((history << 1) & (historyBuffer)) | 1)
                incorrectTaken = incorrectTaken + 1

            if ((temp == 1) & (line[11] == "T")):
                misses = misses + 1
                state = state + 1
                PHT[address] = (((history << 1) & (historyBuffer)) | 1)
                BHT[address] = state
                incorrectTaken = incorrectTaken + 1

            if ((temp == 2) & (line[11] == "T")):
                hits = hits + 1
                state = state + 1
                BHT[address] = state
                PHT[address] = (((history << 1) & (historyBuffer)) | 1)
                correctTaken = correctTaken + 1

            if ((temp == 3) & (line[11] == "T")):
                hits = hits + 1
                PHT[address] = (((history << 1) & (historyBuffer)) | 1)
                correctTaken = correctTaken + 1

            # For the smaller addresses

            ############ Not Taken branches ##############

        else:

            if ((temp == 0) & (line[10] == "N")):
                hits = hits + 1
                correctNotTaken = correctNotTaken + 1
                PHT[mask] = ((history << 1) & (historyBuffer))

            if ((temp == 1) & (line[10] == "N")):
                hits = hits + 1
                state = state - 1  # we got it correct so we go back to strong not taken
                BHT[address] = state
                correctNotTaken = correctNotTaken + 1
                PHT[mask] = ((history << 1) & (historyBuffer))

            # Weakly taken state but we missed
            if ((temp == 2) & (line[10] == "N")):
                misses = misses + 1
                state = state - 1
                BHT[address] = state
                incorrectNotTaken = incorrectNotTaken + 1
                PHT[mask] = ((history << 1) & (historyBuffer))

            # Strong taken state but we missed
            if ((temp == 3) & (line[10] == "N")):
                misses = misses + 1
                state = state - 1
                BHT[address] = state
                PHT[mask] = ((history << 1) & (historyBuffer))
                incorrectNotTaken = incorrectNotTaken + 1

            ########### Taken branches ###################

            if ((temp == 0) & (line[10] == "T")):
                misses = misses + 1
                state = state + 1
                BHT[address] = state
                PHT[address] = (((history << 1) & (historyBuffer)) | 1)
                incorrectTaken = incorrectTaken + 1

            if ((temp == 1) & (line[10] == "T")):
                misses = misses + 1
                state = state + 1
                PHT[address] = (((history << 1) & (historyBuffer)) | 1)
                BHT[address] = state
                incorrectTaken = incorrectTaken + 1

            if ((temp == 2) & (line[10] == "T")):
                hits = hits + 1
                state = state + 1
                BHT[address] = state
                PHT[address] = (((history << 1) & (historyBuffer)) | 1)
                correctTaken = correctTaken + 1

            if ((temp == 3) & (line[10] == "T")):
                hits = hits + 1
                PHT[address] = (((history << 1) & (historyBuffer)) | 1)
                correctTaken = correctTaken + 1

    print(misses)
    print(hits)
    print('\n*********************')
    print('\nBranch prediction type:  \t\t\tPrivate history')
    print('\nBHT size (entries):  \t\t\t\t', 2 ** s)
    print('\nGlobal history register size: \t\t\t', 0)
    print('\nPrivate history register size: \t\t\t', 0)
    print('*********************')
    print('\nNumber of branch: \t\t\t\t', i)
    print('\nNumber of correct prediction of taken branches: ', correctTaken)
    print('\nNumber of incorrect prediction of taken branches: ',
          incorrectTaken)
    print('\nCorrect prediction of not taken branches: ', correctNotTaken)
    print('\nIncorrect prediction of not taken branches: ', incorrectNotTaken)
    print('\nPercentage of correct predictions: ', ((hits) / i) * 100)
    print('\n******************')