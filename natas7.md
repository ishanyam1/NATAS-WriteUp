# NATAS_7 WriteUp
:computer: Host: http://natas7.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas7  
:key: Password: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

:triangular_flag_on_post: Flag: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

- [NATAS\_7 WriteUp](#natas_7-writeup)
  - [Обзор веб-приложения](#обзор-веб-приложения)
  - [Решение](#решение)

## Обзор веб-приложения
<a name="Обзор_веб-приложения"></a> 
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas7/natas7_0.png)

Кнопка <kbd>**Home**</kbd> отправляет на такую страничку
![Скриншот веб-приложения](./img/natas7/natas7_1.png)

Кнопка <kbd>**About**</kbd> отправляет на такую страничку
![Скриншот веб-приложения](./img/natas7/natas7_2.png)

## Решение
<a name="Решение"></a>
Переход на разные страници реализован через обработку на стороне сервера параметра ``page``. Если мы передадим в нём абсолютный путь к любому другому файлу на сервере, он будет прочитан и возвращён на страницу в ответе
![Выгрузка /etc/passwd](img/natas7/natas7_3.png)

Флаги находятся в директории ``/etc/natas_webpass/``. Вытащим флаг этой лабораторки *(он же пароль от natas8)*
![Получение флага](img/natas7/natas7_4.png)

Полученный флаг: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB
