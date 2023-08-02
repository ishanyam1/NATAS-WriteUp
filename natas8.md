# NATAS_8 WriteUp
:computer: Host: http://natas8.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas8  
:lock: Password: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

:triangular_flag_on_post: Flag: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd

## Обзор веб-приложения
Веб-приложение выглядит следующим образом:
![Скриншот веб-приложения](./img/natas8/natas8_0.png)

Ввод слова ``test`` привёл к вот такой реакции:  
![Скриншот веб-приложения](./img/natas8/natas8_1.png)

Кнопка <kbd>View sourcecode</kbd> позволяет просмотреть исходный код страницы:
![Скриншот исходного кода](./img/natas8/natas8_2.png)

## Решение
В коде элемента видим зашифрованную секретную строку и алгоритм, по которому секрет был зашифрован:
![Алгоритм шифрования](img/natas8/natas8_3.png)

Проведём обратное преобразование и получим секретную строку - ``oubWYf2kBq``
![Получение секретной строки](img/natas8/natas8_4.png)

Отправим полученный секрет в форму веб-приложения и получим в ответ флаг
![Флаг](img/natas8/natas8_5.png)

Полученный флаг: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
