import zlib
import binascii

# More examples https://pymotw.com/3/zlib/index.html

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = zlib.compress(original_data)
print('Compressed   :', len(compressed),
      binascii.hexlify(compressed))

decompressed = zlib.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)



