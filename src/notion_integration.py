import json
from dataclasses import dataclass
from urllib.parse import urljoin

@dataclass
class Signal:
    title: str
    description: str
    revenue_data: dict
    backlink: str

def create_notion_page(signal: Signal) -> str:
    notion_page = {
        "title": signal.title,
        "description": signal.description,
        "revenue_data": signal.revenue_data,
        "backlink": signal.backlink
    }
    return json.dumps(notion_page)

def get_backlink(platform_url: str, signal_id: str) -> str:
    return urljoin(platform_url, f"/signals/{signal_id}")

def create_signal(title: str, description: str, revenue_data: dict, platform_url: str, signal_id: str) -> Signal:
    backlink = get_backlink(platform_url, signal_id)
    return Signal(title, description, revenue_data, backlink)
