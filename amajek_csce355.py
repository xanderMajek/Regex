#import re
import sys
import copy


def main():

    # Inputs - (Solutions start on line 236.)
    if sys.argv[1] == '-help':

        print('--no-op, --empty, --has-epsilon, --has-nonepsilon \n')
        print('--infinite, --starts-with a, --ends-with a, --reverse \n')
        print('--prefixes, --suffixes, --b-before-a, --drop-one, --strip \n')
        sys.exit()

    elif sys.argv[1] == "--no-op":

        while True:
            #  input
            try:
                regex = input()
            except EOFError:
                break

            #  solution and print :D
            print(solveNoOp(regex))

    elif sys.argv[1] == "--empty":

        while True:
            #  input
            try:
                regex = input()
            except EOFError:
                break

            #  solution
            if solveEmpty(makeTree(regex)):
                print("yes")
            else:
                print("no")

    elif sys.argv[1] == "--has-epsilon":

        while True:
            #  input
            try:
                regex = input()
            except EOFError:
                break

            #  solution
            if solveEpsilon(makeTree(regex)):
                print("yes")
            else:
                print("no")

    elif sys.argv[1] == "--has-nonepsilon":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break

            #  solution
            if solveNonepsilon(makeTree(regex)):
                print("yes")
            else:
                print("no")

    elif sys.argv[1] == "--infinite":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break

            #  solution
            if solveInfinite(makeTree(regex)):
                print("yes")
            else:
                print("no")

    elif sys.argv[1] == "--starts-with":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break

            #  solution
            if solveStartsWith(makeTree(regex), sys.argv[2]):
                print("yes")
            else:
                print("no")

    elif sys.argv[1] == "--ends-with":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break

            #  solution
            if solveEndsWith(makeTree(regex), sys.argv[2]):
                print("yes")
            else:
                print("no")

    elif sys.argv[1] == "--reverse":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break
            #  solution
            headNode = makeTree(regex)
            makeReverse(headNode)

            line = ""
            #  print
            for element in headNode.printPreorder(headNode):
                line += element
            print(line)

    elif sys.argv[1] == "--prefixes":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break
            #  solution
            headNode = makeTree(regex)
            makePrefixes(headNode)

            line = ""
            #  print
            for element in headNode.printPreorder(headNode):
                line += element
            print(line)

    elif sys.argv[1] == "--suffixes":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break
            #  solution
            headNode = makeTree(regex)
            makeSuffixes(headNode)

            line = ""
            #  print
            for element in headNode.printPreorder(headNode):
                line += element
            print(line)

    elif sys.argv[1] == "--b-before-a":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break
            #  solution
            headNode = makeTree(regex)
            b_before_a(headNode)

            line = ""
            #  print
            for element in headNode.printPreorder(headNode):
                line += element
            print(line)

    elif sys.argv[1] == "--drop-one":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break
            #  solution
            headNode = makeTree(regex)
            makeDropOne(headNode)

            line = ""
            #  print
            for element in headNode.printPreorder(headNode):
                line += element
            print(line)

    elif sys.argv[1] == "--strip":

        while True:

            #  input
            try:
                regex = input()
            except EOFError:
                break
            #  solution
            headNode = makeTree(regex)
            strip(headNode, sys.argv[2])

            line = ""
            #  print
            for element in headNode.printPreorder(headNode):
                line += element
            print(line)

# Solutions


def solveNoOp(regex):

    stack = []

    for element in range(0, len(regex)):

        if regex[element] != "+" and regex[element] != "." and regex[element] != "*":

            # add to array
            stack.append(regex[element])

        elif regex[element] == "+" or regex[element] == ".":

            # pop twice

            pop1 = stack[-1]
            stack.pop()
            pop2 = stack[-1]
            stack.pop()
            temp = regex[element] + pop2 + pop1
            stack.append(temp)

        elif regex[element] == "*":

            # pop once

            pop1 = stack[-1]
            stack.pop()
            temp = regex[element] + pop1
            stack.append(temp)

    # reconstitute string

    prefix = ''
    for element in stack:
        prefix += element

    return(prefix)


def solveEmpty(node):

    if node.typeNode == ".":

        if solveEmpty(node.rchild) or solveEmpty(node.lchild):
            return True
        else:
            return False

    elif node.typeNode == "+":

        if solveEmpty(node.rchild) and solveEmpty(node.lchild):
            return True
        else:
            return False

    elif node.typeNode == "*":

        return False

    elif node.typeNode == "/":

        return True

    else:

        return False


def solveEpsilon(node):

    if node.typeNode == ".":

        if solveEpsilon(node.lchild) and solveEpsilon(node.rchild):
            return True
        else:
            return False

    elif node.typeNode == "+":

        if solveEpsilon(node.lchild) or solveEpsilon(node.rchild):
            return True
        else:
            return False

    elif node.typeNode == "*":

        return True

    elif node.typeNode == "/":

        return False

    else:

        return False


def solveNonepsilon(node):

    if solveEmpty(node) and solveEpsilon(node) == False:
        return False
    else:
        result = False
        for element in node.printPreorder(node):
            if element != "*" and element != "." and element != "/":
                result = True
        return result


def solveInfinite(node):

    if node.typeNode == ".":

        if (solveEmpty(node.lchild) == False and solveInfinite(node.rchild)) or (
                solveInfinite(node.lchild) and solveEmpty(node.rchild) == False):
            return True
        else:
            return False

    elif node.typeNode == "+":

        if solveInfinite(node.rchild) or solveInfinite(node.lchild):
            return True
        else:
            return False

    elif node.typeNode == "*":

        if solveNonepsilon(node):
            return True

    elif node.typeNode == "/":

        return False

    else:

        return False


def solveStartsWith(node, alphaNum):

    if node.typeNode == "/":

        return False

    elif node.typeNode == alphaNum:

        return True

    elif node.typeNode == "+":

        if solveStartsWith(
                node.lchild,
                alphaNum) or solveStartsWith(
                node.rchild,
                alphaNum):
            return True
        else:
            return False

    elif node.typeNode == ".":

        if (solveStartsWith(node.lchild, alphaNum) and solveEmpty(node.rchild) == False) or (
                solveEpsilon(node.lchild) and solveStartsWith(node.rchild, alphaNum)):
            return True
        else:
            return False

    elif node.typeNode == "*":

        if solveStartsWith(node.lchild, alphaNum):
            return True
        else:
            return False

    else:

        return False


def solveEndsWith(node, alphaNum):

    if node.typeNode == "/":

        return False

    elif node.typeNode == alphaNum:

        return True

    elif node.typeNode == "+":

        if solveEndsWith(
                node.lchild,
                alphaNum) or solveEndsWith(
                node.rchild,
                alphaNum):
            return True
        else:
            return False

    elif node.typeNode == ".":

        if (solveEndsWith(node.rchild, alphaNum) and solveEmpty(node.lchild) == False) or (
                solveEpsilon(node.rchild) and solveEndsWith(node.lchild, alphaNum)):
            return True
        else:
            return False

    elif node.typeNode == "*":

        if solveEndsWith(node.lchild, alphaNum):
            return True
        else:
            return False

    else:

        return False


def makeReverse(node):

    if node.typeNode == "+":

        makeReverse(node.lchild)
        makeReverse(node.rchild)

    elif node.typeNode == ".":

        nodeLeft = node.lchild
        nodeRight = node.rchild

        node.set_leftchild(nodeRight)
        node.set_rightchild(nodeLeft)

        makeReverse(node.lchild)
        makeReverse(node.rchild)

    elif node.typeNode == "*":

        makeReverse(node.lchild)

    else:

        return


def makePrefixes(node):

    if node.typeNode == "/":

        return

    elif node.typeNode == "+":

        makePrefixes(node.lchild)
        makePrefixes(node.rchild)

    elif node.typeNode == ".":

        if solveEmpty(node.rchild):

            node.typeNode = "/"
            node.lchild = None
            node.rchild = None

        else:

            # convert . to +
            node.typeNode = "+"

            # copy legs
            temp0 = node.lchild
            temp1 = node.rchild

            temp2 = copy.deepcopy(node.lchild)

            #make . node
            nodeInsert = Node(".")

            # its legs are s and t'
            nodeInsert.set_leftchild(temp2)

            makePrefixes(temp1)

            nodeInsert.set_rightchild(temp1)

            # new right leg is .
            node.set_rightchild(nodeInsert)

            # new left leg is s'
            makePrefixes(temp0)
            node.set_leftchild(temp0)

    elif node.typeNode == "*":

        if solveEmpty(node.lchild):

            node.lchild.typeNode = "/"
            node.lchild.lchild = None
            node.lchild.rchild = None

        else:

            # make * in s*s'.
            insertNode1 = Node("*")

            # s
            insertNode2 = Node(node.lchild.typeNode)
            insertNode2.set_leftchild(copy.deepcopy(node.lchild.lchild))
            insertNode2.set_rightchild(copy.deepcopy(node.lchild.rchild))

            # *'s left leg becomes s
            temp = copy.deepcopy(node.lchild)
            insertNode1.set_leftchild(temp)

            # current node becomes .
            node.typeNode = "."

            # current node left leg become *
            node.set_leftchild(insertNode1)

            # current node's right leg becomes s'

            makePrefixes(insertNode2)

            node.set_rightchild(insertNode2)

    else:

        # copy c
        nodeInsert = Node(node.typeNode)
        nodeInsert.set_leftchild(node.lchild)
        nodeInsert.set_rightchild(node.rchild)

        # insert
        node.lchild = nodeInsert

        # alter node
        node.typeNode = "+"

        # add /*
        node.rchild = Node("*")
        node.rchild.lchild = Node("/")


def makeSuffixes(node):

    makeReverse(node)
    makePrefixes(node)
    makeReverse(node)


def b_before_a(node):

    if node.typeNode == "/":

        return

    elif node.typeNode == "a":

        temp = copy.deepcopy(node)
        node.typeNode = "."
        node.set_leftchild(Node("b"))
        node.set_rightchild(temp)

    elif node.typeNode == "+":

        b_before_a(node.lchild)
        b_before_a(node.rchild)

    elif node.typeNode == ".":

        b_before_a(node.lchild)
        b_before_a(node.rchild)

    elif node.typeNode == "*":

        b_before_a(node.lchild)

    else:

        return


def makeDropOne(node):

    if node.typeNode == "/":

        return

    elif node.typeNode == "+":

        makeDropOne(node.lchild)
        makeDropOne(node.rchild)

    elif node.typeNode == ".":

        # convert . to +
        node.typeNode = "+"

        # copy legs
        temp0 = node.lchild
        temp1 = node.rchild

        temp2 = copy.deepcopy(node.lchild)
        temp3 = copy.deepcopy(node.rchild)

        # make . node x2
        nodeInsert1 = Node(".")
        nodeInsert2 = Node(".")

        # nodeInsert1 legs are s' and t

        # s'
        makeDropOne(temp0)
        nodeInsert1.set_leftchild(temp0)
        # t
        nodeInsert1.set_rightchild(temp3)

        # nodeInsert2 legs are s and t'

        # s
        nodeInsert2.set_leftchild(temp2)
        # t'
        makeDropOne(temp1)
        nodeInsert2.set_rightchild(temp1)

        # new legs for + node
        node.set_leftchild(nodeInsert1)
        node.set_rightchild(nodeInsert2)

    elif node.typeNode == "*":

        # convert * to .
        node.typeNode = "."

        # copy leg
        temp0 = node.lchild
        temp1 = copy.deepcopy(node.lchild)

        # node -> node1 and node2
        # node2 -> node 3 and temp0 (makeDropOne(temp0))
        insertNode1 = Node("*")
        insertNode2 = Node(".")
        insertNode3 = Node("*")

        # s
        insertNode1.set_leftchild(temp1)
        # s'
        makeDropOne(temp0)
        insertNode2.set_leftchild(temp0)
        # *
        insertNode2.set_rightchild(insertNode3)
        # s
        insertNode3.set_leftchild(temp1)

        node.set_leftchild(insertNode1)
        node.set_rightchild(insertNode2)

    else:

        node.typeNode = "*"
        insertNode = Node("/")
        node.set_leftchild(insertNode)


def strip(node, alphaNum):

    if node.typeNode == "/":
        return
    elif node.typeNode == "+":

        strip(node.lchild, alphaNum)
        strip(node.rchild, alphaNum)

    elif node.typeNode == ".":

        if solveEpsilon(node.lchild):

            # convert . to +
            node.typeNode = "+"

            # copy legs
            temp0 = copy.deepcopy(node.lchild)
            temp1 = copy.deepcopy(node.rchild)

            # node -> node1
            insertNode = Node(".")

            # s'
            strip(temp0, alphaNum)
            insertNode.set_leftchild(temp0)

            # t'
            strip(node.rchild, alphaNum)

            # t
            insertNode.set_rightchild(temp1)

            # .
            node.set_leftchild(insertNode)

        else:

            strip(node.lchild, alphaNum)

    elif node.typeNode == "*":

        # convert * to .
        node.typeNode = "."

        # copy leg
        temp0 = copy.deepcopy(node.lchild)
        temp1 = copy.deepcopy(node.lchild)

        # node -> node1 (strip()) and node2
        # node2 -> temp1
        strip(temp0, alphaNum)
        insertNode2 = Node("*")

        # *
        node.set_leftchild(temp0)

        # *
        node.set_rightchild(insertNode2)

        # s
        insertNode2.set_leftchild(temp1)

    elif node.typeNode == alphaNum:

        node.typeNode = "*"
        insertNode = Node("/")
        node.set_leftchild(insertNode)

    else:
        node.typeNode = "/"


def makeTree(regex):

    stack = []

    for element in regex:

        elementNode = Node(element)

        if element != "+" and element != "." and element != "*":

            stack.append(elementNode)

        elif element == "+" or element == ".":

            pop1 = stack[-1]
            pop2 = stack[-2]
            elementNode.set_leftchild(pop2)
            elementNode.set_rightchild(pop1)
            stack.pop()
            stack.pop()
            stack.append(elementNode)

        elif element == "*":
            pop = stack[-1]
            elementNode.set_leftchild(pop)
            stack.pop()
            stack.append(elementNode)

    return stack[0]


class Node:

    def __init__(self, typeNode: str):
        self.typeNode = typeNode
        self.lchild = None
        self.rchild = None

    def set_leftchild(self, node):
        self.lchild = node

    def set_rightchild(self, node):
        self.rchild = node

    def printPreorder(self, node):

        stack = []

        if node:

            stack.append(node.typeNode)
            stack = stack + self.printPreorder(node.lchild)
            stack = stack + self.printPreorder(node.rchild)

        return stack


if __name__ == "__main__":

    main()
