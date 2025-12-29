def insert_bytecode_dump_script_ig_idl(output_of_bytecode_dumper_ig: str) -> str:
    text_to_find_idk_what_to_name_this = "local function v20(v31,v32,v33)"
    bytecode_dump_script_ig_idl = (
        "print(v16)"
    )
    return output_of_bytecode_dumper_ig.replace(text_to_find_idk_what_to_name_this, bytecode_dump_script_ig_idl + text_to_find_idk_what_to_name_this, 1)
def main():
    with open(input("enter your obsufcated file: "), "r", encoding="utf-8") as f:
        output_of_bytecode_dumper_ig = f.read()
    bytecode_dumper = insert_bytecode_dump_script_ig_idl(output_of_bytecode_dumper_ig)
    with open("output.luau", "w", encoding="utf-8") as f:
        f.write(bytecode_dumper)
if __name__ == "__main__":
    main()
