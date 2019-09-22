import csv
import io
import json

from plugin import PluginMount


class Emitter(object, metaclass=PluginMount):
    type = None

    def __init__(self):
        if self.type is None:
            raise ValueError("Emitter {0} does not provide its type".format(self.__class__.__name__))

    def output(self, locale):
        pass


class JsonEmitter(Emitter):
    type = "json"

    def output(self, locale):
        export_data = [h.as_dict() for h in locale.holidays]
        export_data.sort(key=lambda x: x['date'])
        return "\n".join([json.dumps(h, ensure_ascii=False, sort_keys=False, indent=None, separators=(',', ':')) for h in export_data]) + "\n"


class CsvEmitter(Emitter):
    type = "csv"

    def output(self, locale):
        export_data = [h.as_dict() for h in locale.holidays]
        export_data.sort(key=lambda x: x['date'])
        result = io.StringIO()

        writer = csv.DictWriter(result,
                                ["locale", "region", "date", "description", "type", "notes"],
                                quoting=csv.QUOTE_ALL,
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(export_data)

        return result.getvalue()
