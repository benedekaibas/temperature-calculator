import csv
def load_file(filename: str = "") -> list:
    #  OPENS A CSV FILE #
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data 

def get_values_more_30(column: str = "") -> bool:
    # Returns true if the column contains wage more than 30 #
    result = False 
    col_values = []
    index = COLS.index(column)
    for row in ROWS:
        col_values.append(row)

def main():
    data = load_file(filename = "wages_by_education.csv")
    global COLS #global variable that will be accessable in other functions too 
    global ROWS
    COLS = data[0]
    ROWS = data[1:] #everything starting with index 1 and only skipping the 0 row
    print(COLS)
    print(ROWS)

if __name__ == "__main__":
    main()








