import random


def mystery_function(n):
    result = []
    for i in range(1, n + 1):
        temp = []
        for j in range(i):
            temp.append(random.randint(1, 9))
        if i % 2 == 0:
            temp.reverse()
        result.append(temp)
    return result


def transform_data(data):
    new_data = []
    for i, row in enumerate(data):
        if i % 2 == 0:
            new_data.append(sum(row))
        else:
            new_data.append(max(row) if row else 0)
    return new_data


def main():
    n = 5  # Zum Testen eine feste Größe
    data = mystery_function(n)
    transformed = transform_data(data)

    for row in data:
        print(row)
    print("Transformed Data:", transformed)


if __name__ == "__main__":
    main()
