# a simple demo for scan all ip net
* 一个新的demo用于扫描网段当中的所有有效ip地址

### install
```bash
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple # 如果想全局指定清华源

sudo apt-get install nmap

pip install -r requirements.txt  # install
```

### 运行
```bash
├── demo_netifaces.py  # netifaces 案例
├── demo_nmap.py       # nmap  案例
├── demo_scapy.py      # scapy 案例
```  