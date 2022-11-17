import datetime


class CplanDataSession:
    """This class is used to manage the plaintext agenda database"""

    def __init__(self, filename):
        """Set instance property and read for the first time"""
        self.filename = filename
        self.read()

    def read(self):
        """Read from the data file and update the current data state"""
        self._data = []
        with open(self.filename) as f:
            for line in f.readlines():
                date, desc = line.strip().split(' ', 1)
                date = self.str_to_date(date)
                self._data.append((date, desc))

    def add(self, date, desc):
        """Add an entry to data"""
        self._data.append((date, desc))

    def remove(self, search_date, keyword):
        """Remove an entry to data"""
        for i, (date, desc) in enumerate(self._data):
            if date == search_date and keyword.lower() in desc.lower():
                del self._data[i]

    def commit(self):
        """Write the current data to database"""

        with open(self.filename, 'w') as f:
            for date, desc in self._data:
                date = self.date_to_str(date)
                f.write(f'{date} {desc}\n')

    def get_data(self):
        """Get the current data (sorted)"""
        return sorted(self._data, key=lambda d: d[0], reverse=True)

    @staticmethod
    def str_to_date(date_str):
        """Convert str type to datetime"""
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')

    @staticmethod
    def date_to_str(date):
        """Convert datetime type to str type"""
        return date.strftime('%Y-%m-%d')
