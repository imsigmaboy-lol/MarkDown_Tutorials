# luaobfsufcator.com BYTECODE dumper
## Firstly run this to install the dependencies
```bash
termux-setup-storage; [ -x "$PREFIX/bin/wget" ] || pkg install -y wget; yes | pkg upgrade; cd "$HOME"; mkdir -p luau; cd luau; wget https://github.com/imsigmaboy-lol/luau/releases/download/aarch64/AARCH64.zip; unzip AARCH64.zip; rm -f AARCH64.zip; chmod +x luau luau-ast luau-reduce luau-bytecode luau-analyze luau-compile; for f in luau luau-ast luau-reduce luau-bytecode luau-analyze luau-compile; do ln -sf "$HOME/luau/$f" "$PREFIX/bin/$f"; done; cd
```
