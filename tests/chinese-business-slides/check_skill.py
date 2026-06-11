from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "chinese-business-slides"


def read(path: Path) -> str:
    assert path.exists(), f"missing: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def main() -> None:
    skill_md = read(SKILL / "SKILL.md")
    yaml = read(SKILL / "agents" / "openai.yaml")
    visual = read(SKILL / "references" / "visual-system.md")
    patterns = read(SKILL / "references" / "page-patterns.md")
    html = read(SKILL / "references" / "html-output.md")
    qa = read(SKILL / "references" / "qa-checklist.md")
    css = read(SKILL / "assets" / "html-theme.css")
    tokens_path = SKILL / "assets" / "theme-tokens.json"
    tokens = json.loads(read(tokens_path))

    assert skill_md.startswith("---\nname: chinese-business-slides\n")
    for trigger in ["商赛 PPT 风格", "商赛", "创新创业", "挑战杯", "商业计划书", "路演", "行业分析"]:
        assert trigger in skill_md, f"missing trigger: {trigger}"
    for route in ["Presentations", "PPTX", "HTML"]:
        assert route in skill_md, f"missing output route: {route}"
    assert "references/visual-system.md" in skill_md
    assert "references/page-patterns.md" in skill_md
    assert "references/html-output.md" in skill_md
    assert "references/qa-checklist.md" in skill_md

    required_colors = {
        "navy": "#173B63",
        "blue": "#1EA5D8",
        "orange": "#F28A32",
        "red": "#B52832",
        "paper": "#FAF9F5",
    }
    assert tokens["colors"] | required_colors == tokens["colors"]
    for color in required_colors.values():
        assert color.lower() in css.lower(), f"CSS missing color {color}"

    combined = "\n".join([skill_md, visual, patterns, html, qa])
    for rule in [
        "结论式标题",
        "深蓝整页",
        "白底",
        "孤立",
        "统一",
        "来源",
        "16:9",
        "缩略图",
    ]:
        assert rule in combined, f"missing rule: {rule}"

    assert "display_name" in yaml and "default_prompt" in yaml
    assert not re.search(r"\b(TODO|TBD)\b", combined)
    print("chinese-business-slides checks passed")


if __name__ == "__main__":
    main()
