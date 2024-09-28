import csv

class CSVManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                print(row)

    def read_row_by_column_value(self, column_name, value):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row[column_name] == value:
                    return print(row)
        return print(None)
    
    def write_new_row(self, data):
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        print("New row added")

    def get_headers(self):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            return next(reader)


if __name__ == "__main__":
    csv_manager = CSVManager('data.csv')
    print(csv_manager.get_headers())
    