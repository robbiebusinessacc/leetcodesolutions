class Codec:

    def encode(self, longUrl: str) -> str:
        return longUrl.encode()

    def decode(self, shortUrl: str) -> str:
        return shortUrl.decode()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))