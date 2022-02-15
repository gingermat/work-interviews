import time


class StatStore:
    TIMESTAMP_INTERVAL = 300

    def __init__(self):
        self._stats = {}

    def store(self, app_id, country_code, time_install):
        interval = time.mktime(
            time_install.timetuple())/self.TIMESTAMP_INTERVAL
        interval = int(interval)*self.TIMESTAMP_INTERVAL

        if interval not in self._stats:
            self._stats[interval] = {}

        if app_id not in self._stats[interval]:
            self._stats[interval][app_id] = {}

        if country_code not in self._stats[interval][app_id]:
            self._stats[interval][app_id][country_code] = 0

        self._stats[interval][app_id][country_code] += 1

    def export(self, exporter):
        for interval, values in sorted(self._stats.items()):
            for app_id, countries in values.items():
                for country, count in countries.items():
                    row = {
                        'interval': interval,
                        'app_id': app_id,
                        'country': country,
                        'installs': count
                    }
                    exporter.write_row(row)
