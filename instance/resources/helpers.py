import csv
import pathlib


def users_csv():
    return absolute_path('csv/users.csv')


def shops_csv():
    return absolute_path('csv/shops.csv')


def manufacturers_csv():
    return absolute_path('csv/shops.csv')


def absolute_path(file):
    return f'{pathlib.Path(__file__).parent.absolute()}/{file}'


def read_elements(file, build_fn):
    elements = []
    with open(file, newline='') as csv_file:
        reader = csv.reader(csv_file)
        csv_file.readline()
        for row in reader:
            elements.append(build_fn(row))
    return elements
