# -*- coding: utf-8 -*-
"""
DIY参数化 · 资料自动生成工具（三板块版）
=========================================
【用法】
  把文档分别放进「资料」文件夹下的三个子文件夹：
    资料\教程\      → 显示在「教程」板块
    资料\白皮书\    → 显示在「白皮书」板块
    资料\宏文件\    → 显示在「宏文件」板块
  然后双击「更新资料.bat」自动生成 library-data.js。
  上传时把整个「资料」文件夹和 library-data.js 传到 GitHub 仓库。
"""
import os, re, datetime, json

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE, "资料")
OUT = os.path.join(BASE, "library-data.js")

# 板块 → 子文件夹 → 标签 → 允许的扩展名（None=全部）
CATEGORIES = [
    ("tutorials", "教程", "教程", None),
    ("whitepapers", "白皮书", "白皮书", None),
    ("macros", "宏文件", "宏文件", {".swb", ".swp", ".bas", ".dll", ".zip", ".txt", ".pdf", ".docx", ".doc"}),
]

EXT_MAP = {
    ".pdf": ("PDF", "PDF 文档"),
    ".doc": ("DOC", "Word 文档"),
    ".docx": ("DOCX", "Word 文档"),
    ".txt": ("TXT", "文本资料"),
    ".xlsx": ("XLSX", "表格资料"),
    ".xls": ("XLS", "表格资料"),
    ".ppt": ("PPT", "演示文稿"),
    ".pptx": ("PPTX", "演示文稿"),
    ".swb": ("SWB", "SW 宏文件"),
    ".swp": ("SWP", "SW 宏文件"),
    ".bas": ("BAS", "宏文件"),
    ".dll": ("DLL", "宏插件"),
    ".zip": ("ZIP", "压缩包"),
    ".jpg": ("JPG", "图片资料"),
    ".jpeg": ("JPEG", "图片资料"),
    ".png": ("PNG", "图片资料"),
}

DEFAULT_FAVORITES = [
    {"favKey": "book", "title": "机械设计手册", "desc": "非标设计必备工具书，标准件、材料、力学计算一站式查阅，参数化设计的知识底座。", "type": "BOOK", "meta": "工具书 · 推荐", "link": ""},
    {"favKey": "model", "title": "常用 3D 模型库", "desc": "TraceParts、米思米、嘉立创 FA 等模型库，选型即得 STEP，参数化建模的素材来源。", "type": "MODEL", "meta": "资源站 · 推荐", "link": ""},
    {"favKey": "tool", "title": "参数化选型计算器", "desc": "输送机、传动、夹紧机构等非标选型计算工具，把经验公式变成一键计算。", "type": "TOOL", "meta": "工具 · 推荐", "link": ""},
    {"favKey": "wiki", "title": "SolidWorks 帮助与论坛", "desc": "官方帮助文档与工程师社区，方程式、配置、宏的疑难问题都能找到答案。", "type": "WIKI", "meta": "资料站 · 推荐", "link": ""},
]


def load_old_data():
    try:
        with open(OUT, "r", encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
        m = re.search(r"window\.DIY_LIBRARY\s*=\s*(\{.*\});", text, re.S)
        if not m:
            return None
        obj = re.sub(r"([{,]\s*)([A-Za-z_$][\w$]*)\s*:", r'\1"\2":', m.group(1))
        return json.loads(obj)
    except Exception:
        return None


def scan_folder(folder, allow_ext=None):
    """递归扫描文件夹下所有支持的文档"""
    items = []
    if not os.path.isdir(folder):
        return items
    for root, _, files in os.walk(folder):
        for name in sorted(files):
            if name.startswith("~$") or name.startswith("."):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext not in EXT_MAP:
                continue
            if allow_ext is not None and ext not in allow_ext:
                continue
            path = os.path.join(root, name)
            size_kb = os.path.getsize(path) / 1024
            size_txt = f"{size_kb:.0f} KB" if size_kb < 1024 else f"{size_kb / 1024:.1f} MB"
            title = os.path.splitext(name)[0]
            tag, kind = EXT_MAP[ext]
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")
            # 相对「资料」的路径，保留子文件夹层级
            rel = os.path.relpath(path, DOCS_DIR).replace(os.sep, "/")
            items.append({
                "title": title,
                "desc": f"{kind} · {size_txt} · 更新于 {mtime}。点击「在线阅读」直接查看。",
                "type": tag,
                "status": "可下载",
                "meta": f"{tag} · {size_txt}",
                "link": f"资料/{rel}",
            })
    return items


def main():
    if not os.path.isdir(DOCS_DIR):
        os.makedirs(DOCS_DIR, exist_ok=True)
        print("已创建「资料」文件夹，请在其中建立 教程 / 白皮书 / 宏文件 三个子文件夹后重新运行。")
        input("按回车键退出...")
        return

    for _, sub, _, _ in CATEGORIES:
        d = os.path.join(DOCS_DIR, sub)
        if not os.path.isdir(d):
            os.makedirs(d, exist_ok=True)

    old = load_old_data() or {}
    favorites = old.get("favorites") or DEFAULT_FAVORITES

    result = {}
    total = 0
    for key, sub, label, allow in CATEGORIES:
        result[key] = scan_folder(os.path.join(DOCS_DIR, sub), allow)
        total += len(result[key])

    js = []
    js.append("/**")
    js.append(" * 本文件由「更新资料.bat」自动生成，请勿手动编辑！")
    js.append(" * 更新方法：把文档放进 资料\\教程、资料\\白皮书、资料\\宏文件 → 双击「更新资料.bat」")
    js.append(" */")
    js.append("window.DIY_LIBRARY = {")
    for key, sub, label, allow in CATEGORIES:
        js.append("  " + key + ": " + json.dumps(result[key], ensure_ascii=False, indent=2) + ",")
    js.append("  favorites: " + json.dumps(favorites, ensure_ascii=False, indent=2))
    js.append("};")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(js))

    print("=" * 46)
    print("生成完成！共 %d 个文档：" % total)
    for key, sub, label, allow in CATEGORIES:
        print("  [%s] %d 个" % (label, len(result[key])))
        for it in result[key]:
            print("    · %s" % it["title"])
    print("=" * 46)
    print("下一步：")
    print("  1. 把「资料」文件夹整个上传到 GitHub 仓库（保持 教程/白皮书/宏文件 结构）")
    print("  2. 把 library-data.js 上传到仓库根目录")
    print("  3. 等 1~2 分钟，刷新网页即可看到新资料")
    input("按回车键退出...")


if __name__ == "__main__":
    main()
