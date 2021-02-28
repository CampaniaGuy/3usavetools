from .base_converter import BaseConverter

class ConverterWiiU(BaseConverter):
    _sourceSignatureLength = 0x4
    _targetSignature = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0xEA, 0xA7, 0x2B, 0x10, 0x00, 0x00, 0x00, 0x0C, 0x00, 0x00, 0x8A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2C]
