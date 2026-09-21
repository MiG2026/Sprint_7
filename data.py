class Data:
    valid_login = 'Alexey__1988'
    valid_password = 'qwerty'
    valid_firstname = 'Alex'
    valid_courier_data = {'login': 'Alexey__1988', 'password': 'qwerty', 'firstName': 'Alex'}
    courier_data_without_name = {'login': 'Alexey__1988', 'password': '1234'}
    courier_data_with_wrong_password = {'login': 'Alexey__1988', 'password': '123456'}


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Гарри',
        'lastName': 'Поттер',
        'address': 'Тисовая улица, 4',
        'metroStation': 4,
        'phone': '+79001112233',
        'rentTime': 3,
        'deliveryDate': '2026-09-26',
        'comment': 'Профессор, это правда, или это у меня в голове?',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Рон',
        'lastName': 'Уизли',
        'address': 'Нора, 1',
        'metroStation': 26,
        'phone': '+79998887766',
        'rentTime': 7,
        'deliveryDate': '2026-06-27',
        'comment': 'Если что непонятно, иди в библиотеку.',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Гермиона',
        'lastName': 'Грейнджер',
        'address': 'Хампстед-Гарден, 28',
        'metroStation': 15,
        'phone': '+71112223344',
        'rentTime': 1,
        'deliveryDate': '2026-09-30',
        'comment': 'Страх перед именем усиливает страх перед тем, кто его носит.',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Волан-де-Морт',
        'lastName': 'Лорд',
        'address': 'Приют Вула',
        'metroStation': 215,
        'phone': '+77777777777',
        'rentTime': 2,
        'deliveryDate': '2026-09-25',
        'comment': 'Авада кедавра',
        'color': []
    }