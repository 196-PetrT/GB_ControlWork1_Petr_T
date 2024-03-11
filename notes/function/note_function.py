import csv
import os
from datetime import datetime

import notes.file_operation.file_operation as fo


def list_notes(file_name):
    if os.path.exists(file_name):
        with open(file_name, mode="r", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file)
            for note in file_reader:
                print(note)


def save_notes(file_name, array):
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        file_writer = csv.DictWriter(data, fieldnames=['id', 'title', 'body_note', 'date_time'])
        file_writer.writeheader()
        file_writer.writerows(array)


def add_notes(file_name):
    notes = fo.read_file(file_name)
    note = {'id': len(notes) + 1, 'title': input("Введите заголовок заметки: "), 'body_note':
        input("Введите текст заметки: "), 'date_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    notes.append(note)
    save_notes(file_name, notes)
    print("Заметка успешно добавлена!")


def edit_note(file_name, note_id):
    notes = fo.read_file(file_name)
    for note in notes:
        # if note['id'] != str(note_id):

        if note['id'] == str(note_id):
            print("редактируем выбранную заметку")
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body_note'] = input("Введите новый текст заметки: ")
            note['date_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            save_notes(file_name, notes)
            print("Заметка успешно отредактирована!")
            return
    print("Некорректный id")


def delete_notes(file_name, note_id):
    notes = fo.read_file(file_name)
    for note in notes:
        if note['id'] != str(note_id):
            print(f"Заметка с id: {note_id} не найдена!")
        if note['id'] == str(note_id):
            notes = [note for note in notes if note['id'] != str(note_id)]
            save_notes(file_name, notes)
            print("Заметка удалена!")
            return
