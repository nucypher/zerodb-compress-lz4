from zerodb.transform import compress, decompress
from zerodbext.compress_lz4 import lz4_compressor


def test_utilities():
    lz4_compressor.register(default=True)
    test_string = "This is a test " * 1000

    compressed_default = compress(test_string)
    compressed_lz4 = lz4_compressor.compress(test_string)

    assert compressed_default == compressed_lz4
    assert compressed_default != test_string

    assert decompress(compressed_default) == test_string
    assert decompress(compressed_lz4) == test_string
