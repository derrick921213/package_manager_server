# package_manager_server

## These package is make by myself

### Package structure
```
dpm_test1_0.0.1.tgz
|- package.json(Every package must have it)
|- hashes.json(Every package must have it)
|- other file...
```
### init package
```shell
python dpm_server.py init
```
### Build the package
```shell
python dpm_server.py build
```
### set package hash
```shell
python dpm_server.py hash
```
### fix repo package.json
```shell
python dpm_server.py fix add|del
```
### autoRun
```shell
python dpm_server.py all
```

#### package.json
name: Is this package name.
file_name: Must be this package archive name.
main_file: Is ths package executable or main file. 
```json
{
  "name": "test",
  "file_name": "dpm_test1_0.0.1.tgz",
  "version": "0.0.1",
  "main_file": "test1.sh",
  "hash": ""
}
```
### command run list
1. init -> hash -> build -> fix(add|del)<br>or<br>
2. init -> all