#include <iostream>//
int countOnesInChar(char c) {
    int count = 0;
    for (int i = 0; i < 8; ++i) { // char содержит 8 бит
        if (c & (1 << i)) {
            count++;
        }
    }
    return count;
}

void printBitMap(unsigned char bitMap) {
    for (int i = 7; i >= 0; --i) {
        std::cout << ((bitMap & (1 << i)) ? 1 : 0);
    }
    std::cout << std::endl;
}
// Created by slesa on 12.02.2024.
//
int main() {
    setlocale(LC_ALL, "");
    int i, j, k, l, q;
    int m;
    while (true) {

        std::wcout << L"Введите номер задания q: ";
        std::cin >> q;

        if (q == 1) {
            std::wcout << L"Введите значения переменных i, j, k, l: ";
            std::cin >> i >> j >> k >> l;
            if (i > j + 2 * k) {
                m = (i >> 4) + (j << 7) - 17 + (k << 1) - (l >> 5);
            } else {
                m = (i >> 4) + (j << 7) - 17 + (k << 1) + (l >> 5);
            }

            std::wcout << L"Значение выражения: " << m << std::endl;
        }


        if (q == 2) {
            int num1, num2;

// Ввод двух целочисленных чисел
            std::wcout << L"Введите два целочисленных числа: ";
            std::cin >> num1 >> num2;

// Вывод чисел в шестнадцатеричном виде
            std::wcout << L"Первое число в шестнадцатеричном виде: " << std::hex << num1 << std::endl;
            std::wcout << L"Второе число в шестнадцатеричном виде: " << std::hex << num2 << std::endl;

// Побитовое сложение и вывод результата в шестнадцатеричном виде
            int sum = num1 | num2;
            std::wcout << L"Побитовое сложение: " << std::hex << sum << std::endl;

// Побитовое умножение и вывод результата в шестнадцатеричном виде
            int product = num1 & num2;
            std::wcout << L"Побитовое умножение: " << std::hex << product << std::endl;

// Побитовый сдвиг влево и вывод результата в шестнадцатеричном виде
            int left_shift = num1 << 1;
            std::wcout << L"Побитовый сдвиг влево: " << std::hex << left_shift << std::endl;

// Побитовый сдвиг вправо и вывод результата в шестнадцатеричном виде
            int right_shift = num2 >> 1;
            std::wcout << L"Побитовый сдвиг вправо: " << std::hex << right_shift << std::endl;

        }
        if (q == 3){
            // Исходное значение (блок из четырех символов)
            unsigned int u = 0x41424344; // ABCD

            // Маска для XOR-шифрования
            unsigned int mask = 0x12345678;

            // Шифрование
            unsigned int encrypted = u ^ mask;

            // Вывод отдельных байтов до шифрования
            std::wcout << L"Отдельные байты до шифрования: ";
            std::cout << static_cast<char>(u >> 24) << static_cast<char>((u & 0xffffff) >> 16) << static_cast<char>((u & 0xffff) >> 8) << static_cast<char>(u & 0xff) << std::endl;

            // Вывод отдельных байтов после шифрования
            std::wcout << L"Отдельные байты после шифрования: ";
            std::cout << static_cast<char>(encrypted >> 24) << static_cast<char>((encrypted & 0xffffff) >> 16) << static_cast<char>((encrypted & 0xffff) >> 8) << static_cast<char>(encrypted & 0xff) << std::endl;

            // Расшифрование
            unsigned int decrypted = encrypted ^ mask;

            // Вывод отдельных байтов после расшифрования
            std::wcout << L"Отдельные байты после расшифрования: ";
            std::cout << static_cast<char>(decrypted >> 24) << static_cast<char>((decrypted & 0xffffff) >> 16) << static_cast<char>((decrypted & 0xffff) >> 8) << static_cast<char>(decrypted & 0xff) << std::endl;
        }

        if (q == 4){
            int u = 0x11223344; // Пример значения переменной int

            // Вывод исходного значения
            std::wcout << L"Исходное значение: " << std::hex << i << std::endl;

            // Меняем местами последний и предпоследний байты
            int swapped = ((u & 0xFF) << 24) | ((u & 0xFF00) << 8) | ((u & 0xFF0000) >> 8) | ((u & 0xFF000000) >> 24);

            // Вывод значения после обмена байтов
            std::wcout << L"Значение после обмена байтов: " << std::hex << swapped << std::endl;

        }

        if (q == 5){

                char c = 'A'; // Пример значения переменной char

                // Вывод исходного значения
                std::wcout << L"Исходное значение: " << static_cast<int>(c) << std::endl;

                // Определение количества единиц в двоичном представлении
                int onesCount = countOnesInChar(c);

                // Вывод количества единиц
                std::wcout << L"Количество единиц в двоичном представлении: " << onesCount << std::endl;


        }
        if (q == 6){

            unsigned char bitMap = 0; // Начальная битовая карта, все блоки свободны

            // Запрос пользователя о блоках, которые нужно занять
            int blocksToOccupy;
            std::wcout << L"Введите номера блоков, которые нужно занять (от 0 до 7): ";
            std::cin >> blocksToOccupy;

            bitMap |= (1 << blocksToOccupy); // Установка бита для занятого блока
            std::wcout << L"Битовая карта после занятия блока: ";
            printBitMap(bitMap);

            // Запрос пользователя о блоках, которые нужно освободить
            int blocksToFree;
            std::wcout << L"Введите номера блоков, которые нужно освободить (от 0 до 7): ";
            std::cin >> blocksToFree;

            bitMap &= ~(1 << blocksToFree); // Сброс бита для освобожденного блока
            std::wcout << L"Битовая карта после освобождения блока: ";
            printBitMap(bitMap);
        }
        return 0;
    }


    }





