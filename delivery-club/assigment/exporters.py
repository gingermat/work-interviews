import abc
import csv


class IExporter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write_row(self, row):
        pass


class CSVExporter(IExporter):
    FIELDNAMES = ('interval', 'app_id', 'country', 'installs')

    def __init__(self, filepath):
        outcsv = open(filepath, 'w')

        self._writer = csv.DictWriter(outcsv, fieldnames=self.FIELDNAMES)
        self._writer.writeheader()

    def write_row(self, row):
        self._writer.writerow(row)
