def insert_bytecode_dump_script_ig_idl(output_of_bytecode_dumper_ig: str) -> str:
    text_to_find_idk_what_to_name_this = "local function v20(v31,v32,v33)"
    bytecode_dump_script_ig_idl = (
        "function DecodeBase64(a)local b='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'"
        "local c={}a=string.gsub(a,'[^'..b..'=]','')local d={}for e=1,#b do d[string.sub(b,e,e)]=e-1 end;"
        "local f=0;local g=0;for e=1,#a do local h=string.sub(a,e,e)if h~='='then f=f*64+d[h]g=g+6;"
        "if g>=8 then g=g-8;local i=math.floor(f/2^g)f=f%2^g;table.insert(c,string.char(i))end end end;"
        "return table.concat(c)end;"
        "function EncodeBase64(a)local b='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'"
        "local c={}local j={string.byte(a,1,#a)}for e=1,#j,3 do local k=j[e]local l=j[e+1]or 0;"
        "local m=j[e+2]or 0;local n=bit32.lshift(k,16)+bit32.lshift(l,8)+m;"
        "local o=bit32.band(bit32.rshift(n,18),63)local p=bit32.band(bit32.rshift(n,12),63)"
        "local q=bit32.band(bit32.rshift(n,6),63)local r=bit32.band(n,63)"
        "table.insert(c,b:sub(o+1,o+1))table.insert(c,b:sub(p+1,p+1))"
        "if e+1<=#j then table.insert(c,b:sub(q+1,q+1))else table.insert(c,'=')end;"
        "if e+2<=#j then table.insert(c,b:sub(r+1,r+1))else table.insert(c,'=')end end;"
        "return table.concat(c)end;local s=EncodeBase64(v16)print(s);"
    )
    return output_of_bytecode_dumper_ig.replace(text_to_find_idk_what_to_name_this, bytecode_dump_script_ig_idl + text_to_find_idk_what_to_name_this, 1)
def main():
    with open("input.luau", "r", encoding="utf-8") as f:
        output_of_bytecode_dumper_ig = f.read()
    bytecode_dumper = insert_bytecode_dump_script_ig_idl(output_of_bytecode_dumper_ig)
    with open("output.luau", "w", encoding="utf-8") as f:
        f.write(bytecode_dumper)
if __name__ == "__main__":
    main()
