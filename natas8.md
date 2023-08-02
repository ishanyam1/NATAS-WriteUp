# NATAS_7 WriteUp
:computer: Host: http://natas8.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas8  
:lock: Password: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

:triangular_flag_on_post: Flag: 

## Обзор веб-приложения
Веб-приложение выглядит следующим образом:
![Скриншот веб-приложения](./img/natas8/natas8_0.png)

## Прохождение
Переход на разные страници реализован через обработку на стороне сервера параметра ``page``. Если мы передадим в нём абсолютный путь к любому другому файлу на сервере, он будет прочитан и возвращён на страницу в ответе:
![Выгрузка /etc/passwd](img/natas8/natas8_3.png)

Полученный флаг: 
