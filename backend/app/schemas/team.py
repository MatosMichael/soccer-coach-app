"""Team profile fields and validation."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class Team:
    """A team profile, validated when it is created."""

    name: str
    age_group: str
    skill_level: Literal["beginner", "intermediate", "advanced"]
    player_count: int
    formation: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Team name must be non-blank text.")
        if not isinstance(self.age_group, str) or not self.age_group.strip():
            raise ValueError("Age group must be non-blank text, such as U10 or U12.")
        if self.skill_level not in ("beginner", "intermediate", "advanced"):
            raise ValueError("Skill level must be beginner, intermediate, or advanced.")
        if type(self.player_count) is not int or self.player_count <= 0:
            raise ValueError("Player count must be a positive whole number.")

        self.name = self.name.strip()
        self.age_group = self.age_group.strip()
