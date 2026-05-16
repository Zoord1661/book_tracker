import json
from datetime import datetime

def load_books():
    """Загружает книги из файла"""
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    """Сохраняет книги в файл"""
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book(books):
    author = input("Автор: ")
    title = input("Название: ")

    # Проверка на дубликаты
    for book in books:
        if book['author'] == author and book['title'] == title:
            print("Эта книга уже есть в списке!")
            return

    # Ввод и валидация оценки
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Введите число от 1 до 5")
        except ValueError:
            print("Некорректный ввод")

    date = datetime.now().strftime("%d.%m.%Y")
    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    })
    save_books(books)
    print("Книга добавлена!")
    
def show_books(books):
    if not books:
        print("Список пуст")
        return
    for idx, book in enumerate(books):
        print(f"{idx+1}. {book['title']} ({book['author']}) - {book['rating']}⭐ ({book['date']})")

def show_average_rating(books):
    if not books:
        print("Нет книг для подсчета")
        return
    total = sum(book['rating'] for book in books)
    average = total / len(books)
    print(f"Средняя оценка: {average:.2f}⭐")

def show_authors_stats(books):
    stats = {}
    for book in books:
        author = book['author']
        if author in stats:
            stats[author] += 1
        else:
            stats[author] = 1
    for author, count in stats.items():
        print(f"{author}: {count} книг")

def delete_book(books):
    if not books:
        print("Список пуст")
        return
    show_books(books)
    try:
        idx = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= idx < len(books):
            del books[idx]
            save_books(books)
            print("Книга удалена")
        else:
            print("Неверный номер")
    except ValueError:
        print("Некорректный ввод")
