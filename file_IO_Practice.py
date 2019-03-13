
import sys

"""
Check out logging files too

"""
def test_file(thing):
    #better way to open instead of file = file.open()
    with open("data.txt", 'a') as file:
        #write
        file.write(thing+"\n")
        #close
        file.close()

    
def show():
    with open("data.txt") as file:
        for line in file:
            print(line)



if __name__ == '__main__':

    if sys.argv[1].lower() == '--list':
        show()
    else:
        test_file(' '.join(sys.argv[1:]))
