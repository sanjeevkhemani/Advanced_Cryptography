def part1(flag):
    if flag == "0":
        print("Enter a string")
        str = input()
        print("Converted List of Characters: ")
        return [char for char in str]
    elif flag == "1":
        print("Enter chars one at a time, and STOP when done")
        str = ""
        chr = 'y'
        while len(chr) == 1:
            chr = input()
            if len(chr) == 1:
                str += chr
        print("Converted String: ")
        return str
    else:
        return "EXIT"


def part2(flag):
    if flag == "0":
        print("Enter ascii values one at a time, and 256 when done")
        chrs = []
        var = 13
        while var >= 0 and var <256:
            try:
                var = int(input())
                if var >= 0 and var <256:
                    chrs.append(chr(var))
            except:
                break
        print("Converted List of Characters: ")
        return chrs
    elif flag == "1":
        print("Enter chars one at a time, and STOP when done")
        ascii = []
        char = 'y'
        while len(char) == 1:
            char = input()
            if len(char) == 1:
                ascii.append(ord(char))
        print("Converted ASCII Codes: ")
        return ascii
    else:
        return "EXIT"


def part3(flag):
    if flag == "0":
        print("Enter ascii values one at a time, and 256 when done")
        ascii = []
        bnry = []
        var = 13
        while var >= 0 and var <256:
            try:
                var = int(input())
                if var >= 0 and var <256:
                    bnry.append(bin(var))
            except:
                break
        print("Converted Binary Values: ")
        return bnry
    elif flag == "1":
        print("Enter binary one at a time, and STOP when done")
        ascii = []
        bnry = []
        bnr = 1101
        while True:
            try:
                bnr = input()
                var = int(bnr, 2)
                if var >= 0 and var <256:
                    ascii.append(var)
                else:
                    break
            except:
                break
        print("Converted ASCII Codes: ")
        return ascii
    else:
        return "EXIT"


print("Choose Converter\n[1] STRING \t<-> LIST of CHARS Converter")
print("[2] ASCII CODES <-> LIST of CHARS Converter")
print("[3] ASCII CODES <-> BINARY VALUES Converter\n[*] Any Other Value to Quit")
choice = input()
print(choice)

if choice == "1":
    print("Choose Option\n[0] STRING -> LIST of CHARS")
    print("[1] LIST of CHARS -> STRING\n[*] Any Other Value to Exit")
    flag = input()
    print(flag)
    print(part1(flag))
elif choice == "2":
    print("Choose Option\n[0] ASCII CODES -> LIST of CHARS")
    print("[1] LIST of CHARS -> ASCII CODES\n[*] Any Other Value to Exit")
    flag = input()
    print(flag)
    print(part2(flag))
elif choice == "3":
    print("Choose Option\n[0] ASCII CODES -> BINARY VALUES")
    print("[1] BINARY VALUES -> ASCII CODES\n[*] Any Other Value to Exit")
    flag = input()
    print(flag)
    print(part3(flag))
else:
    print("QUIT")
