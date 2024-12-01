import re
import library_class


def main() -> None:
    """Основное меню программы."""
    library = library_class.Library()
    print('Добро пожаловать в консольное приложение "Библиотека"!', 'Что вы хотите сделать?', sep='\n')
    while True:
        print('1. Добавить книгу',
              '2. Удалить книгу',
              '3. Поиск книги',
              '4. Показать все книги',
              '5. Изменить статус книги',
              '6. Выйти', sep='\n')
        try:
            answer: int = int(input('Введите число: '))
            match answer:
                case 1:
                    print('Пожалуйста введите название книги, имя автора и год.')
                    try:
                        title: str = input('Название: ')
                        author: str = input('Автор(Фххххх И.О.): ')
                        if not re.match(r'^[А-ЯЁA-Z|][а-яё|a-z]+? ([А-ЯЁ|A-Z]\.[А-ЯЁ|A-Z]\.)?$', author):
                            raise ValueError('Введите корректное имя автора, согласно шаблону "Фххххх И.О."')
                        year: int = int(input('Год: '))
                        if 2024 < year or year < 0:
                            raise ValueError('Год должен быть положительным целым числом от 0 до 2024')
                        print(library.add_book(title, author, year))
                    except ValueError as e:
                        print(f'Ошибка! {e}')

                case 2:
                    print('Введите id книги, которую хотите удалить.')
                    try:
                        id_book: int = int(input('id: '))
                        if id_book < 0:
                            raise ValueError('id должен быть положительным целым числом')
                        print(library.delete_book(id_book))
                    except ValueError as e:
                        print(e)
                case 3:
                    query: str | int = input('Вы можете искать книгу по названию, автору или году. Введите запрос: ')
                    result: list | str = library.search_book(query)
                    if isinstance(result, list):
                        print('Книги найденные по вашему запросу:')
                        for el in result:
                            print(', '.join([f'{k}-{v}' for k, v in el.items()]))
                    else:
                        print(result)
                case 4:
                    result: list | str | Exception = library.get_all_books()
                    if isinstance(result, Exception | str):
                        print(f'Возникла ошибка: {result}')
                    elif isinstance(result, list):
                        if result:
                            for el in result:
                                print(', '.join([f'{k}-{v}' for k, v in el.items()]))
                        else:
                            print(f'Не было найдено книг в библиотеке')
                case 5:
                    print('Введите id книги и ее статус (В наличии/Выдана).')
                    try:
                        id_book = int(input('id: '))
                        if int(id_book) < 0:
                            raise ValueError('id должен быть положительным целым числом')
                        status = input('Статус: ')
                        if status not in ('В наличии', 'Выдана'):
                            raise ValueError('Введите корректный статус (В наличии/Выдана)')
                        result: Exception | str | bool = library.change_status(id_book, status)
                        if result is True:
                            print(f'Статус книги c id: {id_book} успешно изменен на {status}')
                        elif isinstance(result, Exception | str):
                            print(f'Не удалось изменить статус книги. Ошибка: {result}')
                        elif result is False:
                            print(f'Не удалось изменить статус книги. Книга с id: {id_book} не найдена')
                    except ValueError as e:
                        print(f'Ошибка! {e}')
                case 6:
                    print('До скорых встреч!')
                    break
                case _:
                    raise ValueError
        except ValueError as e:
            print(f'Некорректный ввод. Пожалуйста, введите ЧИСЛО от 1 до 6. Ошибка: {type(e)}')


if __name__ == '__main__':
    main()
