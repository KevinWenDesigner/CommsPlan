"""
唐都医院宣传片方案 - HTML转图片工具
自动将8页PPT截图保存为PNG图片
"""

import os
import time
from playwright.sync_api import sync_playwright

def capture_slides():
    """截取HTML的所有幻灯片页面"""
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, "唐都医院烧伤整形科50周年宣传片方案.html")
    
    # 创建输出目录
    output_dir = os.path.join(current_dir, "宣传片方案图片")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("🎬 开始生成宣传片方案图片...")
    print(f"📁 输出目录: {output_dir}")
    
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # 打开HTML文件
        page.goto(f'file:///{html_file}')
        
        # 等待页面加载完成
        time.sleep(2)
        
        # 总共8页
        total_slides = 8
        
        for i in range(total_slides):
            print(f"📸 正在截取第 {i + 1} 页...")
            
            # 等待动画完成
            time.sleep(1)
            
            # 截图
            screenshot_path = os.path.join(output_dir, f"第{i + 1}页.png")
            page.screenshot(path=screenshot_path, full_page=False)
            
            print(f"✅ 第 {i + 1} 页已保存: 第{i + 1}页.png")
            
            # 如果不是最后一页，点击下一页按钮
            if i < total_slides - 1:
                page.click('#nextBtn')
                time.sleep(0.5)
        
        browser.close()
    
    print("\n✨ 所有图片生成完成！")
    print(f"📂 图片保存在: {output_dir}")
    print(f"🎉 共生成 {total_slides} 张图片")

if __name__ == "__main__":
    try:
        capture_slides()
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print("\n💡 请确保已安装 playwright:")
        print("   pip install playwright")
        print("   playwright install chromium")

