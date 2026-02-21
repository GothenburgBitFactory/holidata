"""
Provides base class for plugins.
"""
from typing import Any, Callable, Union


class PluginMount(type):
    """
    Metaclass that makes a given class plugin mount.
    All classes inheriting will be referenced in the 'plugins' attribute.
    """

    def __init__(cls, name: Any, bases: Any, attrs: Any) -> None:
        super(PluginMount, cls).__init__(name, bases, attrs)

        if not hasattr(cls, "plugins"):
            cls.plugins = []
        else:
            cls.plugins.append(cls)

    def get_plugin(cls, identifier: str, attribute: str) -> Union[None, Callable[[], Any]]:
        return next(iter([plugin for plugin in cls.plugins if getattr(plugin, attribute) == identifier]), None)
