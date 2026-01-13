# Open-Coworker

A cross-platform desktop agentic application with dual-agent architecture.

## Architecture

- **UI**: Electron + React + TypeScript + Streamdown
- **Agent**: Python 3.13 + FastAPI + uv
  - Main Agent: LangGraph (orchestrator)
  - Sub Agent: Claude Agent SDK (controls claude-code)

## Project Structure

```
open-coworker/
├── apps/
│   ├── ui/          # Electron desktop application
│   └── agent/       # Python FastAPI agent service
└── packages/        # Shared packages
```

## Getting Started

### Prerequisites

- Node.js 20+
- Yarn 1.22+
- Python 3.13+
- uv (Python package manager)

### Installation

```bash
# Install Node.js dependencies
yarn install

# Setup Python agent
cd apps/agent
uv sync
```

### Development

```bash
# Start agent service (terminal 1)
yarn dev:agent

# Start UI (terminal 2)
yarn dev
```

## Resources

- [Electron Forge Documentation](https://www.electronforge.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangGraph Documentation](https://docs.langchain.com/langgraph/)
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python)
