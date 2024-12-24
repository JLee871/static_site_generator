import os
import shutil
from pathlib import Path
from markdown_to_html import markdown_to_html_node
from block_markdown import extract_title

def copy_files(source_dir_path, dest_dir_path):
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)
        print(f"cleaned directory {dest_dir_path}")   

    os.mkdir(dest_dir_path)
    print(f"made directory {dest_dir_path}")
    
    for filename in os.listdir(source_dir_path):
        source_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)           
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_dir_path)
            print(f"{filename} copied from {source_dir_path} to {dest_dir_path}")
        else:
            copy_files(source_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    from_template = open(template_path, "r")
    template = from_template.read()
    from_template.close()

    nodes = markdown_to_html_node(markdown)
    content = nodes.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    dest_dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    to_file = open(dest_path, 'w')
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)  
        if os.path.isfile(content_path):
            dest_path = Path(dest_path).with_suffix('.html')
            generate_page(content_path, template_path, dest_path)
        else:
            
            generate_pages_recursive(content_path, template_path, dest_path)
