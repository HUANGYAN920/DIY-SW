/**
 * DIY参数化 · 图书馆 / 专题 / 收藏 资料数据
 * ==========================================
 * 【怎么更新资料】：
 * 1. 用记事本/编辑器打开本文件
 * 2. 找到对应的数组（library=图书馆 / topics=专题 / favorites=收藏）
 * 3. 复制一条现有条目，改内容即可；删条目直接删整行；加条目录粘贴一行
 * 4. 保存，把本文件上传到 GitHub 仓库（覆盖旧的 library-data.js）
 *    同时更新 index.html 里每张卡片的说明也可以——不过卡片会自动从本文件生成
 *
 * 【字段说明】：
 *   title    标题
 *   desc     简介
 *   type     左上角英文标签（如 WHITEPAPER / CASE / TOOL ...）
 *   status   状态标签（更新中 / 可下载 / 新增 ...）
 *   meta     底部灰色小字说明
 *   link     资料链接（可选）：填了会显示"查看资料 ↗"按钮
 *   favKey   仅收藏用：唯一标识（英文，不要重复）
 * ==========================================
 */
window.DIY_LIBRARY = {

  /* ---------- 图书馆 ---------- */
  library: [
    {
      title: "参数化设计白皮书",
      desc: "系统梳理非标自动化参数化设计的方法论：规律总结 → 规则定义 → 自动出图，含常见误区与落地路径。",
      type: "WHITEPAPER",
      status: "更新中",
      meta: "DOC · 全文陆续发布",
      link: ""
    },
    {
      title: "参数化案例集",
      desc: "典型非标零部件的参数化实践案例：标准件模板、系列化改型、自动出图与 BOM 的完整流程。",
      type: "CASE",
      status: "整理中",
      meta: "CASE · 案例讲解",
      link: ""
    },
    {
      title: "3 天培训教材",
      desc: "培训配套教材与练习素材：规律梳理表格、规则定义模板、出图规范清单，随课程发放。",
      type: "TRAINING",
      status: "可预约",
      meta: "TRAINING · 随课发放",
      link: ""
    },
    {
      title: "常见问题 FAQ",
      desc: "参数化设计入门常见问题解答：与二次开发的区别、支持的软件平台、学习路径建议等。",
      type: "FAQ",
      status: "更新中",
      meta: "FAQ · 持续更新",
      link: ""
    }
  ],

  /* ---------- 专题 ---------- */
  topics: [
    {
      title: "方法论专题：规律 → 规则 → 自动",
      desc: "参数化设计三步法详解：如何从产品变化中发现规律，把规律固化成规则，最终实现自动化设计。",
      type: "METHOD",
      status: "更新中",
      meta: "TOPIC · 01",
      link: ""
    },
    {
      title: "案例专题：系列化零件改型",
      desc: "典型非标零部件的参数化实战：改一个参数，模型、图纸、BOM 同步更新，效率提升数倍。",
      type: "CASE",
      status: "更新中",
      meta: "TOPIC · 02",
      link: ""
    },
    {
      title: "工具专题：参数化配置技巧",
      desc: "SOLIDWORKS 方程式、系列零件表、配置驱动的实用技巧与避坑指南。",
      type: "TOOL",
      status: "更新中",
      meta: "TOPIC · 03",
      link: ""
    },
    {
      title: "企业专题：参数化体系落地",
      desc: "从单点模板到企业级参数化标准体系的搭建路径，让知识在企业内传承。",
      type: "ENTERPRISE",
      status: "更新中",
      meta: "TOPIC · 04",
      link: ""
    }
  ],

  /* ---------- 收藏 ---------- */
  favorites: [
    {
      favKey: "book",
      title: "机械设计手册",
      desc: "非标设计必备工具书，标准件、材料、力学计算一站式查阅，参数化设计的知识底座。",
      type: "BOOK",
      meta: "工具书 · 推荐",
      link: ""
    },
    {
      favKey: "model",
      title: "常用 3D 模型库",
      desc: "TraceParts、米思米、嘉立创 FA 等模型库，选型即得 STEP，参数化建模的素材来源。",
      type: "MODEL",
      meta: "资源站 · 推荐",
      link: ""
    },
    {
      favKey: "tool",
      title: "参数化选型计算器",
      desc: "输送机、传动、夹紧机构等非标选型计算工具，把经验公式变成一键计算。",
      type: "TOOL",
      meta: "工具 · 推荐",
      link: ""
    },
    {
      favKey: "wiki",
      title: "SolidWorks 帮助与论坛",
      desc: "官方帮助文档与工程师社区，方程式、配置、宏的疑难问题都能找到答案。",
      type: "WIKI",
      meta: "资料站 · 推荐",
      link: ""
    }
  ]
};
