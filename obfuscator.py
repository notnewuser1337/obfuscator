import os
import base64
from sys import argv

randomizer = 100
obu_text = '_allahuakbar_123_1337_7331' * 100

def obfuscate(content):
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{obu_text} = ""\n'
    for _ in range(int(len(b64_content) / randomizer) + 1):
        _str = ''
        for char in b64_content[index:index + obu_text]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{obu_text} += "{_str}"\n'
        index += randomizer
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode{obu_text}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code

def main():

    try:
        path = argv[1]
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()

        obfuscated_content = obfuscate(file_content)

        with open(f'{path.split(".")[0]} (obfuscated).py', 'w') as file:
            file.write(obfuscated_content)

        print('[+] obfuscated' + os.file.name )

    except: 
        
         if not os.path.isfile(path) or not path.endswith('.py'):
            print('Error, not a python file')
         
         else: 

            if not os.path.exists(path):
                print('Error, file not found')
            

if __name__ == '__main__':
    main()
