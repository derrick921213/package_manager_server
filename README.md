# package_manager_server

## These package is make by myself

### Package modus

test.tar.gz
|- package.json(Every package must have it)
|- hashes.json(Every package must have it)
|- other file...

#### package.json

```json
{
  "name": "test",
  "file_name": "dpm_test1_0.0.1.tar.gz",
  "version": "0.0.1",
  "main_file": "test1.sh"
}
```

#### hashes.json
Use tools/sha256_create to Create anything package file hashes in hashes.json
`Useage ./sha256_create [Package location]` 
