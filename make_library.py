# -*- coding: utf-8 -*-
"""
DIY参数化 · 资料自动生成工具
==============================
【用法】把 PDF / Word 文档放进本目录下的「资料」文件夹，
       双击「更新资料.bat」即可自动生成 library-data.js，
       然后把「资料」文件夹和 library-data.js 一起上传到 GitHub 仓库。
"""
import os, re, datetime, json

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE, "资料")
OUT = os.path.join(BASE, "library-data.js")

EXT_MAP = {
    ".pdf": ("PDF", "PDF 文档"),
    ".doc": ("DOC", "Word 文档"),
    ".docx": ("DOCX", "Word 文档"),
    ".txt": ("TXT", "文本资料"),
    ".xlsx": ("XLSX", "表格资料"),
    ".xls": ("XLS", "表格资料"),
    ".ppt": ("PPT", "演示文稿"),
    ".pptx": ("PPTX", "演示文稿"),
    ".jpg": ("JPG", "图片资料"),
    ".jpeg": ("JPEG", "图片资料"),
    ".png": ("PNG", "图片资料"),
    ".zip": ("ZIP", "压缩包"),
}

# 内置默认专题（如旧数据可读则用旧数据）
DEFAULT_TOPICS = [
    {"title": "方法论专题：规律 → 规则 → 自动", "desc": "参数化设计三步法详解：如何从产品变化中发现规律，把规律固化成规则，最终实现自动化设计。", "type": "METHOD", "status": "更新中", "meta": "TOPIC · 01", "link": ""},
    {"title": "案例专题：系列化零件改型", "desc": "典型非标零部件的参数化实战：改一个参数，模型、图纸、BOM 同步更新，效率提升数倍。", "type": "CASE", "status": "更新中", "meta": "TOPIC · 02", "link": ""},
    {"title": "工具专题：参数化配置技巧", "desc": "SOLIDWORKS 方程式、系列零件表、配置驱动的实用技巧与避坑指南。", "type": "TOOL", "status": "更新中", "meta": "TOPIC · 03", "link": ""},
    {"title": "企业专题：参数化体系落地", "desc": "从单点模板到企业级参数化标准体系的搭建路径，让知识在企业内传承。", "type": "ENTERPRISE", "status": "更新中", "meta": "TOPIC · 04", "link": ""},
]

# 内置默认收藏
DEFAULT_FAVORITES = [
    {"favKey": "book", "title": "机械设计手册", "desc": "非标设计必备工具书，标准件、材料、力学计算一站式查阅，参数化设计的知识底座。", "type": "BOOK", "meta": "工具书 · 推荐", "link": ""},
    {"favKey": "model", "title": "常用 3D 模型库", "desc": "TraceParts、米思米、嘉立创 FA 等模型库，选型即得 STEP，参数化建模的素材来源。", "type": "MODEL", "meta": "资源站 · 推荐", "link": ""},
    {"favKey": "tool", "title": "参数化选型计算器", "desc": "输送机、传动、夹紧机构等非标选型计算工具，把经验公式变成一键计算。", "type": "TOOL", "meta": "工具 · 推荐", "link": ""},
    {"favKey": "wiki", "title": "SolidWorks 帮助与论坛", "desc": "官方帮助文档与工程师社区，方程式、配置、宏的疑难问题都能找到答案。", "type": "WIKI", "meta": "资料站 · 推荐", "link": ""},
]


def load_old_data():
    """尝试从旧文件读取 topics / favorites（JS 风格对象转 JSON）"""
    try:
        with open(OUT, "r", encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
        text = re.sub(r"//[^\n]*", "", text)
        m = re.search(r"window\.DIY_LIBRARY\s*=\s*(\{.*\});", text, re.S)
        if not m:
            return None
        obj = m.group(1)
        obj = re.sub(r"([{,]\s*)([A-Za-z_$][\w$]*)\s*:", r'\1"\2":', obj)
        return json.loads(obj)
    except Exception:
        return None


def build_library():
    items = []
    if os.path.isdir(DOCS_DIR):
        files = sorted(os.listdir(DOCS_DIR))
        for name in files:
            if name.startswith("~$") or name.startswith("."):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext not in EXT_MAP:
                continue
            path = os.path.join(DOCS_DIR, name)
            size_kb = os.path.getsize(path) / 1024
            size_txt = f"{size_kb:.0f} KB" if size_kb < 1024 else f"{size_kb / 1024:.1f} MB"
            title = os.path.splitext(name)[0]
            tag, kind = EXT_MAP[ext]
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")
            items.append({
                "title": title,
                "desc": f"{kind} · {size_txt} · 更新于 {mtime}。点击「在线阅读」直接查看。",
                "type": tag,
                "status": "可下载",
                "meta": f"{tag} · {size_txt}",
                "link": f"资料/{name}",
            })
    return items


def main():
    if not os.path.isdir(DOCS_DIR):
        os.makedirs(DOCS_DIR, exist_ok=True)
        print("已创建「资料」文件夹，请把文档放进去，然后重新双击本工具。")
        input("按回车键退出...")
        return

    old = load_old_data() or {}
    topics = old.get("topics") or DEFAULT_TOPICS
    favorites = old.get("favorites") or DEFAULT_FAVORITES
    library = build_library()

    js = []
    js.append("/**")
    js.append(" * 本文件由「更新资料.bat」自动生成，请勿手动编辑！")
    js.append(" * 更新方法：把文档放进「资料」文件夹 → 双击「更新资料.bat」")
    js.append(" */")
    js.append("window.DIY_LIBRARY = {")
    js.append("  library: " + json.dumps(library, ensure_ascii=False, indent=2) + ",")
    js.append("  topics: " + json.dumps(topics, ensure_ascii=False, indent=2) + ",")
    js.append("  favorites: " + json.dumps(favorites, ensure_ascii=False, indent=2))
    js.append("};")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(js))

    print("=" * 46)
    print("生成完成！资料文件夹中共有 %d 个文档：" % len(library))
    for it in library:
        print("  · %s" % it["title"])
    print("=" * 46)
    print("下一步：")
    print("  1. 把「资料」文件夹里的文档上传到 GitHub 仓库 docs 文件夹")
    print("  2. 把 library-data.js 上传到仓库根目录")
    print("  3. 等 1~2 分钟，刷新网页即可看到新资料")
    input("按回车键退出...")


if __name__ == "__main__":
    main()
