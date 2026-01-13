# pnpm 到 Yarn 迁移计划

## 已完成的工作

✅ 更新 package.json - engines, scripts, workspaces
✅ 更新 .npmrc - 移除 pnpm 配置，添加 yarn registry mirror
✅ 删除 pnpm-workspace.yaml
✅ 更新 .vscode/tasks.json - 所有 pnpm 命令改为 yarn
✅ 更新 .vscode/launch.json - runtimeExecutable 改为 yarn
✅ 更新 CLAUDE.md - 所有 pnpm 引用改为 yarn
✅ 更新 README.md - 所有 pnpm 引用改为 yarn
✅ 更新 .gitignore 注释

## 待完成的工作

### 1. 安装依赖
```bash
cd d:/Repos/open-coworker
yarn install
```

如果 yarn 命令不可用，使用：
```bash
npx yarn@1.22.22 install
```

### 2. 验证安装
```bash
# 检查 yarn.lock 是否生成
ls yarn.lock

# 检查 node_modules
ls node_modules/electron
```

### 3. 测试启动
```bash
# 终端 1: 启动 agent
yarn dev:agent

# 终端 2: 启动 UI
yarn dev
```

### 4. 提交更改
```bash
git add .
git commit -m "chore: migrate from pnpm to yarn workspace

- Update package.json scripts to use yarn workspace commands
- Add workspaces field to root package.json
- Remove pnpm-specific .npmrc configuration
- Add yarn registry mirror configuration
- Update VS Code tasks and launch configs
- Update CLAUDE.md and README.md documentation
- Delete pnpm-workspace.yaml and pnpm-lock.yaml
- Regenerate yarn.lock with all dependencies

Co-Authored-By: Claude <noreply@anthropic.com>"
```

## 文件变更清单

### 修改的文件
- `package.json` - 添加 workspaces，更新 engines 和 scripts
- `.npmrc` - 更新为 yarn registry mirror
- `.vscode/tasks.json` - pnpm → yarn
- `.vscode/launch.json` - pnpm → yarn
- `CLAUDE.md` - 文档更新
- `README.md` - 文档更新
- `.gitignore` - 注释更新

### 删除的文件
- `pnpm-workspace.yaml`
- `pnpm-lock.yaml`
- `yarn.lock` (旧的，不完整)

### 新增的文件
- `yarn.lock` (运行 yarn install 后生成)

## 注意事项

1. 如果使用 `npx yarn`，在 VS Code 调试配置中可能也需要更新
2. 确保使用 Yarn 1.22+ (Berry/Yarn 2+ 语法不同)
3. yarn 会默认 hoist 所有依赖，不需要额外配置
