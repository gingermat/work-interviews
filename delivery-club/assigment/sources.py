import collections
import csv
import os


class CSVSourceBase(collections.abc.Iterator):
    DEFAULT_DELIMITER = ';'

    def __init__(self, filepath, delimiter=DEFAULT_DELIMITER):
        if not os.path.exists(filepath):
            raise FileNotFoundError(filepath)

        self._filepath = filepath
        self._delimiter = delimiter

    def __iter__(self):
        csvfile = open(self._filepath, 'r')
        self._reader = csv.reader(csvfile, delimiter=self._delimiter)

        return self

    def __next__(self):
        for row in self._reader:
            row = self._row_clear(row)
            return self.to_dict(keys=self._get_fields(), values=row)

        raise StopIteration

    @staticmethod
    def to_dict(keys, values):
        return dict(zip(keys, values))

    @staticmethod
    def _row_clear(row):
        return list(map(str.strip, row))

    def _get_fields(self):
        raise NotImplementedError


class CSVSourceExample1(CSVSourceBase):
    def _get_fields(self):
        fields = ['ip', 'time', 'upstream', 'url', 'code', 'num', 'rt', 'qs']
        return fields
