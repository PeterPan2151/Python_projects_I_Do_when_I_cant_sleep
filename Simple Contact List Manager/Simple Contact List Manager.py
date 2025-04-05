while True:
    contact_name = input('Enter Contact name (or type "done" to finish): ')
    if contact_name == 'done':
        break
    elif contact_name:
        phone_number = input(f'Enter phone number for {contact_name}: ')

        contact = f'{contact_name}: {phone_number}'

        with open('./Simple Contact List Manager/contacts.txt', 'r') as file:
            content = file.readlines()
        
        content.append(contact + '\n')

        with open('./Simple Contact List Manager/contacts.txt', 'w') as file:
            file.writelines(content)
