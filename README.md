# Cloud-First Starter

这是一个适合快速上线的极简云端版本。

## 适合什么场景

- 个人主页
- 产品落地页
- 作品集
- 未来 SaaS 或 AI 工具的宣传页起点

## 当前特点

- 纯静态文件，结构简单
- 不依赖本地构建
- 可直接托管到 Vercel、Cloudflare Pages、GitHub Pages
- 根目录已配置 `DESIGN.md`，后续 UI 修改按 VoltAgent-inspired 设计规范执行
- 根目录已配置 `AGENTS.md`，约束文案风格和项目修改方式
- 后续可以再升级成 Next.js 或其他框架

## 文件说明

- `index.html`：首页内容
- `styles.css`：站点样式
- `DESIGN.md`：页面视觉规范，参考 `VoltAgent/awesome-design-md` 的 DESIGN.md 思路
- `AGENTS.md`：给代码代理读取的项目协作规则
- `docs/codex-writing-workflow.md`：Codex 写作流程，把规则、语料、搜索和自检串起来
- `docs/voice/`：预留给个人语料，后续可放满意的微博、长文、口播稿或邮件样本

## 设计规范

当前页面采用深色开发者工具风格：

- 近黑背景
- 电绿色强调色
- 细边框模块
- 代码面板视觉
- 紧凑圆角
- 直接、具体的中文文案

## 如何部署到云端

### Vercel

1. 把这个仓库推到 GitHub。
2. 在 Vercel 里选择 `Add New Project`。
3. 导入这个仓库。
4. Framework Preset 选择 `Other` 或保持静态站点默认值。
5. Build Command 留空。
6. Output Directory 留空。
7. 点击部署。

### Cloudflare Pages

1. 把这个仓库推到 GitHub。
2. 在 Cloudflare Pages 中连接该仓库。
3. Framework preset 选择 `None`。
4. Build command 留空。
5. Build output directory 填 `/` 或留空，按界面默认静态站点设置。
6. 点击部署。

## 下一步建议

先改这几处内容最有价值：

- 站点标题和副标题
- 你的名字或品牌名
- 按钮链接
- 三个功能卡片里的文字

等你确认方向以后，再决定要不要加：

- 联系表单
- 博客
- 数据统计
- OpenAI 接口
- 登录系统
