https://huangyan920.github.io/DIY-SW/ 体验网址
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DIY参数化 · 非标自动化参数化设计</title>
<meta name="description" content="只要变化有规律，就可实现自动设计。不写代码、不做二次开发，自己总结变化规律，自主定义参数化设计，培训3天包教包会。">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' rx='9' fill='%230B2A4A'/%3E%3Ccircle cx='20' cy='20' r='13' stroke='%23F59E0B' stroke-width='3' fill='none'/%3E%3Ccircle cx='20' cy='20' r='5.5' fill='%2335C2E8'/%3E%3C/svg%3E">
<style>
  :root{
    --navy:#0B2A4A;
    --navy-2:#123A63;
    --blue:#1E6FD9;
    --blue-light:#4D94EA;
    --cyan:#35C2E8;
    --orange:#F59E0B;
    --ink:#1B2A3A;
    --gray:#5A6B7B;
    --line:#E3EAF2;
    --bg:#F5F8FC;
    --white:#fff;
    --radius:14px;
    --shadow:0 10px 30px rgba(11,42,74,.10);
    --font:"Microsoft YaHei","PingFang SC","Segoe UI",sans-serif;
    --mono:"Consolas","Courier New",monospace;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{font-family:var(--font);color:var(--ink);background:var(--bg);line-height:1.7}
  a{text-decoration:none;color:inherit}
  img{max-width:100%}

  /* ===== 导航 ===== */
  header{
    position:fixed;top:0;left:0;right:0;z-index:100;
    background:rgba(11,42,74,.96);backdrop-filter:blur(8px);
    border-bottom:1px solid rgba(255,255,255,.08);
  }
  .nav-wrap{max-width:1180px;margin:0 auto;padding:0 24px;height:64px;display:flex;align-items:center;justify-content:space-between}
  .logo{display:flex;align-items:center;gap:10px;font-weight:700;font-size:20px;color:#fff;letter-spacing:1px}
  .logo svg{flex-shrink:0}
  .logo b{color:var(--orange)}
  nav{display:flex;gap:28px}
  nav a{color:rgba(255,255,255,.82);font-size:15px;transition:color .2s}
  nav a:hover{color:var(--orange)}
  .menu-btn{display:none;background:none;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:8px;padding:6px 12px;font-size:14px;cursor:pointer}

  /* ===== Hero ===== */
  .hero{
    position:relative;color:#fff;padding:150px 24px 110px;
    background:
      radial-gradient(1000px 500px at 80% -10%,rgba(53,194,232,.22),transparent 60%),
      radial-gradient(800px 400px at 10% 110%,rgba(245,158,11,.16),transparent 60%),
      linear-gradient(160deg,var(--navy) 0%,var(--navy-2) 55%,#0D3358 100%);
    overflow:hidden;
  }
  .hero::before{ /* 图纸网格 */
    content:"";position:absolute;inset:0;opacity:.14;
    background-image:
      linear-gradient(rgba(255,255,255,.35) 1px,transparent 1px),
      linear-gradient(90deg,rgba(255,255,255,.35) 1px,transparent 1px);
    background-size:44px 44px;
    mask-image:radial-gradient(ellipse at 50% 40%,#000 30%,transparent 75%);
  }
  .hero-inner{position:relative;max-width:1180px;margin:0 auto;text-align:center}
  .hero-tag{
    display:inline-flex;align-items:center;gap:8px;
    border:1px solid rgba(255,255,255,.25);border-radius:999px;
    padding:6px 18px;font-size:13px;letter-spacing:2px;color:var(--cyan);margin-bottom:26px;
  }
  .hero-tag::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--cyan);animation:blink 1.6s infinite}
  @keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
  .hero h1{font-size:clamp(30px,5vw,54px);line-height:1.25;font-weight:800;letter-spacing:2px}
  .hero h1 .hl{color:var(--orange)}
  .hero .sub{margin:22px auto 0;max-width:640px;font-size:clamp(15px,2vw,18px);color:rgba(255,255,255,.85)}
  .hero .slogan{margin-top:38px;font-family:var(--mono);font-size:clamp(14px,2vw,17px);color:var(--cyan);letter-spacing:1px}
  .hero-cta{margin-top:44px;display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
  .btn{display:inline-flex;align-items:center;gap:8px;padding:13px 34px;border-radius:10px;font-size:16px;font-weight:600;transition:transform .2s,box-shadow .2s}
  .btn:hover{transform:translateY(-2px)}
  .btn-primary{background:var(--orange);color:#0B2A4A;box-shadow:0 8px 24px rgba(245,158,11,.35)}
  .btn-ghost{border:1.5px solid rgba(255,255,255,.5);color:#fff}
  .btn-ghost:hover{border-color:var(--orange);color:var(--orange)}

  /* ===== 卖点条 ===== */
  .strip{background:var(--white);border-bottom:1px solid var(--line)}
  .strip-inner{max-width:1180px;margin:0 auto;padding:18px 24px;display:flex;flex-wrap:wrap;gap:10px;justify-content:center}
  .strip span{font-size:14px;color:var(--navy);background:#EEF4FB;border-radius:8px;padding:7px 16px;font-weight:600}
  .strip span b{color:var(--orange)}

  /* ===== 通用区 ===== */
  section{padding:90px 24px}
  .wrap{max-width:1180px;margin:0 auto}
  .sec-head{text-align:center;margin-bottom:56px}
  .sec-head .kicker{font-family:var(--mono);color:var(--blue);letter-spacing:3px;font-size:13px}
  .sec-head h2{font-size:clamp(24px,3.5vw,36px);color:var(--navy);font-weight:800;margin-top:10px;letter-spacing:1px}
  .sec-head p{color:var(--gray);margin-top:12px;max-width:620px;margin-left:auto;margin-right:auto}

  /* ===== 核心主张 ===== */
  .claim{background:var(--navy);color:#fff}
  .claim .sec-head h2{color:#fff}
  .claim-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:20px}
  .claim-card{
    background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
    border-radius:var(--radius);padding:30px 24px;transition:transform .25s,border-color .25s;
  }
  .claim-card:hover{transform:translateY(-6px);border-color:var(--orange)}
  .claim-card .num{font-family:var(--mono);font-size:13px;color:var(--orange);letter-spacing:2px}
  .claim-card h3{font-size:19px;margin:12px 0 8px}
  .claim-card p{font-size:14px;color:rgba(255,255,255,.72)}
  .claim-card .cross{color:rgba(255,255,255,.4);font-size:13px}

  /* ===== 服务 ===== */
  .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:22px}
  .card{background:var(--white);border:1px solid var(--line);border-radius:var(--radius);padding:34px 28px;box-shadow:var(--shadow);transition:transform .25s,box-shadow .25s}
  .card:hover{transform:translateY(-6px);box-shadow:0 18px 40px rgba(11,42,74,.16)}
  .card .ico{width:52px;height:52px;border-radius:12px;background:linear-gradient(135deg,var(--blue),var(--cyan));display:flex;align-items:center;justify-content:center;margin-bottom:18px}
  .card h3{font-size:19px;color:var(--navy);margin-bottom:10px}
  .card p{font-size:14px;color:var(--gray)}
  .card ul{list-style:none;margin-top:12px}
  .card li{font-size:13.5px;color:var(--gray);padding:3px 0 3px 20px;position:relative}
  .card li::before{content:"▸";position:absolute;left:0;color:var(--orange)}

  /* ===== 培训 ===== */
  .training{background:var(--white)}
  .train-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:44px;align-items:center}
  .train-steps{display:flex;flex-direction:column;gap:16px}
  .step{display:flex;gap:16px;align-items:flex-start}
  .step .no{flex-shrink:0;width:44px;height:44px;border-radius:50%;background:var(--navy);color:var(--orange);display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-weight:700}
  .step h4{font-size:17px;color:var(--navy)}
  .step p{font-size:14px;color:var(--gray)}
  .train-side{background:linear-gradient(160deg,var(--navy),var(--navy-2));color:#fff;border-radius:var(--radius);padding:38px 32px}
  .train-side h3{font-size:22px;margin-bottom:18px}
  .train-side li{list-style:none;padding:9px 0 9px 26px;position:relative;font-size:15px;border-bottom:1px dashed rgba(255,255,255,.15)}
  .train-side li:last-child{border-bottom:none}
  .train-side li::before{content:"✓";position:absolute;left:0;color:var(--orange);font-weight:700}
  .train-side .big{margin-top:20px;font-size:26px;font-weight:800;color:var(--orange);text-align:center;letter-spacing:2px}

  /* ===== 平台 ===== */
  .platforms{display:flex;flex-wrap:wrap;gap:14px;justify-content:center}
  .platforms span{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 26px;font-weight:600;color:var(--navy);box-shadow:0 4px 14px rgba(11,42,74,.06)}

  /* ===== 联系 ===== */
  .contact{background:linear-gradient(160deg,var(--navy) 0%,var(--navy-2) 100%);color:#fff;text-align:center}
  .contact h2{font-size:clamp(24px,3.5vw,36px);font-weight:800}
  .contact .p{margin:16px auto 0;max-width:560px;color:rgba(255,255,255,.8)}
  .contact .cta{margin-top:36px}
  .contact .note{margin-top:26px;font-size:13px;color:rgba(255,255,255,.5)}

  footer{background:#081E33;color:rgba(255,255,255,.55);text-align:center;padding:26px 20px;font-size:13px}

  /* ===== 动画 ===== */
  .reveal{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease}
  .reveal.on{opacity:1;transform:none}

  @media(max-width:860px){
    nav{display:none;position:absolute;top:64px;left:0;right:0;background:var(--navy);flex-direction:column;padding:16px 24px;gap:16px}
    nav.open{display:flex}
    .menu-btn{display:block}
    .train-grid{grid-template-columns:1fr}
    section{padding:64px 20px}
  }
</style>
</head>
<body>

<!-- ========== 导航 ========== -->
<header>
  <div class="nav-wrap">
    <a class="logo" href="#top">
      <svg width="34" height="34" viewBox="0 0 40 40" fill="none">
        <circle cx="20" cy="20" r="16" stroke="#F59E0B" stroke-width="3"/>
        <circle cx="20" cy="20" r="7" fill="#35C2E8"/>
        <path d="M20 2v7M20 31v7M2 20h7M31 20h7" stroke="#4D94EA" stroke-width="3" stroke-linecap="round"/>
      </svg>
      DIY<b>参数化</b>
    </a>
    <nav id="nav">
      <a href="#claim">核心理念</a>
      <a href="#service">服务内容</a>
      <a href="#training">3天培训</a>
      <a href="#platform">支持平台</a>
      <a href="#contact">联系我</a>
    </nav>
    <button class="menu-btn" onclick="document.getElementById('nav').classList.toggle('open')">☰ 菜单</button>
  </div>
</header>

<!-- ========== Hero ========== -->
<div class="hero" id="top">
  <div class="hero-inner">
    <span class="hero-tag">非标自动化 · 参数化设计</span>
    <h1>只要变化有规律，<br class="hide"><span class="hl">就能实现自动设计</span></h1>
    <p class="sub">专注非标自动化参数化设计：把重复的建模、改图、出BOM，变成一次性的规则定义。让设计经验沉淀下来，让新工程师像老师傅一样有经验。</p>
    <div class="slogan">&lt; No Code · No SDK · Just Rules &gt;</div>
    <div class="hero-cta">
      <a class="btn btn-primary" href="#service">了解服务</a>
      <a class="btn btn-ghost" href="#contact">预约培训</a>
    </div>
  </div>
</div>

<!-- ========== 卖点条 ========== -->
<div class="strip">
  <div class="strip-inner">
    <span>不写代码</span><span>不做二次开发</span><span>规律自己总结</span><span>参数自主定义</span><span>经验不外泄</span><span>培训<b>3天</b>包教包会</span>
  </div>
</div>

<!-- ========== 核心主张 ========== -->
<section class="claim" id="claim">
  <div class="wrap">
    <div class="sec-head reveal">
      <div class="kicker">PHILOSOPHY</div>
      <h2>核心理念：把设计交给规律</h2>
      <p>我不是卖软件给你，而是教你掌握一种方法——自己总结变化规律，自己定义参数规则，从此掌握设计的主动权。</p>
    </div>
    <div class="claim-grid">
      <div class="claim-card reveal">
        <div class="num">/ 01</div>
        <h3>零门槛</h3>
        <p>不需要二次开发，不需要写代码，普通工程师也能上手。</p>
        <div class="cross">✕ 编程 ✕ 脚本 ✕ API</div>
      </div>
      <div class="claim-card reveal">
        <div class="num">/ 02</div>
        <h3>自主可控</h3>
        <p>自己总结变化规律，自主定义规则，不再依赖软件服务商，自由。</p>
        <div class="cross">✕ 受制于人 ✕ 排队等更新</div>
      </div>
      <div class="claim-card reveal">
        <div class="num">/ 03</div>
        <h3>安全放心</h3>
        <p>设计经验不出企业、不出电脑，安全有保障，知识产权不外泄。</p>
        <div class="cross">✕ 上传云端 ✕ 数据外流</div>
      </div>
      <div class="claim-card reveal">
        <div class="num">/ 04</div>
        <h3>效率倍增</h3>
        <p>系列化产品改参即得：自动生成3D模型、工程图、BOM清单，效率提升数倍至数十倍。</p>
      </div>
      <div class="claim-card reveal">
        <div class="num">/ 05</div>
        <h3>知识传承</h3>
        <p>把老师傅的行业经验（Knowhow）转化成可复用的设计规则，经验在企业内共享传承。</p>
      </div>
      <div class="claim-card reveal">
        <div class="num">/ 06</div>
        <h3>包教包会</h3>
        <p>培训 3 天，包教包会，学完即可独立搭建自己的参数化模块。</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== 服务内容 ========== -->
<section id="service">
  <div class="wrap">
    <div class="sec-head reveal">
      <div class="kicker">SERVICES</div>
      <h2>我能为你做什么</h2>
      <p>从培训到落地，从单点方案到体系搭建，覆盖非标参数化设计全流程。</p>
    </div>
    <div class="cards">
      <div class="card reveal">
        <div class="ico"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/></svg></div>
        <h3>参数化设计培训</h3>
        <p>3 天线下小班 / 企业内训，包教包会。</p>
        <ul>
          <li>变化规律总结方法</li>
          <li>参数定义与驱动规则</li>
          <li>自动出图与 BOM 清单</li>
          <li>模板化、标准化规范</li>
        </ul>
      </div>
      <div class="card reveal">
        <div class="ico"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg></div>
        <h3>非标自动化方案</h3>
        <p>整机 / 单机非标自动化设备设计，方案选型计算。</p>
        <ul>
          <li>机构方案与选型计算</li>
          <li>传动 / 气动 / 电气选型</li>
          <li>参数化整机建模</li>
          <li>出图与 BOM 落地</li>
        </ul>
      </div>
      <div class="card reveal">
        <div class="ico"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M9 13h6M9 17h6"/></svg></div>
        <h3>参数化模板 / 宏</h3>
        <p>帮你把常用件做成改参即用的参数化模块。</p>
        <ul>
          <li>标准件参数化模板</li>
          <li>系列零件表 / 方程式</li>
          <li>自动命名与属性配置</li>
          <li>企业模板规范建设</li>
        </ul>
      </div>
      <div class="card reveal">
        <div class="ico"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/><circle cx="12" cy="12" r="5"/></svg></div>
        <h3>设计咨询</h3>
        <p>一对一诊断你当前的设计痛点，给出落地方案。</p>
        <ul>
          <li>现状流程诊断</li>
          <li>参数化改造路径规划</li>
          <li>标准模块化体系建设</li>
          <li>疑难问题专项支持</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ========== 培训 ========== -->
<section class="training" id="training">
  <div class="wrap">
    <div class="sec-head reveal">
      <div class="kicker">TRAINING</div>
      <h2>3 天培训 · 包教包会</h2>
      <p>不讲理论空话，全部围绕你自己的产品案例，学完就能用。</p>
    </div>
    <div class="train-grid">
      <div class="train-steps">
        <div class="step reveal">
          <div class="no">1</div>
          <div><h4>Day 1 · 规律梳理</h4><p>带你梳理产品的变化规律，建立参数化模型思维，掌握规则总结方法。</p></div>
        </div>
        <div class="step reveal">
          <div class="no">2</div>
          <div><h4>Day 2 · 规则定义</h4><p>动手定义参数、配置驱动规则，完成你自己的第一个参数化模块。</p></div>
        </div>
        <div class="step reveal">
          <div class="no">3</div>
          <div><h4>Day 3 · 出图落地</h4><p>自动生成工程图与BOM清单，规范命名与属性，交付可复用成果。</p></div>
        </div>
        <div class="step reveal">
          <div class="no">✓</div>
          <div><h4>培训后 · 持续支持</h4><p>包教包会承诺：培训后仍提供答疑支持，确保真正落地使用。</p></div>
        </div>
      </div>
      <div class="train-side reveal">
        <h3>你将获得</h3>
        <ul>
          <li>一套可复用的参数化设计方法论</li>
          <li>基于你自己产品的参数化模块</li>
          <li>自动出图 + BOM 的标准流程</li>
          <li>设计经验安全留在企业内部的方案</li>
          <li>不再依赖外部服务商的自主能力</li>
        </ul>
        <div class="big">3 DAYS · 包教包会</div>
      </div>
    </div>
  </div>
</section>

<!-- ========== 支持平台 ========== -->
<section id="platform">
  <div class="wrap">
    <div class="sec-head reveal">
      <div class="kicker">PLATFORMS</div>
      <h2>支持主流三维设计平台</h2>
      <p>不局限于单一软件，方法通用，规则通用。</p>
    </div>
    <div class="platforms reveal">
      <span>SOLIDWORKS</span>
      <span>Solid Edge</span>
      <span>新迪天工CAD</span>
      <span>中望3D</span>
    </div>
  </div>
</section>

<!-- ========== 联系 ========== -->
<section class="contact" id="contact">
  <div class="wrap reveal">
    <h2>让重复的设计，变成一次性的能力</h2>
    <p class="p">无论是个人提升还是企业内训，先聊聊你的产品，我帮你判断哪些环节可以参数化、能提效多少。</p>
    <div class="cta">
      <a class="btn btn-primary" href="mailto:2713510938@qq.com">预约咨询</a>
    </div>
    <div class="note">邮箱：2713510938@qq.com · 微信：HYCOOLive · 工作日 9:00-18:00 回复</div>
  </div>
</section>

<footer>© 2026 DIY参数化 · 非标自动化参数化设计 · 只要变化有规律，就能实现自动设计</footer>

<script>
  // 滚动渐入
  const io = new IntersectionObserver(es=>{
    es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('on'); io.unobserve(e.target);} });
  },{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

  // 点击导航关闭移动端菜单
  document.querySelectorAll('#nav a').forEach(a=>{
    a.addEventListener('click',()=>document.getElementById('nav').classList.remove('open'));
  });
</script>
</body>
</html>
