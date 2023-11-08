import sqlite3

def cr_tables():
    conn = sqlite3.connect('HomeworkPPS.db')
    c = conn.cursor()
    # Создание таблицы для хранения текстовых файлов
    c.execute('''create table if not exists text_d(text_column TEXT)''')
    # создание таблицы для хранения числовых данных
    c.execute('''create table if not exists numb_d(number_column INTEGER)''')

    conn.commit()
    conn.close()

def spisok(data_list):
    conn = sqlite3.connect('HomeworkPPS.db')
    c = conn.cursor()

    for item in data_list:
        if isinstance(item, str):
            # запись слова в таблицу text_d
            c.execute("insert into text_d VALUES (?)",(item,))
            # запись длинны слова в таблицу numd_d
            c.execute("insert into numb_d VALUES (?)", (len(item),))
        elif isinstance(item,int):
            if item % 2 == 0:
             # запись четного числа в таблицу numb_d
                c.execute("insert into numb_d VALUES (?)", (item,))
        else:
        # запись слова "нечетное" в таблицу text_d
                c.execute("insert into text_d VALUES (?)", ("нечетное",))

    conn.commit()
    conn.close()

data_list = [5, 8, 'horse', 'koko', 'bazinga', 11]

cr_tables()
spisok(data_list)








