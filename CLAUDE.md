# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Open-Coworker is a cross-platform desktop agentic application with a dual-agent architecture:
- **UI**: Electron + React + TypeScript + Streamdown
- **Agent**: Python 3.13 + FastAPI + uv
  - Main Agent: LangGraph (orchestrator)
  - Sub Agent: Claude Agent SDK (controls claude-code)

The project uses a yarn workspace monorepo structure with two main apps in `apps/`.

## Development Commands

### Initial Setup
```bash
# Install Node.js dependencies
yarn install

# Setup Python agent
cd apps/agent && uv sync
```

### Development (Two Terminals Required)
```bash
# Terminal 1: Start agent service
yarn dev:agent
# Runs FastAPI on http://127.0.0.1:8000 with auto-reload

# Terminal 2: Start Electron UI
yarn dev
# Starts Electron with Vite dev server on port 5173
```

### Other Commands
```bash
# Build UI for production
yarn build

# Run agent tests
yarn workspace agent test

# Lint code
yarn lint
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

## Configuration

### Ports
- **Agent Service**: `http://127.0.0.1:8000` (FastAPI)
- **UI Dev Server**: `http://localhost:5173` (Vite)

These are separate services that run independently.

### Agent Service
- Host: `127.0.0.1:8000`
- CORS enabled for development
- Auto-reload enabled

### Package Mirrors
- **yarn**: Uses `https://registry.npmmirror.com/` (configured in .npmrc)
- **uv**: Uses Tsinghua TUNA mirror

## Important Notes

- The agent must be running before starting the UI for communication to work
- Current agent implementation is placeholder - actual Claude Agent SDK integration pending
- Streamdown is used for rendering streaming markdown responses in the UI
- Electron preload script provides secure IPC bridge (currently minimal)
