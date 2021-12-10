"""
    ÞETTA ER EKKI HLUTI AF MEGINFORRITINU!!
"""

import os

CLASS_DIAGRAM_FILE = 'hönnun/útkoma/generated_class_diagram.puml'
CODE = '../CODE1/'

class Class:
    def __init__(self, name):
        self.name = name
        self.attributes = []
        self.methods = []
        self.imports = []
    def __str__(self):
        return 'class ' + self.name + ' {\n\t' + '\n\t'.join(self.attributes) + '\n\t' + '\n\t'.join(self.methods) + '\n}'

    def relations_str(self):
        str = ''
        for imp in self.imports:
            str += f'{self.name} ..> {imp}\n'
        return str

def analyze_classes(path):
    ## Bæta við import til að tengja líka
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        class_found = None
        reading_init = False
        imports = []
        for line in lines:
            if line.startswith("import ") or line.startswith("from "): #Import tengingar
                line = line.strip()
                import_name = line[line.index('import ')+7:]
                imports.append(import_name)
                #print("IMPORT:", )
            if line.startswith("class "):
                class_name = line[6:line.index(':')]
                class_found = Class(class_name)
                #print("class", class_found)
            if reading_init and line.strip().startswith('def '):
                reading_init = False
            if class_found is not None and line.strip().startswith('def __init__(self'):
                reading_init = True
            if reading_init and line.strip().startswith('self.') and '=' in line:
                line = line.strip()
                attribute_name = line[5:line.index('=')].replace(' ', '')
                class_found.attributes.append('- ' + attribute_name)
            if line.strip().startswith('def '):
                line = line.strip()
                method = line[4:line.index(':')]
                class_found.methods.append('+ ' + method)
        if class_found is not None:
            class_found.imports = imports

        return class_found



def main():
    print("@startuml")
    print("hide empty members")
    packages = {}
    for root, dirs, files in os.walk(CODE, topdown=False):
        #for name in dirs:
        #    print(os.path.join(root, name))
        for name in files:
            if name.endswith('.py'):
                clazz = analyze_classes(os.path.join(root, name))
                if clazz is not None:
                    if packages.get(root) is None:
                        packages[root] = []
                    packages[root].append(clazz)
    for key, value in packages.items():
        print('package', key.replace('../CODE1/', ''), '{')
        for clazz in packages[key]:
            #print(clazz.imports)
            print(clazz)
        print('}')
    for key, value in packages.items():
        for clazz in packages[key]: #Vensl
            print(clazz.relations_str())
    #print(packages)
    print("@enduml")

if __name__ == '__main__':
    main()
