# PRK
## О программе
Утилита для преобразования всех файлов в указанной директории из XML в markdown и из markdown в HTML.

## Установка и запуск приложения
Системные требования:
* Python версии 3.10.6

Для запуска утилиты необходимо:
1. Скачать директорию PRK из репозитория на GitLab (https://dev.cs.petrsu.ru/imit/cs.petrsu.ru)
2. Для установки библиотек в терминале PRK/src/ ввести: pip install -r requirements.txt
3. Для работы в терминале PRK/src/converter ввести: python3 converter.py -d DIRECTORY [-x] [-m] [-a ANOTHER]

## Справочник по работе
* Для ознакомления в терминале PRK/src/converter ввести: python3 converter.py --help
* Используемые ключи:
```
-d, --directory    Выбор директории, из которой требуется преобразовать файлы
-x, --xml          Преобразование из XML в MarkDown
-m, --markdown     Преобразование из MarkDown в HTML
-a, --another      Выбор директории, в которую требуется сохранить преобразованные файлы
```
