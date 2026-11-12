# HdTgon — Academic Homepage

轻量级 GitHub Pages 学术主页：HTML + CSS + Python 标准库，无 npm、Jekyll、第三方 Python 依赖或浏览器端 JavaScript。支持桌面、移动端、键盘导航及打印。

## 本地预览

需要 Python 3.12+（GitHub Actions 自动配置）。

```bash
git clone https://github.com/HdTgon/HdTgon.github.io.git
cd HdTgon.github.io
python scripts/build.py
python scripts/check.py
python -m http.server 8000 --directory dist
```

浏览器打开 http://localhost:8000 。修改内容或样式后重新运行 build.py，再刷新浏览器。停止服务按 Ctrl+C。

## 维护内容

- `data/profile.json`：姓名、简介、研究方向、新闻、论文、教育和学术服务。
- `assets/avatar.jpg`：当前为 GitHub 头像，替换成个人照片即可。也可更新 JSON 中 photo 路径。
- `assets/cv.pdf`：自行添加真实简历后，把 links.CV 改为 `assets/cv.pdf`。
- `templates/index.html`：页面布局。
- `assets/style.css`：配色、字体、间距与响应式布局。
- `scripts/build.py`：转义数据并生成 dist；所有内容构建为 HTML，关闭 JavaScript 也能访问。
- `.github/workflows/pages.yml`：推送 main 自动构建、检查并部署。

Google Scholar 填写完整个人主页 URL；Email 填 `mailto:you@example.edu`；CV 可用站内相对路径或 HTTPS。设为 null 会显示 To add，不生成假链接。所有站内资源使用相对路径，也可部署至项目型 Pages。

论文示例（仅为格式示例，不代表真实研究成果）：

```json
{
  "title": "Your paper title",
  "authors": ["Your Name", "Coauthor Name"],
  "venue": "Conference or Journal",
  "year": 2026,
  "links": {
    "Paper": "https://doi.org/your-doi",
    "Code": "https://github.com/your-account/your-repository"
  }
}
```

News、Education、Academic Services 使用相同的条目结构，例如：

```json
{"date": "2026.09", "text": "Your academic update or education details."}
```

论文按年份降序排列，同年保留 JSON 顺序。Paper、Code、Project、Slides 等链接均可按需添加。链接为空可省略或设为 null。

## 部署到 GitHub Pages

1. 账号 HdTgon 下创建公开仓库 `HdTgon.github.io`。
2. 将此项目所有源码文件（包括 `.github` 隐藏目录）推送至 `main`，不需要提交 dist。
3. 仓库 **Settings → Pages → Build and deployment → Source → GitHub Actions**。
4. 在 **Actions** 查看 `Deploy academic homepage to GitHub Pages`，必要时手动 Run workflow。
5. 成功后访问 https://hdtgon.github.io/ 。后续更新 JSON/照片并推送 main 即自动发布。

工作流采用两个 job：build 仅有 contents:read；deploy 单独申请 pages:write 和 id-token:write，通过 github-pages environment 发布官方 Pages artifact。并发发布按队列运行。无需个人 Token 或 Secrets。

若创建仓库失败：在 GitHub 手动创建上述仓库，并在 ChatGPT GitHub 连接/App 的仓库授权范围中加入它。GitHub App 可能没有创建仓库、写入 workflow 或管理 Pages 的权限；可本地运行以下命令完成首次发布（gh 会引导浏览器登录，不要把 Token 发到聊天中）：

```bash
gh auth login
gh repo create HdTgon/HdTgon.github.io --public --source=. --remote=origin --push
```

该命令要求当前目录已 `git init` 并有初始提交；若仓库已创建，请改用 git remote add origin 和 git push -u origin main。随后按上方第 3 步启用 Pages。

## 初版资料来源与待补充

视觉结构参考 https://mouxingyang.github.io/ ，独立实现页面与样式。论文标题、年份和期刊/会议来自 https://github.com/HdTgon 的公开仓库描述；未据此断定仓库所有者是作者，尚需本人确认作者名单、正式出版年份、Paper 链接和论文归属。研究方向标签亦从仓库主题推断。

当前仅确认 GitHub 用户名与公开头像；真实姓名、单位、身份、教育、新闻、服务、邮箱、Scholar、CV 均待补充。页面明确标注这些空缺。发布前或后续迭代请在 profile.json 中完善。

## 验证

运行 `python scripts/build.py` 和 `python scripts/check.py` 检查内容字段、锚点、静态资源及工作流关键配置。最终部署应以 GitHub Actions 的实际 build/deploy 成功状态和公开网址响应为准；静态配置检查不替代远端执行。
