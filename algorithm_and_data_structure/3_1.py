while True:
    print('1. Задание-1')
    print('2. Задание_2')
    print('3. Задание_3')
    print('4. Задание_4')
    print('5. Задание_5')
    print('6. Задание_6')

    выбор = input('Выберите пункт меню: ')
    if выбор == '1':
        # Создание статического сегмента памяти размером 32 байта
        static_segment = [0] * 32

        # Создание четырех сегментов динамической памяти размером 32 байта каждый
        dynamic_segments = []
        for _ in range(4):
            dynamic_segment = [0] * 32
            dynamic_segments.append(dynamic_segment)

        # Вывод содержимого статического и динамических сегментов памяти
        print("Статический сегмент памяти:")
        print(static_segment)
        print("\nДинамические сегменты памяти:")
        for i, segment in enumerate(dynamic_segments, start=1):
            print(f"Сегмент {i}: {segment}")

        print(f"Количество отрицательных чисел в файле {filename}: {negative_count}")

    if выбор == '2':
        static_segment = [0] * 32
        dynamic_segments = [[0] * 32 for _ in range(4)]


        def NewPointer(pointer_name, pointer_type):
            global static_segment, dynamic_segments

            if pointer_type == 'byte':
                pointer_size = 1
            elif pointer_type == 'int':
                pointer_size = 2
            elif pointer_type == 'longint':
                pointer_size = 4
            else:
                print("Неподдерживаемый тип указателя")
                return

            # Поиск первого свободного места для размещения указателя
            for i in range(len(static_segment)):
                if static_segment[i] == 0:
                    static_segment[i] = pointer_name
                    static_segment[i + 1:i + pointer_size + 1] = [0] * pointer_size
                    return

            # Поиск первого свободного сегмента для выделения памяти
            for segment in dynamic_segments:
                if all(value == 0 for value in segment):
                    segment[0] = pointer_name
                    segment[1:pointer_size + 1] = [0] * pointer_size
                    return

            print("Недостаточно места для размещения указателя")


        # Пример использования функции NewPointer
        NewPointer('p', 'byte')

        # Вывод содержимого статического и динамических сегментов памяти после размещения указателя
        print("Статический сегмент памяти:")
        print(static_segment)
        print("\nДинамические сегменты памяти:")
        for i, segment in enumerate(dynamic_segments, start=1):
            print(f"Сегмент {i}: {segment}")

    if выбор == '3':
        static_segment = [0] * 32
        dynamic_segments = [[0] * 32 for _ in range(4)]


        def NewPointer(pointer_name, pointer_type):
            global static_segment, dynamic_segments

            if pointer_type == 'byte':
                pointer_size = 1
            elif pointer_type == 'int':
                pointer_size = 2
            elif pointer_type == 'longint':
                pointer_size = 4
            else:
                print("Неподдерживаемый тип указателя")
                return

            # Поиск первого свободного места для размещения указателя
            for i in range(len(static_segment)):
                if static_segment[i] == 0:
                    static_segment[i] = pointer_name
                    static_segment[i + 1:i + pointer_size + 1] = [0] * pointer_size
                    return

            # Поиск первого свободного сегмента для выделения памяти
            for segment in dynamic_segments:
                if all(value == 0 for value in segment):
                    segment[0] = pointer_name
                    segment[1:pointer_size + 1] = [0] * pointer_size
                    return

            print("Недостаточно места для размещения указателя")


        def WritePointer(pointer_name, value):
            global static_segment, dynamic_segments

            # Поиск указателя в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name:
                    static_segment[i + 1] = value
                    return

            # Поиск указателя в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name:
                    segment[1] = value
                    return

            print("Указатель не найден")


        def ReadPointer(pointer_name):
            global static_segment, dynamic_segments

            # Поиск указателя в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name:
                    return static_segment[i + 1]

            # Поиск указателя в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name:
                    return segment[1]

            print("Указатель не найден")
            return None


        # Пример использования функций WritePointer и ReadPointer
        NewPointer('p', 'int')
        WritePointer('p', 5)
        print(ReadPointer('p'))
    if выбор == '4':

        static_segment = [0] * 32
        dynamic_segments = [[0] * 32 for _ in range(4)]


        def NewPointer(pointer_name, pointer_type):
            global static_segment, dynamic_segments

            if pointer_type == 'byte':
                pointer_size = 1
            elif pointer_type == 'int':
                pointer_size = 2
            elif pointer_type == 'longint':
                pointer_size = 4
            else:
                print("Неподдерживаемый тип указателя")
                return

            # Поиск первого свободного места для размещения указателя
            for i in range(len(static_segment)):
                if static_segment[i] == 0:
                    static_segment[i] = pointer_name
                    static_segment[i + 1:i + pointer_size + 1] = [0] * pointer_size
                    return

            # Поиск первого свободного сегмента для выделения памяти
            for segment in dynamic_segments:
                if all(value == 0 for value in segment):
                    segment[0] = pointer_name
                    segment[1:pointer_size + 1] = [0] * pointer_size
                    return

            print("Недостаточно места для размещения указателя")


        def WritePointer(pointer_name, value):
            global static_segment, dynamic_segments

            # Поиск указателя в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name:
                    static_segment[i + 1] = value
                    return

            # Поиск указателя в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name:
                    segment[1] = value
                    return

            print("Указатель не найден")


        def ReadPointer(pointer_name):
            global static_segment, dynamic_segments

            # Поиск указателя в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name:
                    return static_segment[i + 1]

            # Поиск указателя в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name:
                    return segment[1]

            print("Указатель не найден")
            return None


        # Пример использования функций WritePointer и ReadPointer
        NewPointer('p', 'int')
        WritePointer('p', 5)
        print(ReadPointer('p'))
        def SetPointer(pointer_name_dest, pointer_name_src):
            global static_segment, dynamic_segments

            # Поиск указателя-источника в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name_src:
                    value = static_segment[i + 1]
                    break
            else:
                # Поиск указателя-источника в динамических сегментах
                for segment in dynamic_segments:
                    if segment[0] == pointer_name_src:
                        value = segment[1]
                        break
                else:
                    print("Указатель-источник не найден")
                    return

            # Поиск указателя-назначения в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name_dest:
                    static_segment[i + 1] = value
                    return

            # Поиск указателя-назначения в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name_dest:
                    segment[1] = value
                    return

            print("Указатель-назначение не найден")


        # Пример использования функции SetPointer
        NewPointer('p', 'int')
        NewPointer('b', 'int')
        WritePointer('b', 10)
        SetPointer('p', 'b')
        print(ReadPointer('p'))

    if выбор == '5':

        static_segment = [0] * 32
        dynamic_segments = [[0] * 32 for _ in range(4)]


        def NewPointer(pointer_name, pointer_type):
            global static_segment, dynamic_segments

            if pointer_type == 'byte':
                pointer_size = 1
            elif pointer_type == 'int':
                pointer_size = 2
            elif pointer_type == 'longint':
                pointer_size = 4
            else:
                print("Неподдерживаемый тип указателя")
                return

            # Поиск первого свободного места для размещения указателя
            for i in range(len(static_segment)):
                if static_segment[i] == 0:
                    static_segment[i] = pointer_name
                    static_segment[i + 1:i + pointer_size + 1] = [0] * pointer_size
                    return

            # Поиск первого свободного сегмента для выделения памяти
            for segment in dynamic_segments:
                if all(value == 0 for value in segment):
                    segment[0] = pointer_name
                    segment[1:pointer_size + 1] = [0] * pointer_size
                    return

            print("Недостаточно места для размещения указателя")


        def WritePointer(pointer_name, value):
            global static_segment, dynamic_segments

            # Поиск указателя в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name:
                    static_segment[i + 1] = value
                    return

            # Поиск указателя в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name:
                    segment[1] = value
                    return

            print("Указатель не найден")


        def ReadPointer(pointer_name):
            global static_segment, dynamic_segments

            # Поиск указателя в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name:
                    return static_segment[i + 1]

            # Поиск указателя в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name:
                    return segment[1]

            print("Указатель не найден")
            return None


        # Пример использования функций WritePointer и ReadPointer
        NewPointer('p', 'int')
        WritePointer('p', 5)
        print(ReadPointer('p'))
        def SetPointer(pointer_name_dest, pointer_name_src):
            global static_segment, dynamic_segments

            # Поиск указателя-источника в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name_src:
                    value = static_segment[i + 1]
                    break
            else:
                # Поиск указателя-источника в динамических сегментах
                for segment in dynamic_segments:
                    if segment[0] == pointer_name_src:
                        value = segment[1]
                        break
                else:
                    print("Указатель-источник не найден")
                    return

            # Поиск указателя-назначения в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name_dest:
                    static_segment[i + 1] = value
                    return

            # Поиск указателя-назначения в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name_dest:
                    segment[1] = value
                    return

            print("Указатель-назначение не найден")


        # Пример использования функции SetPointer
        NewPointer('p', 'int')
        NewPointer('b', 'int')
        WritePointer('b', 10)
        SetPointer('p', 'b')
        print(ReadPointer('p'))


        def FreePointer(pointer_name):
            global static_segment, dynamic_segments

            # Поиск указателя в статическом сегменте
            for i in range(len(static_segment)):
                if static_segment[i] == pointer_name:
                    del static_segment[i:i + 2]
                    return

            # Поиск указателя в динамических сегментах
            for segment in dynamic_segments:
                if segment[0] == pointer_name:
                    dynamic_segments.remove(segment)
                    return

            print("Указатель не найден")


        # Пример использования функции FreePointer
        NewPointer('p', 'int')
        WritePointer('p', 5)
        print(ReadPointer('p'))

        FreePointer('p')
        print(ReadPointer('p'))

    if выбор == '6':
        # Создаем массив из 6 элементов
        data = [0, 1, 0, 0, 0, 0]

        # Проверяем первую тройку элементов
        if any(data[:3]):
            data.insert(0, 1)
        else:
            data.insert(0, 0)

        # Проверяем вторую тройку элементов
        if any(data[3:]):
            data.insert(3, 1)
        else:
            data.insert(3, 0)

        print(data)

