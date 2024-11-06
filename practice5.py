def drawSquare(size):
    if size<1:
        print("Invalid size")
    elif size==1:
        print("□")
    else:
        print("┌" + ("─"*(size-1)) + "┐")
        for i in range(size-((size//2)+1)):
            print("│" + (" "*(size-1)) + "│")
        print("└" + ("─"*(size-1)) + "┘")
drawSquare(int(input("Input the size you want the square to be: ")))