import re
import secrets
import string

def menu():
    while True:
        print('______________________________')
        print('MENU PRINCIPAL')
        print('1: Cipher')
        print('2: Luhn')
        print('3: Expenses tracker')
        print('4: Case converter')
        print('5: Square root')
        print('6: Generador de contraseña con expreciones regulares')
        print('7: Torre de Hanoi con recursividad')
        print('8: Algoritmo de Orden por Fusión')
        print('0: Para salir')
        print('______________________________')

        opcion = input("Por favor ingrese una opcion: ")

        if opcion == '1':
            
            text = 'mrttaqrhknsw ih puggrur'
            custom_key = 'happycoding'

            def vigenere(message, key, direction=1):
                key_index = 0
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                final_message = ''

                for char in message.lower():

                    # Append any non-letter character to the message
                    if not char.isalpha():
                        final_message += char
                    else:        
                        # Find the right key character to encode/decode
                        key_char = key[key_index % len(key)]
                        key_index += 1

                        # Define the offset and the encrypted/decrypted letter
                        offset = alphabet.index(key_char)
                        index = alphabet.find(char)
                        new_index = (index + offset*direction) % len(alphabet)
                        final_message += alphabet[new_index]
                
                return final_message

            def encrypt(message, key):
                return vigenere(message, key)
                
            def decrypt(message, key):
                return vigenere(message, key, -1)
            
            print('______________________________')
            text2 = input("ingresa el codigo " + f'({text})' + " para decifrar: ")
            #print(f'\nEncrypted text: {text}')
            print(f'Key: {custom_key}')
            decryption = decrypt(text2, custom_key)
            print('______________________________')
            print(f'\nDecrypted text: {decryption}\n')
            
        elif opcion == '2':
            def verify_card_number(card_number):
                sum_of_odd_digits = 0
                card_number_reversed = card_number[::-1]
                odd_digits = card_number_reversed[::2]

                for digit in odd_digits:
                    sum_of_odd_digits += int(digit)

                sum_of_even_digits = 0
                even_digits = card_number_reversed[1::2]
                for digit in even_digits:
                    number = int(digit) * 2
                    if number >= 10:
                        number = (number // 10) + (number % 10)
                    sum_of_even_digits += number
                total = sum_of_odd_digits + sum_of_even_digits
                return total % 10 == 0

            def main():
                card_number = input('0- Para volver al menu principal \nIngrese un numero de tarjeta (ej: 4111-1111-4555-11) para validarlo: ')
                card_translation = str.maketrans({'-': '', ' ': ''})
                translated_card_number = card_number.translate(card_translation)

                if verify_card_number(translated_card_number):
                    print('______________________________')
                    print('--------------VALID!--------------')

                    
                else:
                    print('______________________________')
                    print('--------------INVALID!--------------')

                    

            main()
                
        elif opcion == '3':
            def add_expense(expenses, amount, category):
                expenses.append({'amount': amount, 'category': category})
                
            def print_expenses(expenses):
                for expense in expenses:
                    print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
                
            def total_expenses(expenses):
                return sum(map(lambda expense: expense['amount'], expenses))
                
            def filter_expenses_by_category(expenses, category):
                return filter(lambda expense: expense['category'] == category, expenses)
                

            def main():
                expenses = []
                while True:
                    print('______________________________')
                    print('\nExpense Tracker')
                    print('1. Add an expense')
                    print('2. List all expenses')
                    print('3. Show total expenses')
                    print('4. Filter expenses by category')
                    print('5. Exit')
                    print('______________________________')
                    
                    choice = input('Enter your choice: ')

                    if choice == '1':
                        print('______________________________')
                        amount = float(input('Enter amount: '))
                        print('______________________________')
                        category = input('Enter category: ')
                        add_expense(expenses, amount, category)

                    elif choice == '2':
                        print('______________________________')
                        print('\nAll Expenses:')
                        print_expenses(expenses)

                    elif choice == '3':
                        print('______________________________')
                        print('\nTotal Expenses: ', total_expenses(expenses))
                        print('______________________________')

                    elif choice == '4':
                        print('______________________________')
                        category = input('Enter category to filter: ')
                        print(f'\nExpenses for {category}:')
                        expenses_from_category = filter_expenses_by_category(expenses, category)
                        print_expenses(expenses_from_category)

                    elif choice == '5':
                        print('Exiting the program.')
                        break


            if __name__ == '__main__': main()
            
        elif opcion == '4':
            def convert_to_snake_case(pascal_or_camel_cased_string):

                snake_cased_char_list = [
                    '_' + char.lower() if char.isupper()
                    else char
                    for char in pascal_or_camel_cased_string
                ]

                return ''.join(snake_cased_char_list).strip('_')

            def main():
                print('______________________________')
                print(convert_to_snake_case(input('Ingrese un texto sin separar con su primer letra de cada palabra en mayuscula para convertirlo en snake case: ')))
                print('______________________________')
                

            if __name__ == '__main__':
                main()

        elif opcion == '5':
            def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
                if square_target < 0:
                    raise ValueError('Square root of negative number is not defined in real numbers')
                if square_target == 1:
                    root = 1
                    print('______________________________')
                    print(f'The square root of {square_target} is 1')
                    print('______________________________')
                elif square_target == 0:
                    root = 0
                    print('______________________________')
                    print(f'The square root of {square_target} is 0')
                    print('______________________________')

                else:
                    low = 0
                    high = max(1, square_target)
                    root = None
                    
                    for _ in range(max_iterations):
                        mid = (low + high) / 2
                        square_mid = mid**2

                        if abs(square_mid - square_target) < tolerance:
                            root = mid
                            break

                        elif square_mid < square_target:
                            low = mid
                        else:
                            high = mid

                    if root is None:
                        print(f"Failed to converge within {max_iterations} iterations.")
                
                    else:   
                        print(f'The square root of {square_target} is approximately {root}')
                
                return root
            print('______________________________')
            square_root_bisection(int(input('De que numero quieres saber la raiz cuadrada: ')))
            print('______________________________')

        elif opcion == '6':
            def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

                # Define the possible characters for the password
                letters = string.ascii_letters
                digits = string.digits
                symbols = string.punctuation

                # Combine all characters
                all_characters = letters + digits + symbols

                while True:
                    password = ''
                    # Generate password
                    for _ in range(length):
                        password += secrets.choice(all_characters)
                    
                    constraints = [
                        (nums, r'\d'),
                        (special_chars, fr'[{symbols}]'),
                        (uppercase, r'[A-Z]'),
                        (lowercase, r'[a-z]')
                    ]

                    # Check constraints        
                    if all(
                        constraint <= len(re.findall(pattern, password))
                        for constraint, pattern in constraints
                    ):
                        break
                
                return password
            if __name__ == '__main__':
                new_password = generate_password()
                print('Generated password:', new_password)
        elif opcion == '7':
            NUMBER_OF_DISKS = 3
            A = list(range(NUMBER_OF_DISKS, 0, -1))
            B = []
            C = []

            def move(n, source, auxiliary, target):
                if n <= 0:
                    return
                    # move n - 1 disks from source to auxiliary, so they are out of the way
                move(n - 1, source, target, auxiliary)
                    
                    # move the nth disk from source to target
                target.append(source.pop())
                    
                    # display our progress
                print(A, B, C, '\n')
                    
                    # move the n - 1 disks that we left on auxiliary onto target
                move(n - 1,  auxiliary, source, target)
                          
            # initiate call from source A to target C with auxiliary B
            move(NUMBER_OF_DISKS, A, B, C)
        elif opcion == '8':
            def merge_sort(array):
                if len(array) <= 1:
                    return
                
                middle_point = len(array) // 2
                left_part = array[:middle_point]
                right_part = array[middle_point:]

                merge_sort(left_part)
                merge_sort(right_part)

                left_array_index = 0
                right_array_index = 0
                sorted_index = 0

                while left_array_index < len(left_part) and right_array_index < len(right_part):
                    if left_part[left_array_index] < right_part[right_array_index]:
                        array[sorted_index] = left_part[left_array_index]
                        left_array_index += 1
                    else:
                        array[sorted_index] = right_part[right_array_index]
                        right_array_index += 1
                    sorted_index += 1

                while left_array_index < len(left_part):
                    array[sorted_index] = left_part[left_array_index]
                    left_array_index += 1
                    sorted_index += 1
                
                while right_array_index < len(right_part):
                    array[sorted_index] = right_part[right_array_index]
                    right_array_index += 1
                    sorted_index += 1


            if __name__ == '__main__':
                numbers = [4, 10, 6, 14, 2, 1, 8, 5]
                print('Unsorted array: ')
                print(numbers)
                merge_sort(numbers)
                print('Sorted array: ' + str(numbers))

        elif opcion == '0':
            print('Programa finalizado')
            break
        else:
            print('Por favor ingrese una opcion valida')
            
menu()
