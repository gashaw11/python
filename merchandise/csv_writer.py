import csv

def write_csv(filename):
    with open(filename, 'w', newline = '') as file:
        writer = csv.writer(file)

        header = input("Enter header row")
        if header:
            writer.writerow(header.split(','))
        while True:
            row = input("Enter data row")
            if row.lower() == 'done':
                break
            writer.writerow(row.split(','))

if __name__=="__main__":
    filename = input("enter a file name")
    write_csv(filename)
    print("sucees")