class Tool:
    
    def __init__(self, name, description, path, option, argument, outputElement, outputDataType):
        self.name = name
        self.description = description
        self.path = path
        self.option = option
        self.argument = argument
        self.outputElement = outputElement
        self.outputDataType = outputDataType
    

    def setName(self, name):
        self.name = name

    def setDescription (self, description):
        self.description = description
    
    def setPath (self, path):
        self.path = path
    
    def setOption (self, option):
        self.option = option

    def setArgument (self, argument):
        self.argument = argument

    def setOutputElement(self, outputElement):
        self.outputElement = outputElement

    def setOutputDataType(self, outputDataType):
        self.outputDataType = outputDataType
    
    def getName(self):
        return self.name

    def getDescription (self):
        return self.description
    
    def getPath (self):
        return self.path
    
    def getOption (self):
        return self.option

    def getArgument (self):
        return self.argument

    def getOutputElement(self):
        return self.outputElement

    def getOutputDataType(self):
        return self.outputDataType
