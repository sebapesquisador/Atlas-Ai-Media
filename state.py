"""
ATLAS AI MEDIA

Agent lifecycle states.
"""

from enum import Enum


class AgentState(Enum):
    CREATED = "created"
    INITIALIZED = "initialized"
    RUNNING = "running"
    STOPPED = "stopped"
