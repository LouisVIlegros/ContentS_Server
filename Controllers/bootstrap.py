from Controllers.registry.factory import mainFactory as registry

def bootstrap(namespace, actionType):
    return registry[namespace][actionType]















