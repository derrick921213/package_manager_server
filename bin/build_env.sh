#!/bin/bash
CMD="$(uname)"
BASE="/usr/local/DPM/"
BUILD_DIR="tools"
function download(){
    curl -o /tmp/fix_package https://github.com/derrick921213/package_manager_server/raw/main/tools/mac/fix_package
    curl -o /tmp/pk_ct https://github.com/derrick921213/package_manager_server/raw/main/tools/mac/pk_ct
    curl -o /tmp/sha256_create https://github.com/derrick921213/package_manager_server/raw/main/tools/mac/sha256_create
    sudo mv /tmp/fix_package "$BASE/$BUILD_DIR"
    sudo mv /tmp/pk_ct "$BASE/$BUILD_DIR"
    sudo mv /tmp/sha256_create "$BASE/$BUILD_DIR"
}
function check_dir(){
    if [[ ! -d "$BASE" || ! -d "$BASE/$BUILD_DIR" ]]; then
        sudo mkdir -p "$BASE/$BUILD_DIR"
    fi
}
function set_env(){
    if [ grep -q "export PATH='/usr/local/DPM/tools':$PATH" "$HOME/.zshrc" ]; then
        
    fi
}
function main(){
    if [[ "$CMD" == "Darwin" ]]; then
        cd $BASE/$BUILD_DIR
        check_dir()
        download()

        exit 0
    elif [[ "$CMD" == "Linux" ]]; then
        echo 'This is linux'
    fi
}
main()