import os

# Путь к каталогу с заметками
notes_directory = "notes"

# Функция для создания новой заметки
def create_note():
    note_text = input("Введите текст заметки: ")
    note_filename = os.path.join(notes_directory, f"note_{len(os.listdir(notes_directory)) + 1}.txt")
    
    with open(note_filename, "w") as note_file:
        note_file.write(note_text)
    
    print(f"Заметка сохранена в файле: {note_filename}")

# Функция для чтения списка заметок
def list_notes():
    notes = os.listdir(notes_directory)
    if not notes:
        print("Список заметок пуст.")
    else:
        print("Список заметок:")
        for note in notes:
            print(note)

# Функция для просмотра заметки
def view_note():
    note_name = input("Введите имя заметки для просмотра: ")
    note_filename = os.path.join(notes_directory, note_name)
    
    if os.path.exists(note_filename):
        with open(note_filename, "r") as note_file:
            note_text = note_file.read()
            print("Содержимое заметки:")
            print(note_text)
    else:
        print(f"Заметка '{note_name}' не найдена.")

# Другие функции (редактирование и удаление) могут быть добавлены аналогичным образом.

# Основной цикл программы
if __name__ == "__main__":
    if not os.path.exists(notes_directory):
        os.makedirs(notes_directory)
    
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Просмотреть заметку")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            create_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            view_note()
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
