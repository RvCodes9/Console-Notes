from colorama import Fore, Style

Notes = []

while True:

    while True:

        Note = input(f'\n{Fore.GREEN}:: Note << {Style.RESET_ALL}')

        if Note == '</>':
            break

        else:
            Notes.append(Note)

    operation = input(f'\n{Fore.YELLOW}:: Operation >>> {Style.RESET_ALL}')

    match operation:

        # Save file
        case 'save' | 'Save' | 'SAVE' :

            new_file = input(f'\n{Fore.MAGENTA}:: Save file >>> {Style.RESET_ALL}')

            if new_file.endswith('.txt') == True:

                file_type = ''

            else:
                file_type = '.txt'

            
            with open(new_file + file_type, 'a') as file:
                for line in Notes:
                    file.write(line+'\n')

        
        # Open file
        case 'open' | 'Open' | 'OPEN' :

            new_file = input(f'\n{Fore.MAGENTA}:: Open file >>> {Style.RESET_ALL}')

            if new_file.endswith('.txt') == True:

                file_type = ''

            else:
                file_type = '.txt'
            
            try:
                with open(new_file + file_type, 'r') as file:
                    print(f'\n-------------< {file.name} >-------------\n{Fore.GREEN}Notes ::{Style.RESET_ALL}{Fore.YELLOW} {file.read()}{Style.RESET_ALL}')
            except:
                print(f'\n{Fore.RED}No "{new_file}.txt" file{Style.RESET_ALL}')


        # Exit Notes app
        case 'exit' | 'Exit' | 'EXIT':
            break