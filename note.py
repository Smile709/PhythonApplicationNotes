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