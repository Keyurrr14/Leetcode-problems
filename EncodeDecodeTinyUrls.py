class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

class Codec:

    def __init__(self):
        self.urls: dict = {}
        self.num: int = -1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.num += 1
        self.urls[self.num] = longUrl
        print(f"https://tinyurl.com/{str(self.num)}")
        return f"https://tinyurl.com/{str(self.num)}"
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""

        site_code: int = int(shortUrl.split("/")[-1])
        print(self.urls[site_code])
        return self.urls[site_code]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))