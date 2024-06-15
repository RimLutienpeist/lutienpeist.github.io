import os
import yaml

def generate_yaml(root_dir, level=0):
    nav = []
    for name in os.listdir(root_dir):
        path = os.path.join(root_dir, name)
        if os.path.isdir(path):
            dir_content = generate_yaml(path, level+1)
            if dir_content:  # 只有当文件夹下有.md文件时，才将这个文件夹添加到yaml文件中
                dir_dict = {name: dir_content}
                nav.append(dir_dict)
        elif name.endswith('.md'):
            nav.append({name[:-3]: path})
    return nav

root_dir = '.'  # 根目录
nav = generate_yaml(root_dir)

with open('mkdocs.yml', 'w', encoding='utf8') as f:
    yaml.dump({'nav': nav}, f, allow_unicode=True)