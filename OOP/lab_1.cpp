#include <iostream>

// using namespace std;


int main() {
    int num = 10; // Пример числа для сдвига
    int shift = 2; // Количество позиций для сдвига

    // Побитовый сдвиг влево с помощью умножения на 2^shift
    int left_shifted = num * (1 << shift);
    std::cout << "Number " << num << " after a bitwise shift to the left by " << shift << " positions: " << left_shifted << std::endl;

    // Побитовый сдвиг вправо с помощью деления на 2^shift
    int right_shifted = num / (1 << shift);
    std::cout << "Number " << num << " after a bitwise shift to the right by " << shift << " positions: " << right_shifted << std::endl;




    int i, j, k, l;
    int m;

    std::cout << "Enter the values of the variables i, j, k, l: ";
    std::cin >> i >> j >> k >> l;

    if (i > j + 2 * k) {
    m = (i >> 4) + (j << 7) - 17 + (k << 1) - (l >> 5);
    } else {
    m = (i >> 4) + (j << 7) - 17 + (k << 1) + (l >> 5);
    }

    std::cout << "Значение выражения: " << m << std::endl;


    int num1, num2;

// Ввод двух целочисленных чисел
    std::cout << "Введите два целочисленных числа: ";
    std::cin >> num1 >> num2;

// Вывод чисел в шестнадцатеричном виде
    std::cout << "Первое число в шестнадцатеричном виде: " << std::hex << num1 << std::endl;
    std::cout << "Второе число в шестнадцатеричном виде: " << std::hex << num2 << std::endl;

// Побитовое сложение и вывод результата в шестнадцатеричном виде
    int sum = num1 | num2;
    std::cout << "Побитовое сложение: " << std::hex << sum << std::endl;

// Побитовое умножение и вывод результата в шестнадцатеричном виде
    int product = num1 & num2;
    std::cout << "Побитовое умножение: " << std::hex << product << std::endl;

// Побитовый сдвиг влево и вывод результата в шестнадцатеричном виде
    int left_shift = num1 << 1;
    std::cout << "Побитовый сдвиг влево: " << std::hex << left_shift << std::endl;

// Побитовый сдвиг вправо и вывод результата в шестнадцатеричном виде
    int right_shift = num2 >> 1;
    std::cout << "Побитовый сдвиг вправо: " << std::hex << right_shift << std::endl;

    return 0;
}


