import csv


def fetch(file):
    with open(file, 'r', newline='') as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            for i in row:
                result.append(i.split(';'))
                try:
                    print(len(result[0]))
                    print(len(result[1]))
                    print(result)
                except IndexError:
                    continue


if __name__ == '__main__':
    fetch('')