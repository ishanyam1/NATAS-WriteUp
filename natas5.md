# NATAS_5 WriteUp
:computer: Host: http://natas5.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas5  
:key: Password: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD

:triangular_flag_on_post: Flag: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

- [NATAS\_5 WriteUp](#natas_5-writeup)
  - [Обзор веб-приложения](#обзор-веб-приложения)
  - [Решение](#решение)

## Обзор веб-приложения
<a name="Обзор_веб-приложения"></a> 
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas5/natas5_0.png)

Больше никакого функционала, на первый взгляд, нет

## Решение
<a name="Решение"></a>
Перехватим запрос в Burp Suite и увидим, что веб-приложение устанавливает нам куку ``loggedin``, установленную в **0** 
![Установленная кука](img/natas5/natas5_1.png)

Попробуем выставить эту куку в **1** и увидим, что теперь в ответ веб-приложение отдаёт нам флаг
![Получение флага](img/natas5/natas5_2.png)


Полученный флаг: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR
