Данное консольное приложение предназначено для управления библиотекой книг. Оно позволяет пользователям добавлять, удалять, искать и отображать книги, а также изменять их статусы. 
Каждая книга имеет уникальный идентификатор, название, автора, год издания и статус.

Приложение предоставляет следующие функции: 

-Добавление книги: Пользователь может ввести название, автора и год издания книги, после чего она будет добавлена в библиотеку с уникальным идентификатором и статусом "в наличии".

-Удаление книги: Пользователь может удалить книгу, введя её уникальный идентификатор.

-Поиск книги: Пользователь может искать книги по названию, автору или году издания.

-Отображение всех книг: Приложение выводит список всех книг с их уникальными идентификаторами, названиями, авторами, годами издания и статусами.

-Изменение статуса книги: Пользователь может изменить статус книги на "в наличии" или "выдана", введя её уникальный идентификатор.

Данные о книгах хранятся в текстовом или JSON формате.
Каждая операция реализована в виде отдельной функции.

После запуска приложения вам будет предложено выбрать одну из доступных операций. Следуйте инструкциям на экране для выполнения нужных действий.

Пример команд:

Для добавления книги введите 1, затем следуйте инструкциям.

Для удаления книги введите 2, затем введите id книги.

Для поиска книги введите 3, затем укажите критерии поиска.

Для отображения всех книг введите 4.

Для изменения статуса книги введите 5, затем укажите id книги и новый статус.

Приложение включает обработку ошибок для следующих случаев:

-Попытка удалить книгу с несуществующим id.

-Попытка выбрать число за которым не закреплена команда

-Ввод некорректных данных при добавлении или изменении статуса книги.

-Попытка поиска книги по неверным критериям.

-Отлавливаются ошибки при загрузке/выгрузке данных из файла

-Проверяется корректность введенных данных(id, status, author)

Структура проекта

/library_management

├── main.py     # Основной файл приложения

├── library.py             # Файл с логикой управления библиотекой

└── README.md              # Этот файл

Спасибо за использование моего приложения для управления библиотекой книг!
