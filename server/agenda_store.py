import datetime

DATA_FILENAME = 'agenda.txt'

def read_agenda():
    data = []
    with open(DATA_FILENAME) as data_file:
        for line in data_file.readlines():
            date, desc = line.split(' ', 1)
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            data.append((date, desc))

def add_agenda(date, desc):
    pass