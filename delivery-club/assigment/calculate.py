#!/usr/bin/env python3

from parser import Parser

from exporters import CSVExporter
from sources import CSVSourceExample1
from stat_store import StatStore


def main(datafile, outfile):
    sources = (
        CSVSourceExample1(datafile),
    )

    stat_store = StatStore()
    parser = Parser(sources=sources, stat_store=stat_store)
    parser.parse()

    csv_exporter = CSVExporter(filepath=outfile)
    stat_store.export(csv_exporter)


if __name__ == '__main__':
    datafile = 'data/sample_installs.csv'
    outfile = 'output.csv'

    main(datafile, outfile)
