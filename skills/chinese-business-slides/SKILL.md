---
name: chinese-business-slides
description: Use whenever the user says “商赛 PPT 风格” or asks to create or revise Chinese business-competition, 创新创业, 挑战杯, 商赛, 商业计划书, 项目答辩, 路演, 行业分析, market analysis, or competition-style presentation content in PPTX, PowerPoint, HTML slides, or printable web format.
---

# 中国商赛商业演示

## 明确触发

用户说“用商赛 PPT 风格”“按照商赛 PPT 风格做”“商赛风格 PPT”或含义相同的表达时，直接启用本技能，无需再次询问风格。

## 核心

制作直白、清楚、统一的商业演示。让评委或管理者先看到判断，再看到证据。

本技能提供视觉与叙事约束。PPTX 制作继续调用 `Presentations` skill；HTML 使用本技能的 16:9 规则和主题资产。

## 工作流程

### 1. 判断输出路径

- 用户需要 `.pptx`、PowerPoint 或可编辑演示稿：先读取 `Presentations` skill，再叠加本技能。
- 用户需要 HTML、网页演示或可打印页面：读取 [html-output.md](references/html-output.md)。
- 用户提供现成模板：服从模板继承流程，只把本技能用于内容层级和新增页面检查。

### 2. 建立结论主线

写出整套演示的 5–9 条判断。每页只承担一条主要判断。

标题使用结论式表达，例如：

- `成人玩家成为最大年龄组，玩具从礼物转向自我表达`
- `行业增长已经回来，价值向少数赛道集中`

避免只写 `市场分析`、`项目介绍`、`商业模式`、`竞争优势`。

### 3. 核验材料

- 当前行业、公司、政策和市场数据需要查询最新来源。
- 保存来源、发布日期、统计口径和单位。
- 数据页在页脚显示来源；详细 URL 放入来源页或附录。
- 缺少证据时缩小结论，不补造数字。

### 4. 锁定视觉系统

读取 [visual-system.md](references/visual-system.md)，并使用 [theme-tokens.json](assets/theme-tokens.json)。

必须遵守：

- 白底承担主要阅读页面。
- 深蓝整页只用于封面数据栏、案例、章节或附录。
- 白底中禁止放缺少结构依据的大面积孤立深蓝块。
- 蓝色表示增长、市场、机会；橙色表示活力、消费、阶段重点；红色表示风险、政策、高优先级结论。
- 全篇统一标题位置、章节标签、白卡、色条、页脚、页码和图表标签。

### 5. 规划页面

读取 [page-patterns.md](references/page-patterns.md)。

- 8–12 页演示使用 3–5 种宏观布局。
- 复用成熟页面语法，控制视觉变化。
- 图表使用浅蓝、亮蓝、浅橙、亮橙的同色系对照。
- 一页只设置一个主要证据对象。
- 深蓝案例页和深蓝附录页可以形成章节节奏。

### 6. 制作与检查

- PPTX：元素保持可编辑，渲染全部页面并检查版式。
- HTML：使用 [html-theme.css](assets/html-theme.css)，检查 16:9、浏览器缩放和打印。
- 交付前读取 [qa-checklist.md](references/qa-checklist.md)。

## 风格边界

这套风格适合：

- 商赛与创业项目答辩
- 行业趋势与市场分析
- 商业计划书和项目路演
- 政策价值、社会价值与产业项目
- 需要快速阅读的内部商业汇报

以下场景只在用户明确要求时使用：

- 财报与投资者关系演示
- 艺术、时尚和摄影作品集
- 强品牌发布会
- 学术论文答辩
- 纯技术架构演讲

## 交付标准

- 缩略图下能识别统一的视觉系统。
- 内容顺序清楚，标题可以单独组成摘要。
- 颜色角色稳定，没有随页随机变化。
- 没有模板拼贴感、连续卡片墙和装饰性图形堆叠。
- 数据、单位、日期和来源准确。
- PPTX 或 HTML 完成对应格式的机械检查。
