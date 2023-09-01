import hashlib,json,tarfile,requests,sys,os
from io import BytesIO
from typing import NoReturn
from colorama import Fore, Style
commands = {
    "hash": None,
    "build": None,
    "init": None,
    # "create": ["package","hash"],
    "fix": ["add","del"]
}
file_dir = os.path.dirname(os.path.dirname(os.path.realpath('__file__')))

class command:
    def __init__(self,app:str,action:str|None,argv:list=None):
        self.app = app
        # if action is not None and isinstance(action,str):
        self.action = action
        if argv is not None and isinstance(argv,list):
            self.argv = argv
class Error(Exception):
    def __init__(self, msg: str) -> None:
        self.message = msg
    def __str__(self) -> str:
        return self.message
class Func:
    def __init__(self, obj: command):
        self.obj = obj
        match self.obj.app:
            case "init":
                self.init()
            case "build":
                self.build()
            case "hash":
                self.hash()
            case "fix":
                self.fix()
            case _:
                raise Error("沒有可執行的function!")
    def init(self):
        package_name = input('請輸入名稱：')
        package_version = input('請輸入版本號：')
        package_main = input('請輸入程式進入點：')
        if not package_name or not package_version or not package_main:
            raise Error("參數不完整！")
        package_dest = file_dir+f'/{package_name}/'
        if not os.path.exists(package_dest):
            os.mkdir(package_dest)
        with open(package_dest+'package.json','w+') as f:
            data = {
                "name":package_name,
                "file_name":f"dpm_{package_name}.tgz",
                "version":package_version,
                "main_file":package_main,
                "hash": None
            }
            f.write(json.dumps(data,indent=4))
        temp = open(package_dest+package_main,'w+')
        temp.close
        with open(package_dest+'hashes.json','w+') as f:
            data = {
                "package.json":{
                    "hashes":sha256(package_dest+'package.json','package.json')
                },
                f"{package_main}":{
                    "hashes":sha256(package_dest+package_main,package_main)
                }
            }
            f.write(json.dumps(data,indent=4))
    def build(self):
        package_name = input('請輸入名稱：')
        if not package_name:
            raise Error("參數不完整！")
        source_folder = file_dir+f'/{package_name}/'
        if not os.path.exists(source_folder):
            raise Error("打包失敗！")
        data = json.load(open(source_folder+'package.json','r'))
        if data["hash"] != sha256(source_folder+'hashes.json','hashes.json'):
            raise Error("Hash 不同無法打包！")
        output_filename = data['file_name']
        with tarfile.open(os.path.dirname(file_dir)+'/software/'+output_filename, 'w:gz') as tar:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_folder)
                    tar.add(file_path, arcname=arcname)
        print(Fore.GREEN+f'Contents of folder {Fore.YELLOW}"{source_folder}"{Style.RESET_ALL} {Fore.GREEN}have been compressed to {Fore.BLUE}"{output_filename}"'+Style.RESET_ALL)
    def hash(self):
        package_name = input('請輸入名稱：')
        hashes_file_name = 'hashes.json'
        if not package_name:
            raise Error("參數不完整！")
        source_folder = file_dir+f'/{package_name}/'
        if not os.path.exists(source_folder):
            raise Error("打包失敗!")
        if not os.path.exists(source_folder+hashes_file_name):
            raise Error('找不到hashes.json')
        with open(source_folder+hashes_file_name,'r') as f:
            hashes = json.load(f)
            for root, dirs, files in os.walk(source_folder, topdown=False):
                for name in files:
                    if name == 'hashes.json':
                        continue
                    hash_code = sha256(os.path.join(root, name),name,True)
                    hashes[name]["hashes"] = hash_code
        with open(source_folder+hashes_file_name,'w') as f:
            json.dump(hashes,f,indent=4)
        with open(source_folder+'package.json','r') as f:
            package_info = json.load(f)
            package_info["hash"] = sha256(source_folder+'hashes.json',"hashes.json",True)
        with open(source_folder+'package.json','w') as f:
            json.dump(package_info,f,indent=4)
    def fix(self):
        match self.obj.action:
            case "add":
                package_name = input('請輸入名稱：')
                if not package_name:
                    raise Error("參數不完整！")
                source_folder = file_dir+f'/{package_name}/'
                repo_folder = os.path.dirname(file_dir)+'/'
                if not os.path.exists(source_folder):
                    raise Error('目標package不存在')
                with open(repo_folder+'package.json','r') as f:
                    with open(source_folder+'package.json','r') as f1:
                        package_info = json.load(f1)
                        software_package = repo_folder+f'software/{package_info["file_name"]}'
                        if not os.path.exists(software_package):
                            raise Error(f'無法將此package添加至repo內! "{software_package}" 不存在')
                        data_map = {
                            "file_name": package_info["file_name"],
                            "version": package_info["version"],
                            "url": f"https://github.com/derrick921213/package_manager_server/raw/main/software/{package_info['file_name']}",
                            "hash": package_info["hash"] 
                        }
                    data = json.load(f)
                    data[package_info["name"]] = data_map
                with open(repo_folder+'package.json','w+') as f: 
                    f.write(json.dumps(data,indent=4))
            case "del":
                package_name = input('請輸入名稱：')
                if not package_name:
                    raise Error("參數不完整！")
                repo_folder = os.path.dirname(file_dir)+'/'
                with open(repo_folder+'package.json','r') as f:
                    data = json.load(f)
                    if package_name in data:
                        del data[package_name]
                    else:
                        raise Error('無此軟體可供刪除!')
                with open(repo_folder+'package.json','w') as f:
                    json.dump(data,f,indent=4)
def sha256(path,name,show=False) -> str:
    f = open(path, 'rb')
    sh = hashlib.sha256()
    sh.update(f.read())
    callback = sh.hexdigest()
    if show:
        print(f'{Fore.BLUE}{callback}{Style.RESET_ALL}', " ====> ", f'{Fore.YELLOW}{name}{Style.RESET_ALL}')
    f.close()
    return callback

def usage() -> NoReturn:
    msg = f'''指令樣式： {Fore.YELLOW}{sys.argv[0]} [0] [1] [...]{Style.RESET_ALL}
    {Fore.MAGENTA}這個工具可以產生一個新的package，並且可以將其hash值計算出來，也可以將package打包{Style.RESET_ALL}
[0]: hash build init fix
    {Fore.GREEN}hash{Style.RESET_ALL}: 計算所需package內所有檔案的hash值
    {Fore.GREEN}build{Style.RESET_ALL}: 將package打包成tgz壓縮檔
    {Fore.GREEN}init{Style.RESET_ALL}: 創建新的package
    {Fore.GREEN}fix{Style.RESET_ALL}: 可將repo內的package.json更新
[1]: 只是用在[0]為fix下
    {Fore.GREEN}add{Style.RESET_ALL}: 添加新的package進repo內
    {Fore.GREEN}del{Style.RESET_ALL}: 從repo刪除特定的package
    '''
    print('\n'+msg)
    os._exit(1)

def parse(argc:int,argv:list) -> object:
    app = argv[1]
    try:
        action = argv[2]
    except IndexError:
        action = None
    del argv[0:3]
    obj = command(app,action,argv)
    if obj.app not in commands:
        raise Error("沒有這項功能!")
    if commands[obj.app] is None :
        if obj.action is None and obj.argv==[]:
            del obj.action
            del obj.argv
            return obj
    if obj.action is not None:
        try:
            if obj.action not in commands[obj.app]:
                raise Error("指令錯誤!")
        except TypeError:
            raise Error("該指令不支援後續參數")
    return obj


def main(argc:int,argv:list) -> NoReturn:
    if argc<2 or argv[1] == '-h':
        usage()
    obj = parse(argc,argv)
    Func(obj)
    # print(vars(obj))

if __name__ == '__main__':
    argc:int = len(sys.argv)
    argv:list = sys.argv
    try:
        main(argc,argv)
    except Error as e:
        print(Fore.RED+e.message+Style.RESET_ALL)