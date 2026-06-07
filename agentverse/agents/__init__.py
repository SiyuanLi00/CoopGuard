# from .agent import Agent
from agentverse.registry import Registry

agent_registry = Registry(name="AgentRegistry")

from .base import BaseAgent
from .conversation_agent import ConversationAgent

from .coopguard_agent import CoopGuardAgent
from .coopguard_multi_agent import CoopGuardAgent
from .coopguard_multi_agent_con import CoopGuardAgent