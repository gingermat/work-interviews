from collections.abc import Iterable
from datetime import datetime
from urllib import parse

from iso3166 import countries


class Parser:
    def __init__(self, sources, stat_store):
        self.sources = sources
        self._stat_store = stat_store

    def parse(self):
        for source in self.sources:
            self._source_parse(source)

    def _source_parse(self, source):
        for row in source:
            self._row_parse(row)

    def _row_parse(self, row):
        row_valid = self._row_validate(row)
        if not row_valid:
            return

        qs = self._extract_qs(row['qs'])
        if not qs:
            return

        self._stat_store.store(**qs)

    def _row_validate(self, row):
        return 'qs' in row

    def _extract_qs(self, qs):
        qs = parse.parse_qs(qs)

        app_id = qs.get('app_id')
        if not app_id:
            return

        time_install = qs.get('install_time')
        if not time_install:
            return

        if isinstance(app_id, Iterable):
            app_id = app_id[0]

        if isinstance(time_install, Iterable):
            time_install = time_install[0]

        try:
            time_install = datetime.strptime(
                time_install, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            return

        country_code = qs.get('country_code')
        if country_code is not None:
            if isinstance(country_code, Iterable):
                country_code = country_code[0]

            try:
                country = countries.get(country_code.upper())
                country_code = country.alpha2
            except KeyError:
                country_code = ''
        else:
            country_code = ''

        return dict(app_id=app_id, country_code=country_code,
                    time_install=time_install)
