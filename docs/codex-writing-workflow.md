# Codex Writing Workflow

这份流程把 Claude Project 的 Skill 和 Knowledge 做法，翻成 Codex 在本仓库里的使用方式。

## 对应关系

- Claude Project instructions -> `AGENTS.md`
- Claude Skill file -> `AGENTS.md` 里的稳定流程规则
- Claude Knowledge -> `docs/voice/` 下的语料文件
- 单次 brief -> 用户当轮消息、图片、链接、资料
- 写前联网搜索 -> Codex 在需要新信息时先查证
- 写后自检 -> 按项目里的中文风格清单检查

## 目录约定

`docs/voice/` 用来放语料。可以放微博、公众号、朋友圈长文、口播稿、邮件、产品文案。文件名建议写清楚来源和场景，例如：

- `2026-05-weibo-ai-tools.md`
- `2026-05-product-launch-copy.md`
- `2026-05-speaking-notes.md`

每篇语料开头加三行说明，方便 Codex 读取：

```md
场景：微博长文
语气：直接、口语、带个人判断
保留特征：短段落、少形容词、先讲结论
```

## 写作流程

1. 读取 `AGENTS.md` 和 `DESIGN.md`。
2. 读取 `docs/voice/` 中和任务最接近的 3 到 8 篇语料。
3. 从用户材料里提炼核心观点，缺观点时先问一句。
4. 需要新信息时先搜索，避免沿用旧数据。
5. 起草内容，优先贴近语料里的节奏和用词。
6. 按 AI 味清单自检并修改。
7. 输出可直接使用的版本，必要时附修改说明。

## AI 味自检

- 物理动作动词滥用：承载、打造、赋能、撬动、沉淀、拉通。
- 形容词先下判断：伟大、极致、颠覆、深度、重要、显著。
- 抽象名词当主语：效率、体验、能力、生态、场景、价值。
- 不必要夹英文：workflow、brief、insight、agent、prompt。
- 对立转折包装：少用“不是……而是……”“与其……不如……”这类模板句。

## 使用建议

先放 10 到 20 篇你满意的原文进 `docs/voice/`。规则只能约束错误，语料能让输出接近你的真实表达。
