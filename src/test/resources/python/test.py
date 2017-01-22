import  os
def main(b):
    with open('data\\test.txt','r') as testf:
        for line in testf:
            print line


def test(b):

    print(str(b));
    return  "success"

if __name__ == "__main__":
    main("gg")
