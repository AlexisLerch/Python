def menu():
    while True:
        print('MENU PRINCIPAL')
        print('1 : Cipher')
        print('2: Luhn')
        print('3: Expenses tracker')
        print('0: Para salir')

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

            text2 = input("ingresa el codigo " + f'({text})' + " para decifrar: ")
            #print(f'\nEncrypted text: {text}')
            print(f'Key: {custom_key}')
            decryption = decrypt(text2, custom_key)
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
                    print('--------------VALID!--------------')
                    
                else:
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
                    print('\nExpense Tracker')
                    print('1. Add an expense')
                    print('2. List all expenses')
                    print('3. Show total expenses')
                    print('4. Filter expenses by category')
                    print('5. Exit')
                    
                    choice = input('Enter your choice: ')

                    if choice == '1':
                        amount = float(input('Enter amount: '))
                        category = input('Enter category: ')
                        add_expense(expenses, amount, category)

                    elif choice == '2':
                        print('\nAll Expenses:')
                        print_expenses(expenses)

                    elif choice == '3':
                        print('\nTotal Expenses: ', total_expenses(expenses))

                    elif choice == '4':
                        category = input('Enter category to filter: ')
                        print(f'\nExpenses for {category}:')
                        expenses_from_category = filter_expenses_by_category(expenses, category)
                        print_expenses(expenses_from_category)

                    elif choice == '5':
                        print('Exiting the program.')
                        break


            if __name__ == '__main__': main()
            
        elif opcion == '0':
            print('Programa finalizado')
            break
        else:
            print('Por favor ingrese una opcion valida')
            
menu()
