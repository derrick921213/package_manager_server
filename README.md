# Derrick-Package-Manager-Server
這個repo是DPM的Server端，這裡的工具可以創建安裝包
## 在software資料夾內是已經打包好的檔案
### 包內結構
```
dpm_test1_0.0.1.tgz
|- package.json(Every package must have it)
|- hashes.json(Every package must have it)
|- other file...
```
### 初始化一個包
```shell
python dpm_server.py init
```
### 建置一個包
```shell
python dpm_server.py build
```
### 為每個檔案計算hash值
```shell
python dpm_server.py hash
```
### 修復repo內的package.json
```shell
python dpm_server.py fix add|del
```
### 自動完成建置
```shell
python dpm_server.py all
```

### 指令執行順序
1. init -> hash -> build -> fix(add|del)<br>or<br>
2. init -> all