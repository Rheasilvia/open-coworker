# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Open-Coworker is a cross-platform desktop agentic application with a dual-agent architecture:
- **UI**: Electron + React + TypeScript + Streamdown
- **Agent**: Python 3.13 + FastAPI + uv
  - Main Agent: LangGraph (orchestrator)
  - Sub Agent: Claude Agent SDK (controls claude-code)

The project uses a pnpm workspace monorepo structure with two main apps in `apps/`.

## Development Commands

### Initial Setup
```bash
# Install Node.js dependencies
pnpm install

# Setup Python agent
cd apps/agent && uv sync
```

### Development (Two Terminals Required)
```bash
# Terminal 1: Start agent service
pnpm dev:agent
# Runs FastAPI on http://127.0.0.1:8000 with auto-reload

# Terminal 2: Start Electron UI
pnpm dev
# Starts Electron with Vite dev server
```

### Other Commands
```bash
# Build UI for production
pnpm build

# Run agent tests
pnpm --filter agent test

# Lint code
pnpm lint
```

## Architecture

### Monorepo Structure
- `apps/ui/` - Electron desktop application
- `apps/agent/` - Python FastAPI agent service
- `packages/` - Shared packages (future use)

### Communication Protocol
UI and Agent communicate via HTTP with Server-Sent Events (SSE):
- **Endpoint**: `POST http://localhost:8000/chat`
- **Request**: `{"message": "user query"}`
- **Response**: SSE stream with `data: {"content": "chunk"}` format

Key files:
- UI client: `apps/ui/src/renderer/lib/agent-client.ts`
- Agent routes: `apps/agent/src/api/routes.py`

### Dual-Agent Architecture
1. **Orchestrator** (`apps/agent/src/agents/orchestrator.py`): LangGraph-based main agent
2. **Sub Agent** (`apps/agent/src/agents/sub_agent.py`): Claude Agent SDK wrapper

Both are currently placeholder implementations returning "Hello World" responses.

## Build Systems

### Electron (UI)
- **Tool**: Electron Forge with Vite plugin
- **Config**: `apps/ui/forge.config.cjs`
- **Vite configs**: `vite.main.config.ts`, `vite.renderer.config.ts`

### Python (Agent)
- **Tool**: uv with pyproject.toml
- **Backend**: Hatchling
- **Packages**: Source in `src/` directory

## Configuration

### Agent Service
- Host: `127.0.0.1:8000`
- CORS enabled for development
- Auto-reload enabled

### Package Mirrors
- **pnpm**: Uses `https://registry.npmmirror.com/`
- **uv**: Uses Tsinghua TUNA mirror

## Important Notes

- The agent must be running before starting the UI for communication to work
- Current agent implementation is placeholder - actual Claude Agent SDK integration pending
- Streamdown is used for rendering streaming markdown responses in the UI
- Electron preload script provides secure IPC bridge (currently minimal)
