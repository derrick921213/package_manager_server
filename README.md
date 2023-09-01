# package_manager_server

## These package is make by myself

### Package structure
```
dpm_test1_0.0.1.tgz
|- package.json(Every package must have it)
|- hashes.json(Every package must have it)
|- other file...
```
### Build the package
Use tools/pk_ct to build .tgz file

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
  "hash": "sha256:c90832bd747eaa17dd9df5f725e9338a85197a5d498669ac3b034d280de13d25"
}
```
### command run list
init -> hash -> build -> fix(add|del)