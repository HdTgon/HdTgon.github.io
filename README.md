# HdTgon Academic Homepage

基于 [RayeRen/AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) 的 Jekyll 学术主页，保留原主题、响应式布局和 MIT 许可证。上游版本：`2cc1577eeaf2f74dede6d016a70722dbd409ea2f`。

网站：https://hdtgon.github.io/

## 更新资料

所有个人资料集中在 `_data/profile.json`：姓名、照片、介绍、研究方向、新闻、论文、教育、荣誉奖项及社交链接。布局在 `_pages/about.html`，侧栏在 `_includes/author-profile.html`。导航在 `_data/navigation.yml`。主题样式保留上游 `_sass/` 与 `assets/css/main.scss`，个人调整在 `assets/css/profile.css`。

`links` 支持 GitHub、Google Scholar、Email（mailto: 地址）、CV（例如 `/files/cv.pdf`）。null 表示待补充，不生成虚假链接。照片替换 `images/avatar.jpg`。CV 文件放 `files/cv.pdf` 后填写对应链接。

论文条目字段：title（标题）、authors（作者数组）、venue（期刊/会议）、year（整数）、links（Paper/Code 等链接对象）。可选 image 字段填写真实论文图片路径。新闻、教育、奖项条目格式为 `{"date":"2026.09","text":"Your update"}`。

现有论文依据公开 GitHub 仓库描述迁入，归属、作者、正式出版信息待本人确认；研究方向亦从仓库主题推断。未填个人信息继续标注待补充，没有使用模板自带的示例履历或引用数。

## 本地预览和构建

安装 Ruby 3.3、Bundler 和编译工具后：

```bash
git clone https://github.com/HdTgon/HdTgon.github.io.git
cd HdTgon.github.io
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

访问 http://127.0.0.1:4000 。修改 `_config.yml` 后重启。独立构建与输出验证：

```bash
bundle exec jekyll build
python scripts/check.py
```

## 自动部署

Settings → Pages → Source 保持 GitHub Actions。推送 main 自动运行官方 `actions/jekyll-build-pages`，检查 `_site` 后上传 Pages artifact 并部署。无需新增 Secrets。可在 Actions 手动 Run workflow。该 Jekyll 版本替换此前的 Python 静态构建，旧版仍保留在 Git 历史中。

未启用上游 Scholar 定时爬虫和引用数功能；填写真实 Scholar 信息后可再配置。原模板许可证见 LICENSE。

## 简介换行与链接

`_data/profile.json` 中 `about` 是字符串数组，每个元素显示为一个段落。段落之间加逗号，最后一项后不加逗号，不要在同一对双引号内部直接换行。简介支持 Markdown 链接，例如 `[Prof. Shudong Huang](https://huangsd.github.io/)`。

## Contact 与论文图片

底部邮箱在 `_data/profile.json` 的 `contact.email` 修改。侧栏社交链接与底部 Contact 独立维护。

每篇论文的 `image` 是图片路径，`image_alt` 是替代说明，`badge` 是左上角标志文字（如 ICML、TNNLS、KBS）。图片放在 `images/publications/`，建议使用论文框架图或成果示意图。六篇论文现已使用本人上传的 PNG 图片。论文按照 `_data/profile.json` 中 publications 数组的顺序显示；调整数组条目的顺序即可调整页面顺序。替换后例如：

```json
"image": "images/publications/basecil.png",
"image_alt": "Overview of the baseCIL method",
"badge": "ICML"
```

桌面显示左图右文，窄屏自动上下排列。样式在 `assets/css/profile.css` 的 Publication thumbnails 段。

论文缩略图统一采用 11:7 比例，居中裁切填满图片框，点击可查看完整原图。顶部 Research 和 Honors and Awards 导航入口已隐藏，正文仍保留。页尾署名不在页面显示，模板版权和 MIT 许可证继续保留在 LICENSE 及本说明中。Contact 邮箱为纯文本。

## 论文作者与官方链接

`authors` 数组按官方作者顺序填写纯文本姓名，显示时以逗号分隔，与 profile.name 相同的姓名自动加粗，无需写 Markdown 星号。`links.Paper` 使用 ICML 官方会议页、IEEE Xplore 或 Elsevier ScienceDirect 的论文页，Code 保持指向代码仓库。

核对来源：

- ICML: https://icml.cc/virtual/2026/poster/63084 ，作者顺序亦与官方论文集 https://proceedings.mlr.press/v306/cao26h.html 核对。
- TNNLS: https://ieeexplore.ieee.org/document/10737889/ ，DOI 10.1109/TNNLS.2024.3482440；作者与出版社提交至 Crossref 的元数据核对。
- INS: https://www.sciencedirect.com/science/article/pii/S0020025524000914
- KBS CFSMO: https://www.sciencedirect.com/science/article/pii/S095070512300922X
- ESWA: https://www.sciencedirect.com/science/article/pii/S0957417423023953
- KBS CCSFS: https://www.sciencedirect.com/science/article/pii/S0950705123003283

CFSMO 和 ESWA 的正式卷期为 2024，网站继续保留本人指定的 2023 显示年份；链接和作者使用已核对的官方记录。
