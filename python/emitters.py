from plugin import PluginMount


class Emitter(object, metaclass=PluginMount):
    type = None

    def __init__(self):
        if self.type is None:
            raise ValueError("Emitter {0} does not provide its type".format(self.__class__.__name__))

    def output(self, locale):
        pass
