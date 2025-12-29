import os
import sys
import subprocess
import tempfile

def make_unique_filename(name):
    if not os.path.exists(name):
        return name
    base, ext = os.path.splitext(name)
    n = 1
    new = f"{base}({n}){ext}"
    while os.path.exists(new):
        n += 1
        new = f"{base}({n}){ext}"
    return new

def insert_bytecode_dump_script_ig_idl(output_of_bytecode_dumper_ig: str) -> str:
    text_to_find_idk_what_to_name_this = "local function v20(v31,v32,v33)"
    bytecode_dump_script_ig_idl = "print(v16)\n"
    return output_of_bytecode_dumper_ig.replace(
        text_to_find_idk_what_to_name_this,
        bytecode_dump_script_ig_idl + text_to_find_idk_what_to_name_this,
        1
    )

def main():
    args = sys.argv[1:]
    output_name = None
    input_name = None
    if len(args) >= 2 and args[0] == "-o":
        output_name = args[1]
        if len(args) >= 3:
            input_name = args[2]
    elif len(args) >= 1:
        input_name = args[0]
    if not input_name:
        input_name = input("enter your obsufcated file: ").strip()
    with open(input_name, "r", encoding="utf-8") as f:
        output_of_bytecode_dumper_ig = f.read()
    bytecode_dumper = insert_bytecode_dump_script_ig_idl(output_of_bytecode_dumper_ig)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".luau") as tmp:
        tmp.write(bytecode_dumper.encode("utf-8"))
        tmp_path = tmp.name

    proc = subprocess.run(["luau", tmp_path], capture_output=True, text=True)
    dumped = proc.stdout
    if not output_name:
        output_name = input("output file name (.luac): ").strip()
    if not output_name.lower().endswith(".luac"):
        output_name += ".luac"

    output_name = make_unique_filename(output_name)

    with open(output_name, "w", encoding="utf-8") as f:
        f.write(dumped)
if __name__ == "__main__":
    main()
