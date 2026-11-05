# https://www.linkedin.com/pulse/how-solve-games-genetic-algorithms-building-advanced-shewchenko-cz93e/
import math

class Node:

    @staticmethod
    def buildNode(type="hidden", bias = math.random() * 0.2 - 0.1, squash = "SIGMOID"):
        return Node(type, bias, squash)

    def __init__(self, type, bias, squash):
        self.type = type
        self.bias = bias
        self.squah = squash
        self.activation = 0
        self.state = 0
        self.connections = {"in":[], "out": [],}
        
class Connection:
    @staticmethod
    def buildConnection(start, end, weight):
        return Connection(start,end,weight)

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight == math.random() * 0.2 - 0.1 if weight == None else weight

class Network:
    def __init__(self,inputSize = 2, outputSize = 1):
        self.nodes = []
        self.connections = []
        self.inputSize = inputSize
        self.outputSize = outputSize
        self.inputNodes = set()
        self.outputNotes = set()

    @staticmethod
    def buildNetwork(inputSize, outputSize):
        if inputSize == None or outputSize == None:
            raise ValueError("No inputSize or outputSize given")

        network = Network(inputSize, outputSize)
        Network.createInitialNodes(network)
        Network.connectIntialNodes(network)

    @staticmethod
    def createInitialNodes(network):
        for _ in range(network.inputSize):
            node = Node.buildNode("input")
            network.nodes.append(node)
            network.inputNodes.add(node)

        for _ in range(network.outputSize):
            node = Node.buildNode("output")
            network.nodes.append(node)
            network.outputNodes.add(node)

    @staticmethod
    def connectInitialNodes(network):
        for i in range(network.inputSize):
            for j in range(network.inputSize, network.outputSize + network.inputSize):
                weight = math.random() * network.inputSize * math.sqrt(2/network.inputSize)
                connectNode
        



