# NATAS_19 WriteUp
:computer: Host: http://natas19.natas.labs.overthewire.org/  
:bust_in_silhouette: Usename: natas19  
:key: Password: 8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s

:triangular_flag_on_post: Flag: guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH
 
- [NATAS\_19 WriteUp](#natas_19-writeup)
  - [Обзор веб-приложения](#обзор-веб-приложения)
  - [Решение](#решение)

## Обзор веб-приложения
<a name="Обзор_веб-приложения"></a> 
Веб-приложение выглядит следующим образом
![Скриншот веб-приложения](./img/natas19/natas19_0.png)

Ввод учётных данных **test:test** приводит к вот такой реакции
![Скриншот веб-приложения](./img/natas19/natas19_1.png)

Кнопки <kbd>**View sourcecode**</kbd> на этот раз нет :sweat_smile:

## Решение
<a name="Решение"></a>
Взглянем на полученную куку снова  
![Скриншот веб-приложения](./img/natas19/natas19_2.png)

Сразу и не поймёшь что это такое, однако CyberChef творит чудеса  
![Сессионная кука](./img/natas19/natas19_3.png)

Выходит, на этот раз куку слепили из такого же рандомного трёхзначного числа и введённого логина  
Немедленно повторяем процедуру брутфорса
![Получение флага](./img/natas19/natas19_4.png)

Перебор завершился успешно
:space_invader: Payload: ``PHPSESSID=3238312d61646d696e`` 


Полученный флаг: guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH
