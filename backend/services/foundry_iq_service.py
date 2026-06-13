"""Local Foundry IQ-ready knowledge pack service."""

from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[2]
FOUNDRY_PACK_DIR = BASE_DIR / "knowledge" / "foundry_iq_pack"


def _read_markdown_sources() -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    for path in sorted(FOUNDRY_PACK_DIR.glob("*.md")):
        sources.append(
            {
                "source_name": path.name,
                "source_path": str(path.relative_to(BASE_DIR)),
                "content": path.read_text(encoding="utf-8"),
            }
        )
    return sources


def _snippet(content: str, query_terms: set[str]) -> str:
    lines = [line.strip() for line in content.splitlines() if line.strip() and not line.startswith("#")]
    if not lines:
        return ""
    for line in lines:
        lower = line.lower()
        if any(term in lower for term in query_terms):
            return line[:260]
    return lines[0][:260]


def retrieve_foundry_evidence(query: str = "", limit: int = 5) -> list[dict[str, Any]]:
    """Return grounded snippets from approved local synthetic markdown sources."""

    query_terms = {term.lower() for term in query.replace("_", " ").split() if len(term) > 3}
    if not query_terms:
        query_terms = {"agent", "blueprint", "governance", "approval", "source"}

    evidence: list[dict[str, Any]] = []
    for source in _read_markdown_sources():
        content = source["content"]
        lower = content.lower()
        score = sum(1 for term in query_terms if term in lower)
        if score or len(evidence) < limit:
            evidence.append(
                {
                    "layer": "Foundry IQ",
                    "source_name": source["source_name"],
                    "source_path": source["source_path"],
                    "snippet": _snippet(content, query_terms),
                    "citation": source["source_name"],
                    "match_score": score,
                }
            )

    return sorted(evidence, key=lambda item: item["match_score"], reverse=True)[:limit]


def get_foundry_iq_status() -> dict[str, Any]:
    sources = _read_markdown_sources()
    return {
        "name": "Foundry IQ",
        "status": "local_demo_ready",
        "mode": "local_demo",
        "description": "Grounded knowledge pack with cited synthetic sources for blueprint and governance reasoning.",
        "document_count": len(sources),
        "sources": [
            {"source_name": source["source_name"], "source_path": source["source_path"]}
            for source in sources
        ],
        "signals": [
            {"label": "Approved knowledge sources", "value": len(sources)},
            {"label": "Grounded retrieval", "value": "ready"},
            {"label": "Source citations", "value": "enabled"},
        ],
    }
