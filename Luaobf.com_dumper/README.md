# luaobfsufcator.com BYTECODE dumper
## Firstly
run this to install the dependencies
```bash
[ ! -d "$HOME/storage" ] && termux-setup-storage; [ -x "$PREFIX/bin/wget" ] || pkg install -y wget; pkg upgrade -y; cd "$HOME"; mkdir -p luau; cd luau; wget -N https://github.com/imsigmaboy-lol/luau/releases/download/aarch64/AARCH64.zip; unzip -o AARCH64.zip; rm -f AARCH64.zip; chmod +x luau luau-ast luau-reduce luau-bytecode luau-analyze luau-compile 2>/dev/null; for f in luau luau-ast luau-reduce luau-bytecode luau-analyze luau-compile; do ln -sf "$HOME/luau/$f" "$PREFIX/bin/$f"; done; cd
```
## Secondly
go to the directory of the obsufcated script you want to dump. example: cd "/storage/emulated/0/obsufcated_script.luau"
##Thirdly
run this
```bash
wget "
```
