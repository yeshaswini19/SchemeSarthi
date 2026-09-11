from typing import List, Literal

from pydantic import BaseModel, Field


class Eligibility(BaseModel):
    status: Literal[
        "likely_eligible",
        "likely_not_eligible",
        "cannot_determine"
    ]

    reasons: List[str] = Field(default_factory=list)

    missing_information: List[str] = Field(default_factory=list)


class Evidence(BaseModel):
    claim: str
    source: str


class SchemeAnalysis(BaseModel):
    scheme_name: str

    summary: str

    eligibility: Eligibility

    benefits: List[str] = Field(default_factory=list)

    documents: List[str] = Field(default_factory=list)

    application_steps: List[str] = Field(default_factory=list)

    evidence: List[Evidence] = Field(default_factory=list)