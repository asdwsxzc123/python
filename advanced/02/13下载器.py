import urllib.request
import gevent
# req = urllib.request.urlopen('http://www.sina.com.cn')
def download(img_name, img_url):
  req = urllib.request.urlopen(img_url)
  content = req.read()
  with open(img_name, 'wb') as f:
    f.write(content)

def main():
  gevent.joinall([
      gevent.spawn(download, './img/1.jpg', 'https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/31/23ee10a3ac3e6511d669fa41f42faf04_big.png'),
      gevent.spawn(download, './img/2.jpg','https://rpic.douyucdn.cn/live-cover/appCovers/2018/11/03/5925473_20181103010952_small.jpg')
  ])

if __name__ == '__main__':
  main()