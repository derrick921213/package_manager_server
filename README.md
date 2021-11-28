# package_manager_server

## These package is make by myself

### Package structure

dpm_test1_0.0.1.tgz
|- package.json(Every package must have it)
|- hashes.json(Every package must have it)
|- other file...

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
  "main_file": "test1.sh"
}
```

#### hashes.json
Use tools/sha256_create to Create anything package file hashes in hashes.json
`Useage ./sha256_create [Package location]` 
