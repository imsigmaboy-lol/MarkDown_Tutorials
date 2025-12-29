import os
import sys
import subprocess
import tempfile
import argparse

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
    parser = argparse.ArgumentParser(description="Process Luau bytecode dumper")
    
    parser.add_argument("-i", "--input", help="Input Luau file")
    parser.add_argument("-o", "--output", help="Output luauc file")
    
    args = parser.parse_args()
    input_file = args.input
    if not input_file:
        input_file = input("Enter your obfuscated file: ").strip()
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        sys.exit(1)
    with open(input_file, "r", encoding="utf-8") as f:
        output_of_bytecode_dumper_ig = f.read()
    bytecode_dumper = insert_bytecode_dump_script_ig_idl(output_of_bytecode_dumper_ig)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".luau", mode='w', encoding='utf-8') as tmp:
        tmp.write(bytecode_dumper)
        tmp_path = tmp.name
    
    try:
        proc = subprocess.run(["luau", tmp_path], capture_output=True)
        dumped = proc.stdout
        output_file = args.output
        if not output_file:
            output_file = input("Output file name (.luauc): ").strip()
        
        if not output_file.lower().endswith(".luauc"):
            output_file += ".luauc"
        
        output_file = make_unique_filename(output_file)
        with open(output_file, "wb") as f:
            f.write(dumped)
        
        print(f"[done] saved: {output_file}")
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
if __name__ == "__main__":
    main()
