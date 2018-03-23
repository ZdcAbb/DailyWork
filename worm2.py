print "hello world"
import urllib3
manager = urllib3.PoolManager()
r = manager.request('GET', 'http://www.baidu.com')

print r.data
print len(manager.pools)

assert 1 == len(manager.pools)

