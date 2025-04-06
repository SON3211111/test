import os

folder_path = 'templates'  # HTML 있는 폴더
old_path = '../static/img/'
new_path = '/static/img/'

for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content.replace(old_path, new_path)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("경로 원복 완료! (Flask용)")
