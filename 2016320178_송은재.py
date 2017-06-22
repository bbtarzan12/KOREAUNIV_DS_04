import RBTree
import os


def create_tree():
    return RBTree.RedBlackTree()


def print_result(tree):
    print("filename :", select, file=outputFile)
    print("total :", tree.total_node(), file=outputFile)
    print("insert :", insertNum, file=outputFile)
    print("delete :", deleteNum, file=outputFile)
    print("miss :", missNum, file=outputFile)
    print("nb :", tree.black_node(), file=outputFile)
    print("bh :", tree.black_height(), file=outputFile)
    for node in tree.inorder_walk():
        print(node.key, ('R' if node.color else 'B'), file=outputFile)

def search_input_file():
    filenames = os.listdir('./input')
    return filenames

def search_and_print():
    isAdd = False
    if searchFile is None:
        print("put your search files in input folder ")
        exit()
    else:
        searchlines = searchFile.readlines()
        for sline in searchlines:
            svalue = int(sline)
            if svalue == 0:
                inputFile.close()
                outputFile.close()
                searchFile.close()
                print(outputFile.name)
                exit()
            snode = rbt.search(svalue)
            curr = snode.key
            if snode.key is None:
                rbt.add(svalue)
                snode = rbt.search(svalue)
                isAdd = True
            print(rbt.predecessor(snode).key,curr,rbt.successor(snode).key, file = outputFile)
            if isAdd:
                rbt.delete(snode)
                isAdd = False



if __name__ == "__main__":
    fileNames = os.listdir('./input')
    select = ''
    isSearch = False
    if fileNames is None:
        print("put your text files in input folder")
        exit()
    else:
        print('=====================')
        for filename in fileNames:
            print(filename)
        print('=====================')
        select = input('select input file (ex, input.txt) : ')
        isFind = False
        for filename in fileNames:
            if filename == select:
                isFind = True
        if isFind is False:
            print('There is no',select)
            exit()
    search = input('Do you want to use search?(y/n) : ')
    if search == 'y':
        isSearch = True
        searchFile = open('./search/search01.txt', 'r')
    inputFile = open('./input/'+select, 'r')
    outputFile = open('./result/'+select[:-4]+'_result.txt', 'w')

    insertNum = 0
    deleteNum = 0
    missNum = 0

    rbt = create_tree()
    lines = inputFile.readlines()
    for line in lines:
        value = int(line)
        if value == 0:
            if isSearch:
                search_and_print()
            else:
                print_result(rbt)
            inputFile.close()
            outputFile.close()
            print(outputFile.name)
            exit()
        if value > 0:
            rbt.add(value)
            insertNum += 1
        elif value < 0:
            try:
                rbt.delete(rbt.search(abs(value)))
                deleteNum += 1
            except:
                print("There is no", value, file=outputFile)
                missNum += 1
