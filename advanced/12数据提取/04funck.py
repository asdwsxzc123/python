from parse_url import parse_url
import re

class Jandan:
    def __init__(self):
        self.url = 'http://jandan.net/duan'
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    def run(self):
        html_str = parse_url(self.url,self.header)
        
        print(html_str)

if __name__ == "__main__":
    jandan = Jandan()
    jandan.run()