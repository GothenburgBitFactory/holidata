import csv
import io
import json

from holidata.plugin import PluginMount


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
        result=",\n".join([json.dumps(h, ensure_ascii=False, sort_keys=False, indent=None, separators=(',', ':')) for h in export_data]) + "\n"
        return "[{}]".format(result)


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


class YamlEmitter(Emitter):
    type = "yaml"

    def output(self, locale):
        export_data = [h.as_dict() for h in locale.holidays]
        export_data.sort(key=lambda x: x["date"])

        output = "%YAML 1.1\n"
        output += "---\n"
        for holiday in export_data:
            output += "  holiday:\n"

            for key in ["locale", "region", "date", "description", "type", "notes"]:
                value = holiday[key]

                if value is not None and value != "":
                    output += "    {}: {}\n".format(key, value)
                else:
                    output += "    {}:\n".format(key)

        output += "...\n"
        return output


class XmlEmitter(Emitter):
    type = "xml"

    def output(self, locale):
        export_data = [h.as_dict() for h in locale.holidays]
        export_data.sort(key=lambda x: x["date"])

        output = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
        output += "<holidays>\n"

        for holiday in export_data:
            output += "  <holiday>\n"

            for key in ["locale", "region", "date", "description", "type", "notes"]:
                value = holiday[key] if key in holiday else ""
                output += "    <{0}>{1}</{0}>\n".format(key, value if value is not None else "")

            output += "  </holiday>\n"

        output += "</holidays>\n"
        return output
