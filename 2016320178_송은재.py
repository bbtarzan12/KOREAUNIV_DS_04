import RBTree
import sys


def CreateTree():
    return RBTree.RedBlackTree()

def PrintResult(tree):
    print("filename :",fileName, file = outputFile)
    print("total :",tree.total_node(), file = outputFile)
    print("insert :", insertNum, file=outputFile)
    print("delete :",deleteNum, file = outputFile)
    print("miss :", missNum, file = outputFile)
    print("nb :",tree.black_node(), file = outputFile)
    print("bh :",tree.black_height(), file = outputFile)
    for node in tree.inorder_walk():
        print(str(node.key)[:-1], ('R' if node.color else 'B'), file = outputFile)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Ex )",sys.argv[0],"input.txt")
        exit()
    fileName = sys.argv[1]
    inputFile = open(fileName, 'r')
    outputFile = open('result.txt','w')

    insertNum = 0
    deleteNum = 0
    missNum = 0


    rbt = CreateTree()
    lines = inputFile.readlines()
    for line in lines:
        if line[0] is '0':
            PrintResult(rbt)
            inputFile.close()
            outputFile.close()
            exit()
        if line[0] is not '-':
            rbt.add(line)
            insertNum += 1
        elif line[0] is '-' :
            try:
                rbt.delete(rbt.search(line[1:]))
                deleteNum += 1
            except:
                print("There is no",line[1:], file = outputFile)
                missNum += 1
