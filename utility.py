'''
Utility to print file contents in given format
Only single commandline option is allowed from -l, -c, -w, -n, -a
For help, use option -h
'''
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='File Utility')
    g = parser.add_mutually_exclusive_group()
    g.add_argument('-l', metavar='filename', required=False,
                        help='Display number of lines present in input file')
    g.add_argument('-c', metavar='filename', required=False,
                        help='Display number of character present in input file')
    g.add_argument('-w', metavar='filename', required=False,
                        help='Display number of words in a input file')
    
    g.add_argument('-n', metavar='filename', required=False,
                        help='Display only numeric value in input file')
    g.add_argument('-a', metavar='filename', required=False,
                        help='Display only alphabets in input file')
    
    args = parser.parse_args()

    try:
        if args.l:
            with open(args.l, 'r') as fp:
                x = len(fp.readlines())
                print(x, ' ', str(args.l))

        elif args.c:
            with open(args.c, 'r') as fp:
                data = fp.read()
                count = 0
                for c in data:
                    if c.isalpha():
                        count += 1
                print(count, ' ', str(args.c))

        elif args.w:
            with open(args.w, 'r') as fp:
                data = fp.read()
                count = len(data.split())
                print(count, ' ', str(args.w))
        
        elif args.n:
            with open(args.n, 'r') as fp:
                data = fp.read()
                count = 0
                for c in data:
                    if c.isnumeric():
                        print(c, end='')

                print(' ', str(args.n))
        
        elif args.a:
            with open(args.a, 'r') as fp:
                data = fp.read()
                count = 0
                for c in data:
                    if c.isalpha():
                        print(c, end='')

                print(' ',str(args.a))
        
    except (FileNotFoundError, IOError):
        print("File not found. Please provide valid filename")
    except:
        print("Something went wrong")