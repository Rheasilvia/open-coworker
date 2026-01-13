"""Main agent orchestrator using LangGraph."""
from typing import TypedDict
from langgraph.graph import StateGraph, END
from src.agents.sub_agent import claude_agent


class AgentState(TypedDict):
    """State for the agent graph."""

    messages: list[dict]
    next: str


class OrchestratorAgent:
    """Main orchestrator agent using LangGraph."""

    def __init__(self):
        """Initialize the orchestrator."""
        self.graph = self._build_graph()
        print("Orchestrator Agent initialized (placeholder)")

    def _build_graph(self) -> StateGraph:
        """Build the agent graph."""
        workflow = StateGraph(AgentState)

        # Add nodes
        workflow.add_node("router", self._router)
        workflow.add_node("claude_code", self._claude_code_node)

        # Add edges
        workflow.set_entry_point("router")
        workflow.add_conditional_edges(
            "router",
            lambda state: state.get("next", END),
            {"claude_code": "claude_code", END: END},
        )
        workflow.add_edge("claude_code", END)

        return workflow.compile()

    async def _router(self, state: AgentState) -> AgentState:
        """Route the request to the appropriate sub-agent."""
        # TODO: Implement intelligent routing
        # For now, always route to claude_code
        state["next"] = "claude_code"
        return state

    async def _claude_code_node(self, state: AgentState) -> AgentState:
        """Handle requests that require claude-code."""
        message = state["messages"][-1]["content"]
        response = await claude_agent.execute(message)
        state["messages"].append({"role": "assistant", "content": response})
        return state

    async def process(self, message: str):
        """
        Process a message through the orchestrator.

        Args:
            message: The user message

        Yields:
            Chunks of the response
        """
        # For now, use a simple implementation
        # TODO: Integrate with actual LangGraph streaming
        state = AgentState(messages=[{"role": "user", "content": message}], next="")
        result = await self._claude_code_node(state)

        response_content = result["messages"][-1]["content"]
        for char in response_content:
            yield char


# Global instance
orchestrator = OrchestratorAgent()
