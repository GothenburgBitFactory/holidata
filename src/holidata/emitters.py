import csv
import io
import json
from typing import List, Dict, Any, Callable

from holidata.holiday import Holiday
from holidata.plugin import PluginMount


class Emitter(metaclass=PluginMount):
    type: str = None

    def __init__(self):
        if self.type is None:
            raise ValueError(f"Emitter {self.__class__.__name__} does not provide its type!")

    @staticmethod
    def get(identifier: str) -> Callable[[], 'Emitter']:
        return Emitter.get_plugin(identifier, "type")

    def output(self, holidays: List[Holiday]) -> str:
        raise NotImplementedError


class JsonEmitter(Emitter):
    type: str = "json"

    def output(self, holidays: List[Holiday]) -> str:
        export_data: List[Dict[str, Any]] = [h.as_dict() for h in holidays]
        export_data.sort(key=lambda x: (x["date"], x["description"], x["region"]))
        return "\n".join([json.dumps(h, ensure_ascii=False, sort_keys=False, indent=None, separators=(",", ":")) for h in export_data]) + "\n"


class CsvEmitter(Emitter):
    type: str = "csv"

    def output(self, holidays: List[Holiday]) -> str:
        export_data: List[Dict[str, Any]] = [h.as_dict() for h in holidays]
        export_data.sort(key=lambda x: (x["date"], x["description"], x["region"]))
        result: io.StringIO = io.StringIO()

        writer: csv.DictWriter = csv.DictWriter(
            result,
            ["locale", "region", "date", "description", "type", "notes"],
            quoting=csv.QUOTE_ALL,
            lineterminator="\n")
        writer.writeheader()
        writer.writerows(export_data)

        return result.getvalue()


class YamlEmitter(Emitter):
    type: str = "yaml"

    @staticmethod
    def _format_yaml(holiday: Dict[str, Any]) -> str:
        output: str = "  holiday:\n"
        for key in ["locale", "region", "date", "description", "type", "notes"]:
            value: Any = holiday[key]

            if value is not None and value != "":
                output += f"    {key}: {value}\n"
            else:
                output += f"    {key}:\n"

        return output

    def output(self, holidays: List[Holiday]) -> str:
        export_data: List[Dict[str, Any]] = [h.as_dict() for h in holidays]
        export_data.sort(key=lambda x: (x["date"], x["description"], x["region"]))

        output: str = "%YAML 1.1\n"
        output += "---\n"

        for holiday in export_data:
            output += YamlEmitter._format_yaml(holiday)

        output += "...\n"
        return output


class XmlEmitter(Emitter):
    type: str = "xml"

    @staticmethod
    def _format_xml(holiday: Dict[str, Any]) -> str:
        output: str = "  <holiday>\n"

        for key in ["locale", "region", "date", "description", "type", "notes"]:
            value: Any = holiday[key] if key in holiday else ""
            output += f"    <{key}>{value if value is not None else ''}</{key}>\n"

        output += "  </holiday>\n"
        return output

    def output(self, holidays: List[Holiday]) -> str:
        export_data: List[Dict[str, Any]] = [h.as_dict() for h in holidays]
        export_data.sort(key=lambda x: (x["date"], x["description"], x["region"]))

        output: str = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
        output += "<holidays>\n"

        for holiday in export_data:
            output += XmlEmitter._format_xml(holiday)

        output += "</holidays>\n"
        return output
