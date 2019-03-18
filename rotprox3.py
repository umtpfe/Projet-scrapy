from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

ua = UserAgent() # Genere un utilisateurs aleatoirement
proxies = [] # proxies [ip, port]

# Main function
def main():
  # Recupere les dernier proxies
  proxies_req = Request('https://www.sslproxies.org/')
  proxies_req.add_header('User-Agent', ua.random)
  proxies_doc = urlopen(proxies_req).read().decode('utf8')

  soup = BeautifulSoup(proxies_doc, 'html.parser')
  proxies_table = soup.find(id='proxylisttable')

  # Sauvegarde les proxies dans un tableau
  for row in proxies_table.tbody.find_all('tr'):
    proxies.append({
      'ip':   row.find_all('td')[0].string,
      'port': row.find_all('td')[1].string
    })

  # Choisire un proxy aleatoirement 
  proxy_index = random_proxy()
  proxy = proxies[proxy_index]

  for n in range(1, 100):
    req = Request('https://www.google.com/')
    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

    # Genere un proxy chaque 10 requetes
    if n % 10 == 0:
      proxy_index = random_proxy()
      proxy = proxies[proxy_index]

    # appel
    try:
      my_ip = urlopen(req).read().decode('utf8')
      print('#' + str(n) + ': ' + my_ip)
    except: # Supprime le proxy en cas d'erreur trouve un autre
      del proxies[proxy_index]
      print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
      proxy_index = random_proxy()
      proxy = proxies[proxy_index]

# indexe
def random_proxy():
  return random.randint(0, len(proxies) - 1)

if __name__ == '__main__':
  main()