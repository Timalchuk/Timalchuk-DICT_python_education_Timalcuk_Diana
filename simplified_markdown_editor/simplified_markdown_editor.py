class Editor:
    def __init__(self):
        self.text = ''''''  # Исходный текст, к которому будут применяться форматирования
        self.formatters = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'unordered-list', 'ordered-list', 'new-line']
        self.commands = ['!help', '!done']  # Список доступных команд
        self.menu()

    def menu(self):
        while True:
            line = input('Choose a formatter:>')  # Ввод выбранного форматирования или команды
            if line not in self.formatters and line not in self.commands:
                print('Unknown formatting type or command')  # Вывод сообщения об ошибке
                continue
            if line == self.commands[0]:
                print(f'''Available formatters:{' '.join(self.formatters)}
Special commands:{' '.join(self.commands)}''')  # Вывод списка
            elif line == self.commands[1]:
                break
            else:
                self.format(line)  # Применение выбранного форматирования
                print(self.text)
                f = open('output.md', 'w')  # Открытие файла output.md для записи
                f.writelines(self.text)
                f.close()

    def format(self, formatter):
        if formatter == self.formatters[0]:
            line = input('Text:>')
            self.text += line + ' '
        elif formatter == self.formatters[1]:
            line = input('Text:>')
            self.text += '**' + line + '** '  # Добавление жирного форматирования в текущий текст
        elif formatter == self.formatters[2]:
            line = input('Text:>')
            self.text += '*' + line + '* '  # Добавление курсивного форматирования в текущий текст
        elif formatter == self.formatters[3]:
            line = input('Text:>')
            self.text += '`' + line + '` '  # Добавление форматирования встроенного кода в текущий текст
        elif formatter == self.formatters[4]:
            label = input('Label:>')
            url = input('URL:>')
            self.text += '[%s](%s) ' % (label, url)  # Добавление ссылки в текущий текст
        elif formatter == self.formatters[5]:
            level = int(input('Level:>'))
            line = input('Text:>')
            self.text += level * '#' + line + ' '  # Добавление заголовка в текущий текст
        elif formatter == self.formatters[7]:
            rows = int(input('Number of rows:>'))
            while rows <= 0:
                rows = input('The numbers of rows should be greater than zero/nNumber of rows:>')
            for i in range(1, rows + 1):
                row = input('Row #%d:>' % i)
                self.text += '%d. %s\n' % (i, row)  # Добавление элементов упорядоченного списка в текущий текст
        elif formatter == self.formatters[6]:
            rows = int(input('Number of rows:>'))
            while rows <= 0:
                rows = input('The numbers of rows should be greater than zero/nNumber of rows:>')
            for i in range(1, rows + 1):
                row = input('Row #%d:>' % i)
                self.text += '* %s\n' % row  # Добавление элементов неупорядоченного списка в текущий текст
        elif formatter == self.formatters[8]:
            self.text += '\n'  # Добавление перевода строки в текущий текст


markdown = Editor()
