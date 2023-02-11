from .base_converter import BaseConverter

class ConverterWiiU(BaseConverter):
    _sourceSignatureLength = 0x4
    _targetSignature = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x00, 0x00, 0x8A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2C]

    def convertMonsterDiscState(self, srcBytes, state):
        newState = [0, 0]

        discovered = state[0] & 1
        silver = state[0] & 2
        gold = state[0] & 4
        mini = state[0] & 8

        if discovered:
            newState[0] += 0x80

        if silver:
            newState[0] += 0x20

        if gold:
            newState[0] += 0x40

        if mini:
            newState[0] += 0x8

        return newState