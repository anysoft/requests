from requests.adapters import HTTPAdapter

import requests


class CustomAdapter(HTTPAdapter):
    def __init__(self, proxy_headers=None, **kwargs):
        self.proxy_headers = proxy_headers
        super().__init__(**kwargs)

    def proxy_headers(self, proxy, headers={}):
        if self.proxy_headers:
            proxy_headers = dict(self.proxy_headers)  # 创建代理请求的请求头
            proxy_headers.update(proxy.headers)  # 将代理请求的请求头与给定的请求头合并
            return proxy_headers
        return proxy.headers
def uc_unicom(ip):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.1661.41'
        }
        proxies = {
            'http': f'http://{ip}',
            'https': f'http://{ip}'
        }
        proxy_headers = {
            'Proxy-Authorization': 'Basic dWMxMC4xOTQuMTg3LjIyMDoxZjQ3ZDNlZjUzYjAzNTQ0MzQ1MWM3ZWU3ODczZmYzOA=='
        }
        session = requests.Session()
        adapter = CustomAdapter(proxy_headers=proxy_headers)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        response = session.get('https://api.ip.sb/ip')
        response = session.get('https://api.ip.sb/ip', headers=headers, proxies=proxies)


        response = requests.get('https://api.ip.sb/ip', headers=headers, proxies=proxies)
        # response = requests.get('https://searchplugin.csdn.net/api/v1/ip/get', headers=headers, proxies=proxies)
        # print(response.status_code)
        print(response.text)
    except Exception as e:
        print(e)

def tencent_unicom(ip):
    # ip = '101.71.140.5:8128'
    response = requests.get('http://kc.iikira.com/kingcard')
    Q_GUID = response.text.split(',')[0]
    Q_Token = response.text.split(',')[1]
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.1661.41'
        }
        proxies = {
            'http': f'http://{ip}',
            'https': f'http://{ip}',
            'headers': {
                'Q-GUID': Q_GUID,
                'Q-Token': Q_Token
            }
        }
        response = requests.get('https://api.ip.sb/ip', headers=headers, proxies=proxies)
        # response = requests.get('https://searchplugin.csdn.net/api/v1/ip/get', headers=headers, proxies=proxies)
        # print(response.status_code)
        print(response.text)
    except Exception as e:
        print(e)
def baidu_telecom(ip):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.1661.41'
        }
        proxies = {
            'http': f'http://{ip}',
            'https': f'http://{ip}',
            'headers': {
                'Host': '153.3.236.22:443',
                'X-T5-Auth': '683556433',
                'User-Agent': 'baiduboxapp'
            }
        }
        # session = requests.session()
        # print(session.get('https://api.ip.sb/ip', headers=headers, proxies=proxies).text)
        # print(session.get('https://api.ip.sb/ip', headers=headers, proxies=proxies).text)
        # print(session.get('https://searchplugin.csdn.net/api/v1/ip/get', headers=headers, proxies=proxies).text)
        # print(session.get('https://api.ip.sb/ip', headers=headers, proxies=proxies).text)
        # response = session.get('https://searchplugin.csdn.net/api/v1/ip/get', headers=headers, proxies=proxies)
        response = requests.get('https://api.ip.sb/ip', headers=headers, proxies=proxies)
        # response = requests.get('https://searchplugin.csdn.net/api/v1/ip/get', headers=headers, proxies=proxies)
        # print(response.status_code)
        print(response.text)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    uc_unicom('101.71.140.5:8128')
    # tencent_unicom('210.22.247.196:8090')
    # baidu_telecom('14.215.179.244:443')
    pass

"""
UC
 listen_port=65080;worker_proc=0;uid=3004;daemon=on;http_ip=101.71.140.5;http_port=8128;http_del="Host,X-Online-Host";http_first="[M] http://[H][U] [V]\r\nCONNECT applog.uc.cn:443/ HTTP/1.1\r\nProxy-Authorization: Basic dWMxMC4xOTQuMTg3LjIyMDoxZjQ3ZDNlZjUzYjAzNTQ0MzQ1MWM3ZWU3ODczZmYzOA==\r\n";Host: [H]\r\n
Proxy-Connection: keep-alive\r\n";https_connect=on;https_ip=101.71.140.5;https_port=8128;https_del="X-Online-Host,Host";https_first="[M] [H]/ [V]\r\nCONNECT applog.uc.cn:443/ HTTP/1.1\r\nProxy-Authorization: Basic dWMxMC4xOTQuMTg3LjIyMDoxZjQ3ZDNlZjUzYjAzNTQ0MzQ1MWM3ZWU3ODczZmYzOA==\r\n";dns_tcp=http;dns_listen_port=65053;dns_url="119.29.29.29";

101.71.140.5，http端口8128，https端口8128
58.144.152.23 重庆
 58.144.152.119 重庆
 111.206.25.206 北京
 123.126.122.24 北京
 125.39.52.35 天津
 111.161.111.158 天津
 210.22.247.196 上海
 116.128.146.115 上海
 140.207.62.13 上海
 140.207.62.38 上海
 157.255.173.182 广东
 157.255.173.185 广东
 157.255.173.186 广东


Proxy-Authorization: Basic dWNYLVQ1LUF1dGg6MWY0N2QzZWY1M2IwMzU0NDM0NTFjN2VlNzg3M2ZmMzg=
ucX-T5-Auth:1f47d3ef53b035443451c7ee7873ff38

Proxy-Authorization: Basic dWMxMC4xOTQuMTg3LjIyMDoxZjQ3ZDNlZjUzYjAzNTQ0MzQ1MWM3ZWU3ODczZmYzOA==
uc10.194.187.220:1f47d3ef53b035443451c7ee7873ff38

Proxy-Authorization: Basic dWMxMC4xMDMuMjcuMTgyOjFmNDdkM2VmNTNiMDM1NDQzNDUxYzdlZTc4NzNmZjM4
uc10.103.27.182:1f47d3ef53b035443451c7ee7873ff38

#王卡的IP和端口
#116.128.146.115，http端口8090，https端口8091
#210.22.247.196，http端口8090，https端口8091
#210.22.247.193，http端口8090，https端口8091
#广东 157.255.173.182 157.255.137.185
#上海 140.207.62.38 210.22.247.196
#北京 111.206.25.206 123.126.122.24
#天津 125.39.52.35 111.161.111.158
#重庆 58.144.152.119
#西瓜资源网收集整理 www.xglist.com

listen_port=65080;worker_proc=0;mode=3gnet;daemon=on;uid=3004;token_api="http://api.dtpwxn.top/get_tiny_cofing.php";http_ip=210.22.247.196;http_port=8090;http_del="X-Online-Host,Host";http_first="[M] http://[H][U] [V]\r\nQ-GUID: [Q_G]\r\nQ-Token: [Q_T]\r\nHost: [H]\r\n";https_connect=on;https_ip=210.22.247.196;https_port=8091;https_del="X-Online-Host,Host";https_first="[M] [H] [V]\r\nHost: [H]\r\nQ-GUID: [Q_G]\r\nQ-Token: [Q_T]\r\n";dns_tcp=http;dns_listen_port=65053;dns_url="119.29.29.29";
token_api="http://cs.xxzml.cn/k/get_tinyproxy_config.php";
#token_api="http://kc.iikira.com/kingcard";


#百度的IP和端口
#14.215.177.73，http端口443，https端口443
#220.181.43.12，http端口443，https端口443
#180.97.104.45，http端口443，https端口443
#123.125.142.40，http端口443，https端口443
#163.177.151.162，http端口443，https端口443
#112.80.255.21，http端口443，https端口443
14.215.179.244
Host: 153.3.236.22:443\r\nX-T5-Auth: 683556433\r\nUser-Agent:baiduboxapp

"""
