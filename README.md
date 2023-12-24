# informatika_7
База до выполнения функций будет зависеть от текущего состояния базы данных. После выполнения функций база данных будет изменена в соответствии с выполненными операциями.

Основные CRUD-операции с сущностями:

1. Создание (Create): Пользователь может создать новый элемент, указав его данные, например имя, ID зала и контактные данные. Элемент добавляется с помощью функции `seller.create_one()`.

2. Удаление (Delete): Пользователь может удалить элемент по его ID. Удаление выполняется с помощью функции `seller.delete_one_by_id(*указание ID элемента*)`.

3. Чтение списка (Read): Пользователь может получить список всех элементов с помощью функции `seller.get_all()`. Также пользователь может получить конкретный элемент по его ID с помощью функции `seller.get_one_by_id()`.

4. Обновление (Update): Пользователь может заменить данные элемента по его ID. Обновление выполняется с помощью функции `seller.update_one_by_id()`.
