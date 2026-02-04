import os
from PIL import Image

# ================= 配置区域 =================
# 图片文件夹路径
SOURCE_DIR = 'source/img' 

# JPG 质量 (1-95)，推荐 75，既能大幅减小体积，肉眼又看不出区别
QUALITY = 75

# 是否删除原图？ (True: 删除原有的 PNG/大图, False: 保留)
# 建议设为 True，因为我们要解决 Cloudflare 的 25MB 限制
REPLACE_ORIGINAL = True 
# ===========================================

def get_size_mb(file_path):
    return os.path.getsize(file_path) / (1024 * 1024)

def compress_to_jpg(directory):
    count = 0
    saved_space = 0

    print(f"🚀 开始扫描文件夹: {directory} ...")

    for root, dirs, files in os.walk(directory):
        for file in files:
            # 扫描常见图片格式 (排除已经是 .jpg 的小图，避免重复压缩)
            if file.lower().endswith(('.png', '.bmp', '.tiff', '.jpeg')):
                file_path = os.path.join(root, file)
                file_size = get_size_mb(file_path)

                # 设定阈值：大于 1MB 的图片才处理 (你可以根据需要修改，比如 0.5)
                if file_size > 1: 
                    print(f"\n📸 发现大图: {file} ({file_size:.2f} MB)")
                    
                    try:
                        with Image.open(file_path) as img:
                            # 关键步骤：JPG 不支持透明通道 (Alpha)
                            # 如果是 RGBA (透明 PNG)，必须转为 RGB (白色背景)，否则会报错
                            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                                print("   ⚠️  检测到透明通道，自动转换为白色背景...")
                                bg = Image.new('RGB', img.size, (255, 255, 255))
                                bg.paste(img, mask=img.split()[3]) # 3 is the alpha channel
                                img = bg
                            elif img.mode != 'RGB':
                                img = img.convert('RGB')
                            
                            # 构建新的文件名 (.jpg)
                            new_file_name = os.path.splitext(file)[0] + ".jpg"
                            new_file_path = os.path.join(root, new_file_name)

                            # 保存为 JPG，开启 optimize 优化体积
                            img.save(new_file_path, 'JPEG', quality=QUALITY, optimize=True)
                            
                            new_size = get_size_mb(new_file_path)
                            change = file_size - new_size
                            saved_space += change
                            count += 1
                            
                            print(f"   ✅ 转换成功: {new_file_name} ({new_size:.2f} MB)")
                            print(f"   📉 瘦身: {change:.2f} MB")

                            # 删除原文件（解决 Cloudflare 报错的关键）
                            if REPLACE_ORIGINAL and file_path != new_file_path:
                                os.remove(file_path)
                                print("   🗑️  已删除原文件")

                    except Exception as e:
                        print(f"   ❌ 处理失败: {e}")

    print(f"\n🎉 处理完成！共转换 {count} 张图片，累计节省空间 {saved_space:.2f} MB")

if __name__ == '__main__':
    if os.path.exists(SOURCE_DIR):
        compress_to_jpg(SOURCE_DIR)
    else:
        print(f"❌ 错误: 找不到文件夹 '{SOURCE_DIR}'，请检查路径。")