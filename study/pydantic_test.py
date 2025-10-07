from dataclasses import dataclass
from re import X

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

from bank_database import DatabaseConn

@dataclass
class SupportDependencies:
    customer_id: int
    db: DatabaseConn

class SupportResult(BaseModel):
    support_advice: str = Field(description = 'Advice returned to the customer')
    block_card: bool = Field(description = 'Whether to block the customer card')
    risk: int = Field(description = 'Risk level of query', ge= 0, le = 10)


support_agent = Agent(
    'gemini-1.5-flash',
    deps_type = SupportDependencies,
    result_type = SupportResult,
    system_prompt = (
        'You are a support agent in our bank, give the '
    )
)