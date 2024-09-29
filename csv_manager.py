import csv
import pandas as pd
from tabulate import tabulate

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
        
    def print_csv_as_table(self):
        df = pd.read_csv('data.csv')
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))


if __name__ == "__main__":
    csv_manager = CSVManager('data.csv')
    
#     csv_manager.print_csv_as_table()
#     print("Leer csv")
#     csv_manager.read_csv()

#     print("Leer csv por fila")
#     print(f"Estas son la columnas {csv_manager.get_headers()}")
#     column_name = input("Elija la columna: ")
#     value = input("Valor de la columna: ")
#     csv_manager.read_row_by_column_value(column_name, value)

#     print("Escribir una nueva fila")
#     data = []
#     i = 0
#     headers = csv_manager.get_headers()
#     for column in headers:
#         data.append(input(f"{column}: "))
    
#     csv_manager.write_new_row(data)

#     print("Comprobamos que este escrito:")
#     csv_manager.read_csv()
    