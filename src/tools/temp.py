# import hashlib

# def sha256(path, name):
#     f = open(path, 'rb')
#     sh = hashlib.sha256()
#     sh.update(f.read())
#     print(sh.hexdigest(), " ====> ", name)
#     f.close()
#     return
# sha256("./dpm_temp.tgz","dpm_temp.tgz")
# import json
# with open('package.json','r') as file:
#     data = json.load(file)
# # Add a new record to the existing object
# new_record = {
#     "file_name": "new_package.tgz",
#     "version": "1.0.0",
#     "url": "https://example.com/packages/new_package.tgz",
#     "hash": "sha256:abcdef1234567890"
# }
# data["new_record_key"] = new_record

# # Write the updated data back to the JSON file
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4) 

# import tarfile
# import json

# tgz_filename = 'dpm_temp.tgz'
# package_json_path = 'package.json'

# # Open the tgz file in read mode
# with tarfile.open(tgz_filename, 'r:gz') as tgz:
#     # Get the package.json file as a file object
#     package_json_file = tgz.extractfile(package_json_path)
    
#     if package_json_file:
#         # Read and decode the JSON content
#         package_json_content = package_json_file.read().decode('utf-8')
        
#         # Parse the JSON content
#         package_data = json.loads(package_json_content)
        
#         # Print or process the package data
#         print(package_data)

# import requests
# import tarfile
# import json
# from io import BytesIO

# url = 'https://github.com/derrick921213/package_manager_server/raw/main/software/dpm_test1.tgz'
# package_json_path = 'package.json'

# # Fetch the tgz file from the URL
# response = requests.get(url)

# if response.status_code == 200:
#     tgz_bytes = BytesIO(response.content)
    
#     with tarfile.open(fileobj=tgz_bytes, mode='r:gz') as tgz:
#         package_json_file = tgz.extractfile(package_json_path)
        
#         if package_json_file:
#             package_json_content = package_json_file.read().decode('utf-8')
#             package_data = json.loads(package_json_content)
#             print(package_data)
# else:
#     print('Failed to fetch the tgz file.')

# import os
# import tarfile

# source_folder = './src/temp/'
# output_filename = 'compressed_folder.tar.gz'

# with tarfile.open(output_filename, 'w:gz') as tar:
#     for root, dirs, files in os.walk(source_folder):
#         for file in files:
#             file_path = os.path.join(root, file)
#             arcname = os.path.relpath(file_path, source_folder)  # 获取文件相对于 source_folder 的路径
#             tar.add(file_path, arcname=arcname)
    
# print(f'Contents of folder "{source_folder}" have been compressed to "{output_filename}"')

# class command:
#     def __init__(self,app:str,action:str,argv:list=None):
#         self.app = app
#         self.action = action
#         if argv is not None and isinstance(argv,list):
#             self.argv = argv
# parsed = command("sha256","create",['test'])
# print(type(getattr(parsed,'argv')))


# commands = {
#     "hash": ["sign","add"],
#     "build": None,
#     "create": ["package","hash"],
#     "fix": ["add","del"]
# }
# print("good" if "signd" in commands["hash"] else "bad")
# import os
# file_dir = os.path.dirname(os.path.realpath('__file__'))
# print (file_dir)
# test = input('test: ')
# print(type(test))