import hashlib, httplib, os, re, urllib2, urllib
###############################INCOMPLETE################################
if __name__ == '__main__':
    md5 = dict()
    #TODO
    md5['93c985c35fa28eb819d91b5f55be7b65'] = 'compromise'
    md5['4039a3ef7fc79e4adb60b43ac108d648'] = 'admin'
    md5['fe9ac5cfb7b2438c900ed3e56c0e2cb0'] = '0dayz'
    md5['4c298cfa40e502fb644d9a5fdc9c6a11'] = 'vulnerability'
    md5['3761dd5bdb3dae4fc7ba3d5652b7bfc0'] = 'security'
    md5['3d0a2ab11fb9c59d19a9d95d56ea2e6d'] = 'hacker'
    md5['539746c4b3beae3e77773fa940d83d78'] = 'pentester'

    conn = httplib.HTTPConnection('192.168.159.131')
    conn.request('GET','/captcha/example5/')
    res = conn.getresponse()
    url = 'http://192.168.159.131/captcha/example5/'+re.findall(r'<img src="(.*)"/ >',res.read())[0]
    urllib.urlretrieve(url, 'temp.png')
    imgfile = open('temp.png')
    imgmd5 = hashlib.md5(imgfile.read()).hexdigest()
    imgfile.close()
    conn.request('GET','/captcha/example5/submit?captcha='+md5[imgmd5]+'&submit=Submit+Query')
    res2 = conn.getresponse()
    page = res2.read()
    print page
    print md5[imgmd5]
    os.remove('temp.png')
