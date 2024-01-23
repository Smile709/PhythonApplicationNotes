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
            file_content = file.read()
            notes = json.loads(file_content)
    except FileNotFoundError:
        pass
    return notes

def save_json(filename, notes):  # Сохранение заметок в файл
    with open(filename, 'w') as file:
        json.dump(notes, file, indent=2)

def add(notes, title, body): # Добавление новой заметки
    note_id = len(notes) + 1
    timestamp = get_current_timestamp()
    note = {'id': note_id, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(note)
    print(f'Заметка с ID {note_id} добавлена успешно.')

def edit(notes, note_id, title, body): # Редактирование заметки
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['body'] = body
            note['timestamp'] = get_current_timestamp()
            print(f'Заметка с ID {note_id} отредактирована успешно.')
            return
    print(f'Заметка с ID {note_id} не найдена.')

def delete(notes, note_id): # Удаление заметки
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print(f'Заметка с ID {note_id} удалена успешно.')
            return
    print(f'Заметка с ID {note_id} не найдена.')

def display(notes): # Вывод всех заметок
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['body']}, Дата: {note['timestamp']}")

def display_id(notes, note_id): # Вывод заметки по ID
    for note in notes:
        if note['id'] == note_id:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['body']}, Дата: {note['timestamp']}")
            return
    print(f'Заметка с ID {note_id} не найдена.')

def filter_notes_by_date(notes, date_str): # Фильтрация заметок по дате
    filtered_notes = [note for note in notes if note['timestamp'].startswith(date_str)]
    return filtered_notes

def get_current_timestamp(): # Получение текущей даты и времени в строковом формате
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

work_with_notes("notes.json")
