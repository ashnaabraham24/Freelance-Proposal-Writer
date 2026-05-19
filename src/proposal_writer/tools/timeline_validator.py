from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class TimelineValidatorInput(BaseModel):

    deliverables: int = Field(
        ...,
        description="Number of project deliverables"
    )

    days: int = Field(
        ...,
        description="Proposed timeline in days"
    )


class TimelineValidator(BaseTool):

    name: str = "Timeline Validator"

    description: str = (
        "Checks whether the project timeline is realistic. "
        "Flags timelines under 2 days per deliverable "
        "or above 7 days per deliverable."
    )

    args_schema: Type[BaseModel] = TimelineValidatorInput

    def _run(
        self,
        deliverables: int,
        days: int
    ) -> str:

        ratio = days / deliverables

        min_days = deliverables * 2
        max_days = deliverables * 7

        if ratio < 2:

            return (
                f"Unrealistic timeline. "
                f"{days} days for "
                f"{deliverables} deliverables. "
                f"Recommended range: "
                f"{min_days}-{max_days} days."
            )

        elif ratio > 7:

            return (
                f"Timeline too padded. "
                f"{days} days for "
                f"{deliverables} deliverables. "
                f"Recommended range: "
                f"{min_days}-{max_days} days."
            )

        return (
            f"Timeline looks realistic. "
            f"Recommended range: "
            f"{min_days}-{max_days} days."
        )