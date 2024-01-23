import json

def work_with_notes(filename): #Бот программы (main функция)
    choice = show_menu()
    notes = read_json(filename)

    while (choice != 7):
        if choice == 1:
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            add(notes, title, body)
        elif choice == 2:
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            edit(notes, note_id, title, body)
        elif choice == 3:
            note_id = int(input("Введите ID заметки для удаления: "))
            delete(notes, note_id)
        elif choice == 4:
            display(notes)
        elif choice == 5:
            note_id = int(input("Введите ID для вывода нужной заметки: "))
            display_id(notes, note_id)
        elif choice == 6:
            date_str = input("Введите дату для фильтрации (в формате YYYY-MM-DD): ")
            filtered_notes = filter_notes_by_date(notes, date_str)
            display(filtered_notes)
        else:
            print("Неверная команда. Пожалуйста, введите корректную команду.")

        choice = show_menu()

    save_json(filename, notes)

def show_menu(): # Печатает меню выбора
    print('1. Добавить новую заметку', 
          '2. Редактировать заметку', 
          '3. Удалить заметку', 
          '4. Показать все заметки', 
          '5. Показать заметку по ID', 
          '6. Показать заметки за указанную дату', 
          '7. Закончить работу', sep='\n') 
    choice = int(input("Введите команду: "))
    return choice

def read_json(filename):
    print(f"Попытка чтения из файла: {filename}")
    notes = []
    try:
        with open(filename, 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        pass
    return notes

def save_json(filename, notes): # Сохранение заметок в файл
    with open(filename, 'w') as file:
        json.dump(notes, file)

work_with_notes("notes.json")

while True:
    command = input("Введите команду (add, edit, delete, list, filter, exit): ").lower()

    if command == 'exit':
            break
    elif command == 'add':
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            add_note(title, body)
    elif command == 'edit':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            edit_note(note_id, title, body)
    elif command == 'delete':
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
    elif command == 'list':
            display_notes()
    elif command == 'filter':
            date_str = input("Введите дату для фильтрации (в формате YYYY-MM-DD): ")
            filtered_notes = filter_notes_by_date(date_str)
            display_notes(filtered_notes)
    else:
            print("Неверная команда. Пожалуйста, введите корректную команду.")