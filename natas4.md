# NATAS_4 WriteUp
:computer: Host: http://natas4.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas4  
:lock: Password: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

:triangular_flag_on_post: Flag: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD

## Обзор веб-приложения
Веб-приложение выглядит следующим образом:
![Скриншот веб-приложения](./img/natas4/natas4_0.png)

Доступна кнопка "Refresh page", ведущая на страницу ``/index.php``  
При нажатии на "Refresh page" страница ``index.php`` отдаёт нам сообщение, что мы перешли на неё с неправильного источника.
![Скриншот веб-приложения](./img/natas4/natas4_1.png)


## Решение
Перехватим запрос в Burp Suite и попробуем подменить заголовок ``Referer`` на предложенный веб-приложением (``http://natas5.natas.labs.overthewire.org/``).  
В ответ веб-приложение отдаёт нам флаг:
![Получение флага](img/natas4/natas4_2.png)

Полученный флаг: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD