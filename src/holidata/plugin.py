"""
Provides base class for plugins.
"""


class PluginMount(type):
    """
    Metaclass that makes a given class plugin mount.
    All classes inheriting will be referenced in the 'plugins' attribute.
    """

    def __init__(cls, name, bases, attrs):
        super(PluginMount, cls).__init__(name, bases, attrs)

        if not hasattr(cls, "plugins"):
            cls.plugins = []
        else:
            cls.plugins.append(cls)
