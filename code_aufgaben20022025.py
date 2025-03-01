import random

def main():
    # zahlen = [3, 7, 2, 9, 5]
    #
    # summe = 0
    # for zahl in zahlen:
    #     summe = summe + zahl
    #
    # print(summe)

    zahlen = [4, 7, 10, 23, 8, 6]
    gerade_zahlen = []

    for zahl in zahlen:
        if zahl % 2 == 0:
            gerade_zahlen.append(zahl)

    print(gerade_zahlen)

    zufällige_zahlen = []

    for _ in range(10):
        zufällige_zahlen.append(random.randint(1, 100))

    print(zufällige_zahlen)

if __name__ == "__main__":
    main()