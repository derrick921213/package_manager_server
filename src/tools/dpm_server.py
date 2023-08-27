import hashlib,json,tarfile,requests,sys,os
from io import BytesIO

def sha256(path,name):
    f = open(path, 'rb')
    sh = hashlib.sha256()
    sh.update(f.read())
    print(sh.hexdigest(), " ====> ", name)
    f.close()
    return
    
def error(err_code: int):
    match err_code:
        case 1:
            print("參數不足需求,目前只有一個")
    os._exit(err_code)


def main(argc:int,argv:list) -> int:
    if argc<2:
        return 1
    return 0

if __name__ == '__main__':
    argc = len(sys.argv)
    argv = sys.argv
    exit_code:int = main(argc,argv)
    if exit_code!=0:
        error(exit_code)