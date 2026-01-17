---
title: 我的技术栈之路：从Vue到Hexo
date: 2025-10-16 14:00:00
tags: [Vue, Hexo, Netlify, 教程]
categories: [技术杂谈]
cover: /img/banner.jpg
description: 记录我是如何从手写 Vue 博客转向使用 Hexo + Butterfly 主题，并成功部署到 Netlify 的全过程。
---

## 前言

作为一名人工智能专业的学生，我最初的想法是使用 **Vue 3 + Element Plus** 配合AI搭建一个博客。我成功配置了 Vite，写好了 Router，甚至搭建了一个简单的后台骨架。

但是，在折腾 Layout 和 CSS 的过程中，我意识到：**如果是为了写文章，我不应该在造轮子上花费太多时间。** 于是，我找到了一个更成熟的静态博客生成器 —— **Hexo**，并选择了颜值极高的 **Butterfly** 主题。

## 为什么选择 Hexo + Butterfly

1.  **极速生成**：基于 Node.js，生成静态页面非常快。
2.  **无需后端**：生成的全是 HTML/CSS/JS，可以直接部署在 Netlify 等免费托管平台。
3.  **Butterfly 主题**：这是我选择 Hexo 的最大动力。它自带了夜间模式、美观的卡片布局、社交图标，几乎不需要改代码就能拥有一个专业的博客外观。

---

## 🛠️ 本地搭建全流程

这是我成功搭建博客的完整命令记录，留作备忘。

### 1. 初始化 Hexo
首先需要安装 Hexo 的全局脚手架，并在空文件夹中初始化项目。

```bash
# 全局安装 Hexo 工具
npm install -g hexo-cli

# 初始化博客文件夹 (确保文件夹为空)
hexo init .

# 安装基础依赖
npm install

```

### 2. 安装 Butterfly 主题与必要插件

Butterfly 主题使用了 Pug 和 Stylus 渲染器，如果漏装了下面第二行命令，运行会报错。

```bash
# 下载主题
npm install hexo-theme-butterfly

# 安装渲染器 (关键步骤！)
npm install hexo-renderer-pug hexo-renderer-stylus --save

```

### 3. 启用主题

修改博客根目录下的 `_config.yml` 配置文件：

```yaml
# 找到 theme: landscape 修改为 butterfly
theme: butterfly

```

---

## 🚀 部署到 Netlify

我选择了 **GitHub + Netlify** 的自动化部署方案。只要我把代码推送到 GitHub，Netlify 就会自动构建并发布新文章。

### 1. 推送代码到 GitHub

因为我之前在这个仓库里存过 Vue 的代码，所以使用了强制推送来覆盖历史。

```bash
git init
git add .
git commit -m "重构：迁移至 Hexo 博客"
git branch -M main
git remote add origin [https://github.com/HanaViolet/MyWeb.git](https://github.com/HanaViolet/MyWeb.git)

# 强制推送 (慎用，会覆盖远程历史)
git push -u origin main -f

```

### 2. Netlify 的关键设置

这是最容易踩坑的地方！从 Vue 切换到 Hexo 后，必须去 Netlify 后台修改构建命令。

* **路径**：Site configuration -> Build & deploy -> Edit settings
* **配置项修改**：

| 设置项 | 旧值 (Vue) | **新值 (Hexo)** |
| --- | --- | --- |
| **Build command** | `npm run build` | `hexo generate` |
| **Publish directory** | `dist` | `public` |

### 3. 验证成果

保存设置后，手动点击 **Trigger deploy**。当状态变为绿色的 **Published** 时，访问我的域名，那只漂亮的蝴蝶就出现了！

---

## 📝 常用命令备忘

以后写博客只需要记住这三步：

1. **新建文章**：`hexo new "文章标题"`
2. **本地预览**：`hexo s` (访问 localhost:4000)
3. **发布上线**：
```bash
git add .
git commit -m "发布新文章"
git push

```



## 结语

虽然放弃了手写 Vue 博客有点遗憾，但通过这次迁移，我学会了 Git 的强制推送、Netlify 的持续集成配置，以及 Hexo 的插件机制。

现在的重点是：**可以好好写文章了！**

```

### 💡 食用指南
1.  复制上面的代码。
2.  在 VS Code 中打开 `source/_posts/我的技术栈之路.md`。
3.  **全选 -> 粘贴 -> 保存**。
4.  然后执行你的 **“发布三连击”** (`git add` ... `git push`)。

一分钟后，你的博客上就会出现这篇记录了你今天奋斗历程的文章了！去试试吧！

```