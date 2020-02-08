def open_ged(ged_name):
    try:
        fp = open(ged_name, 'r')
    except FileNotFoundError:
        print(f'File cannot be opened:{ged_name}')
    else:
        tags = {"0": ["HEAD", "NOTE", "INDI", "FAM", "TRLR"],
                "1": ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],
                "2": ["DATE"]}

        for line in fp:
            print(f'-->{line.strip()}')
            word = line.split()
            # 1 SEX M
            if word[0] in tags and word[1] in tags[word[0]]:
                print(f'<--{word[0]}|{word[1]}|Y|{" ".join(word[2:])}')
            # 0 I01 INDI
            elif word[0] in tags and word[-1] in tags[word[0]]:
                print(f'<--{word[0]}|{word[-1]}|Y|{word[1]}')
            else:
                print(f'<--{word[0]}|{word[1]}|N|{" ".join(word[2:])}')


def main():
    # ged_name1 = 'proj02test.ged'
    # open_ged(ged_name1)
    # ged_name2 = 'GEDCOM_HW01.txt'
    # open_ged(ged_name2)
    ged_name3 = 'proj03_testfile_hogwarts.ged'
    open_ged(ged_name3)


if __name__ == '__main__':
    main()