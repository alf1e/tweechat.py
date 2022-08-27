class EventHandle:
    def __int__(self):
        self.event_handlers = {}

    def ON(self, event: str, function):
        self.event_handlers[event] = function

    def call(self, event: str, context):
        self.event_handlers[event](context)
