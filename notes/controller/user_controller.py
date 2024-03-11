import notes.function.note_function as nf
import notes.file_operation.file_operation as fo

from os.path import exists

from notes.interface.user_interface import com


def app():
    com()

    while True:
        command = input("\nВведите команду: ")
        if command == "a":
            if not exists("../notes.csv"):
                fo.create_file("../notes.csv")
            nf.add_notes("../notes.csv")
        elif command == "l":
            nf.list_notes("../notes.csv")
        elif command == "e":
            edit_note_id = int(input("Введите id заметки для редактирования: "))
            nf.edit_note("notes.csv", edit_note_id)
        elif command == "d":
            delete_note_id = int(input("Введите id заметки для удаления: "))
            nf.delete_notes("../notes.csv", delete_note_id)

        elif command == "q":
            break
        else:
            print("Некорректная команда. Введите команду заново.")
            com()



