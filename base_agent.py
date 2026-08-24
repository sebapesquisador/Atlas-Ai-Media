"""
ATLAS AI MEDIA

Base class for all agents.
"""

from abc import ABC, abstractmethod

from atlas.agents.state import AgentState
from atlas.events.event import Event
from atlas.events.event_bus import EventBus
from atlas.logging import logger
from atlas.memory.manager import MemoryManager


class BaseAgent(ABC):
    """
    Base class for all ATLAS agents.
    """

    def __init__(
        self,
        name: str,
        event_bus: EventBus,
        memory_manager: MemoryManager,
    ) -> None:
        self.name = name
        self.event_bus = event_bus
        self.memory_manager = memory_manager
        self.state = AgentState.CREATED

    @abstractmethod
    def execute(self) -> None:
        """
        Execute the agent.
        """

    def publish(
        self,
        event: Event,
    ) -> None:
        """
        Publish an event.
        """
        logger.info(
            "%s published event '%s'",
            self.name,
            event.name,
        )
        self.event_bus.publish(event)

    def subscribe(
        self,
        event_name: str,
        handler,
    ) -> None:
        """
        Subscribe to an event.
        """
        self.event_bus.subscribe(event_name, handler)

    def initialize(self) -> None:
        """
        Initialize the agent.
        """
        logger.info("%s initialized", self.name)
        self.state = AgentState.INITIALIZED

    def start(self) -> None:
        """
        Start the agent.
        """
        logger.info("%s started", self.name)
        self.state = AgentState.RUNNING

    def stop(self) -> None:
        """
        Stop the agent.
        """
        logger.info("%s stopped", self.name)
        self.state = AgentState.STOPPED
