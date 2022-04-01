from ex import *
if __name__ == '__main__':
    exer=input("select an exercise\n")
    match exer:
        case '1':
            listOne = [3, 6, 9, 12, 15, 18, 21]
            listTwo = [4, 8, 12, 16, 20, 24, 28]
            ex=ex1(listOne,listTwo)
            ex.make_ex1(listOne,listTwo)
        case '2':
            sampleList = [34, 54, 67, 89, 11, 43, 94]
            ex=ex2(sampleList)
            ex.make_ex2(sampleList)
        case '3':
            sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
            ex=ex3(sampleList)
            ex.make_ex3(sampleList)
        case '4':
            sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
            ex=ex4(sampleList)
            ex.make_ex4(sampleList)
        case '6':
            firstSet = {23, 42, 65, 57, 78, 83, 29}
            secondSet = {57, 83, 29, 67, 73, 43, 48}
            ex=ex6(firstSet,secondSet)
            ex.make_ex6(firstSet,secondSet)
        case '7':
            firstSet = {57, 83, 29}
            secondSet = {57, 83, 29, 67, 73, 43, 48}
            ex=ex7(firstSet,secondSet)
            ex.make_ex7(firstSet,secondSet)
        case '8':
            rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
            sampleDict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
            ex=ex8(rollNumber,sampleDict)
            ex.make_ex8(rollNumber,sampleDict)
        case '9':
            speed = { 'Jan':47,'Feb ':52,' March':47,' April':44,' May ':52,'June ':53, ' July':54, ' Aug ':44,' Sept ':54}
            ex=ex9(speed)
            ex.make_ex9(speed)
        case '10':
            sampleList = [87, 52, 44, 53, 54, 87, 52, 53]
            ex=ex10(sampleList)
            ex.make_ex10(sampleList)