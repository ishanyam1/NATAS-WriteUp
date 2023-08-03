# NATAS_4 WriteUp
:computer: Host: http://natas4.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas4  
:key: Password: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

:triangular_flag_on_post: Flag: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD

- [NATAS\_4 WriteUp](#natas_4-writeup)
  - [Обзор веб-приложения](#обзор-веб-приложения)
  - [Решение](#решение)

## Обзор веб-приложения
<a name="Обзор_веб-приложения"></a> 
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas4/natas4_0.png)

Доступна кнопка <kbd>**Refresh page**</kbd>, ведущая на страницу ``/index.php``  
При нажатии на <kbd>**Refresh page**</kbd> страница ``/index.php`` отдаёт нам сообщение, что мы перешли на неё с неправильного источника
![Скриншот веб-приложения](./img/natas4/natas4_1.png)


## Решение
<a name="Решение"></a>
Перехватим запрос в Burp Suite и попробуем подменить заголовок ``Referer`` на предложенный ранее веб-приложением - ``http://natas5.natas.labs.overthewire.org/``  
В ответ веб-приложение отдаёт нам флаг
![Получение флага](img/natas4/natas4_2.png)

Полученный флаг: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD