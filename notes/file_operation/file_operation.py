import csv


def create_file(file_name):
    with open(file_name, "w", encoding='utf-8') as data:
        file_writer = csv.DictWriter(data, fieldnames=['id', 'title', 'body_note', 'date_time'])
        file_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8', newline='') as data:
        file_reader = csv.DictReader(data)
        return list(file_reader)
