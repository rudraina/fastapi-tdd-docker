from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

from typing import Union, List


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id

async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    print("\n\n\n\n\n\n\n\n\n\n\n","SEE BELOW","\n\n\n\n\n\n\n\n\n\n\n")
    print(summary)
    print("\n\n\n\n\n\n\n\n\n\n\n")
    if summary:
        return summary
    return None

async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries