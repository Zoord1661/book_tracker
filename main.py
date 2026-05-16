from utils import *

def main():
    books = load_books()
    while True:
        print("\n=== Трекер прочитанных книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Средняя оценка")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            show_books(books)
        elif choice == '3':
            show_average_rating(books)
        elif choice == '4':
            show_authors_stats(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
