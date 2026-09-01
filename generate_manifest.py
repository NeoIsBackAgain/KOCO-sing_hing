import os
import json

images_dir = "images"
manifest = {}

for folder_name in os.listdir(images_dir):
    folder_path = os.path.join(images_dir, folder_name)
    if os.path.isdir(folder_path):
        files = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
        ]
        # 按文件名排序 (01.jpg, 02.jpg...)
        files.sort()
        if files:
            manifest[folder_name] = files

with open("images-manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"完成！共找到 {len(manifest)} 个项目文件夹")