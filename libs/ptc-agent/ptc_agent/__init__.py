"""
PTC Agent - Programmatic Tool Calling for AI agents with MCP.

This package provides:
- Core infrastructure (sandbox, MCP, sessions)
- Agent implementations (PTCAgent, tools, middleware)
- Configuration system
- Utility functions

Quick start:
    from ptc_agent import AgentConfig, PTCAgent
    from ptc_agent.core import SessionManager

    config = AgentConfig.create(llm=your_llm)
    session = SessionManager.get_session("my_session", config.to_core_config())
    await session.initialize()

    agent = PTCAgent(config)
    executor = agent.create_agent(session.sandbox, session.mcp_registry)
"""

__version__ = "0.1.0"

# Re-export commonly used classes for convenience
from ptc_agent.config import (
    AgentConfig,
    LLMConfig,
    LLMDefinition,
    CoreConfig,
    load_from_files,
    load_core_from_files,
)
from ptc_agent.core import (
    PTCSandbox,
    SessionManager,
    Session,
    MCPRegistry,
    MCPToolInfo,
)
from ptc_agent.agent import (
    PTCAgent,
    PTCExecutor,
    create_ptc_agent,
    DaytonaBackend,
)

__all__ = [
    # Version
    "__version__",
    # Config
    "AgentConfig",
    "LLMConfig",
    "LLMDefinition",
    "CoreConfig",
    "load_from_files",
    "load_core_from_files",
    # Core
    "PTCSandbox",
    "SessionManager",
    "Session",
    "MCPRegistry",
    "MCPToolInfo",
    # Agent
    "PTCAgent",
    "PTCExecutor",
    "create_ptc_agent",
    "DaytonaBackend",
]
