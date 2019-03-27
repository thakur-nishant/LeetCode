"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""


class Codec:

    def __init__(self):
        self.mapper = {}
        self.encode_length = 6

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        sub_len = len(longUrl) // self.encode_length
        i = 0
        encoded_string = '"http://tinyurl.com/'
        while i < len(longUrl):
            curr = sum([ord(x) for x in (list(longUrl[i:i + sub_len]))]) % 73
            if curr < 10:
                encoded_string += str(curr)
            else:
                encoded_string += chr(curr - 10 + 64)
            i += sub_len

        self.mapper[encoded_string] = longUrl
        return encoded_string

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.mapper[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
