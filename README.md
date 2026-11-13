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
