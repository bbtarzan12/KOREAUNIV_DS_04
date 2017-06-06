import RBTree

f = open('input.txt','r')
lines = f.readlines()
rbt = RBTree.RedBlackTree()
for line in lines:
    if line[0] is '0':
        total = 0
        nb = 0
        for key in rbt.inorder_walk():
            total += 1
            if key.color is False:
                nb += 1
        print("total :",total)
        print("bh :",rbt.black_height())
        print("nb :",nb)
        f.close()
        break
    if line[0] is not '-':
        rbt.add(line)
    elif line[0] is '-' :
        try:
            rbt.delete(rbt.search(line[1:]))
        except:
            print("There is no",line[1:])