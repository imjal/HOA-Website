import zillow_info
import sheet_transfer
import verify

def check(last_name, listName):
    last_name = str(last_name).lower()
    for name in listName:
        if last_name == str(name).lower():
            return True;

    return False

def main():
    values = sheet_transfer.getValues("A:H")
    for row in values:
        if len(row) > 5:
            owners = verify.findName(str(row[6]), row[7], "Peoria")
            if len(owners) > 0:
                names = owners.split()
                if not (check(row[2], names)):
                    print row[0], row[5]
            else:
                print row[0], row[5]


if __name__ == '__main__':
    main()