# HTML 输出

## 画布

- 每页固定为 16:9。
- 设计基准为 `1280 × 720`。
- 页面使用 `aspect-ratio: 16 / 9`，缩放时整体等比。
- 打印时一页对应一张幻灯片，禁止跨页断开。

## 主题

复制或引用 `../assets/html-theme.css`。

使用统一组件：

- `.cbs-slide`
- `.cbs-kicker`
- `.cbs-title`
- `.cbs-subtitle`
- `.cbs-card`
- `.cbs-card--blue`
- `.cbs-card--orange`
- `.cbs-card--red`
- `.cbs-dark`
- `.cbs-source`

不要为每页重新定义颜色、圆角、阴影和标题尺寸。

## 页面结构

```html
<section class="cbs-slide">
  <div class="cbs-kicker">01 / 市场回升</div>
  <h1 class="cbs-title">2025 年进入恢复周期</h1>
  <p class="cbs-subtitle">全球与本地市场同步转正。</p>
  <div class="cbs-content">
    <!-- chart or proof object -->
  </div>
  <footer class="cbs-source">来源：机构，发布日期</footer>
</section>
```

## 图表

- 优先使用 SVG 或原生 HTML/CSS，保持清晰。
- 使用设计 token 的蓝橙对照。
- 数值直接放在图形附近。
- 图例、轴、注释和来源与 PPTX 版本保持一致。

## 响应式预览

- 桌面端显示整页并留出页面间距。
- 小屏允许缩放整张画布，禁止把一页重排成长网页。
- 正文不能依赖 hover。
- 导航和页码不遮挡内容。

## 打印

```css
@media print {
  body { background: #fff; }
  .cbs-slide {
    width: 13.333in;
    height: 7.5in;
    break-after: page;
    box-shadow: none;
  }
}
```

打印前检查：

- 背景色已开启打印。
- 深蓝整页没有变成白底。
- 页脚和来源未被裁切。
- 文字、图表和卡片没有溢出 16:9 画布。
