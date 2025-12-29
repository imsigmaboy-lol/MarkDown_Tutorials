# luaobfsufcator.com BYTECODE dumper
## Firstly
run this to install the dependencies
```bash
[ ! -d "$HOME/storage" ] && termux-setup-storage; [ -x "$PREFIX/bin/wget" ] || pkg install -y wget; pkg upgrade -y; cd "$HOME"; mkdir -p luau; cd luau; wget -N https://github.com/imsigmaboy-lol/luau/releases/download/aarch64/AARCH64.zip; unzip -o AARCH64.zip; rm -f AARCH64.zip; chmod +x luau luau-ast luau-reduce luau-bytecode luau-analyze luau-compile 2>/dev/null; for f in luau luau-ast luau-reduce luau-bytecode luau-analyze luau-compile; do ln -sf "$HOME/luau/$f" "$PREFIX/bin/$f"; done; cd
```
## Secondly
go to the directory of the obsufcated script you want to dump. example: cd "/storage/emulated/0/obsufcated_script.luau"


## Thirdly
run this
```bash
[ -x "$PREFIX/bin/python" ] || pkg install -y python;[ -f Dump_bytecode.py ] || wget "https://raw.githubusercontent.com/imsigmaboy-lol/Deobsufcaters_LUAU/refs/heads/main/Luaobsufactor.com/Dump_bytecode.py"
```
## Next
You should see a brand new file named "Dump_bytecode.py" this is (as the name suggets) the script that can dump the bytecode.

To use this brand new file, do 
```python
python Dump_bytecode.py
```
then from there it will prompt you for your input obsufcated file, and what u want the dumped output to be.
## OPTIONAL
if u wanna simplify usage in the CLI, you can use the flag -i OR --input which tells python what the obsufcated input is. Then -o  OR --output tells python what the output file should be from the input. You can also combine theses if you want to
EXAMPLE:
```python
python Dump_bytecode.py -i input.luau -o output.luauc
```
