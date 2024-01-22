import os

def work_with_notes(filename): #Бот программы (main функция)
    choice = show_menu()
    notes=read_json(filename)
    #app = AppNotes()
    #app.load_notes()

    while (choice!=6):
        #command = input("Введите команду (add, edit, delete, list, filter, exit): ").lower()

        if choice == 1:
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            add(title, body)
        elif choice == '2':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            edit(note_id, title, body)
        elif choice == '3':
            note_id = int(input("Введите ID заметки для удаления: "))
            delete(note_id)
        elif choice == '4':
            display()
        elif choice == '5':
            date_str = input("Введите дату для фильтрации (в формате YYYY-MM-DD): ")
            filtered_notes = filter_notes_by_date(date_str)
            display(filtered_notes)
        else:
            print("Неверная команда. Пожалуйста, введите корректную команду.")

def show_menu(): # Печатает меню выбора
    print('1. Добавить новую заметку', 
          '2. Редактировать заметку', 
          '3. Удалить заметку', 
          '4. Показать все заметки', 
          '5. Показать заметки за указанную дату', 
          '6. Закончить работу', sep= '\n') 
    choice=int(input("введите команду: "))
    return choice