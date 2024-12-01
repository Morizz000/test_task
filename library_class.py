import json


class Library:
    """Класс описывающий библиотеку. Имеет 7 методов и 2 атрибута.
    Методы: save_update_in_file, change_status, get_all_books, search_book, delete_book, add_book, read_data_in_json.
    Атрибуты: self.filename - содержит имя json файла для хранения данных, self.books - список хранящий текущие книги"""
    def __init__(self):
        self.filename: str = 'library.json'
        self.books: list = self.read_data_in_json()

    def save_update_in_file(self) -> Exception | bool:
        """Обновляет содержимое файла используя атрибут self.books и контекстный менеджер, ничего не принимает на вход,
        возвращает True, если не возникло исключений при чтении файла, иначе возвращает объект исключения."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.books, file, ensure_ascii=False, indent=2)
                return True
        except Exception as e:
            return e

    def read_data_in_json(self) -> list | Exception | str:
        """Читает содержимое файла с помощью контекстного менеджера. Ничего не принимает на вход.
        Возвращает результат чтения или исключение, если оно возникло."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                result = json.load(file)
                return result
        except json.JSONDecodeError:
            return f'Библиотека пустая.'
        except Exception as e:
            return e

    def add_book(self, title: str, author: str, year: int) -> str:
        """Добавляет книгу в json файл. Принимает на вход название, автор, год. Возвращает результат работы функции:
        книга была добавлена/книга не была добавлена. Присваивает уникальный id книге и статус "В наличии",
        Использует функцию save_update_in_file для сохранения изменений."""
        if isinstance(self.books, str):
            id_book: int = 0
            self.books: list = []
        elif isinstance(self.books, Exception):
            return f'При чтении файла произошла ошибка. {type(self.books)}'
        else:
            id_book: int = self.books[-1]['id'] + 1
        status_book: str = 'В наличии'
        self.books.append({'id': id_book, 'title': title, 'author': author, 'year': int(year), 'status': status_book})
        result: bool | Exception | str = self.save_update_in_file()
        if isinstance(result, Exception):
            return f'Книга "{title}" не была добавлена. Ошибка: {type(result)}'
        return f'Книга "{title}" успешно добавлена!'

    def delete_book(self, id_book: int) -> str:
        """Удаляет книгу из json файла. Принимает на вход id книги. Возвращает строку с результатми работы функции:
        книга не удалена ошибка/книга удалена/книга не найдена. Использует функцию read_data_in_json для выгрузки данных
        из файла и функцию save_update_in_file для обновления файла."""
        all_books: list | Exception | str = self.read_data_in_json()
        if isinstance(all_books, str | Exception):
            return f'Книга с id {id_book} не была удалена. Ошибка: {all_books}'
        for idx, book in enumerate(all_books):
            if book['id'] == id_book:
                del_book: dict = all_books.pop(idx)
                self.books: list = all_books
                result: bool | Exception = self.save_update_in_file()
                if isinstance(result, Exception):
                    return f'Книга с id: {id_book} не была удалена. Ошибка: {type(result)}'
                return f'Книга "{del_book['title']}" была успешно удалена!'
        return f'Книга c id: {id_book} не была найдена в библиотеке.'

    def search_book(self, query: str | int) -> str | list:
        """Находит книгу по запросу. На вход принимает год|автор|название. Использует функцию read_data_in_json для
         чтения из файла. Возвращает список книг или сообщение, что книга не надена."""
        all_books: list | Exception | str = self.read_data_in_json()
        if isinstance(all_books, str | Exception):
            return f'Книга не была найдена, ошибка: {all_books}'
        result: list = []
        for el in all_books:
            if query in (el['title'], el['author'], str(el['year'])):
                result.append(el)
        if result:
            return result
        return f'Не нашли книг по вашему запросу: {query}.'

    def get_all_books(self) -> Exception | list | str:
        """Показывает содержимое файла. Для чтения файла использует функцию read_data_in_json."""
        result: list | Exception | str = self.read_data_in_json()
        return result

    def change_status(self, id_book: int, status: str) -> Exception | bool | str:
        """Меняет статус у книги. Принимает id книги и ее новый статус(Выдана|В наличии). Возващает объект исключения,
        если возникла ошибка при чтении файла или добавлении записи в файл. Использует функцию read_data_in_json для
        чтения и save_update_in_file для обновления файла."""
        all_books: list | Exception | str = self.read_data_in_json()
        if isinstance(all_books, str | Exception):
            return all_books
        for el in all_books:
            if el['id'] == id_book:
                el['status']: str = status
                self.books: list = all_books
                res: bool | Exception = self.save_update_in_file()
                return res
        return False
