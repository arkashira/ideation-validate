from notion_integration import create_notion_page, create_signal
import json

def test_create_notion_page():
    signal = create_signal("Test Signal", "This is a test signal", {"revenue": 100}, "https://example.com", "123")
    notion_page = create_notion_page(signal)
    notion_page_dict = json.loads(notion_page)
    assert notion_page_dict["title"] == "Test Signal"
    assert notion_page_dict["description"] == "This is a test signal"
    assert notion_page_dict["revenue_data"] == {"revenue": 100}
    assert notion_page_dict["backlink"] == "https://example.com/signals/123"

def test_create_signal():
    signal = create_signal("Test Signal", "This is a test signal", {"revenue": 100}, "https://example.com", "123")
    assert signal.title == "Test Signal"
    assert signal.description == "This is a test signal"
    assert signal.revenue_data == {"revenue": 100}
    assert signal.backlink == "https://example.com/signals/123"

def test_create_signal_empty_revenue_data():
    signal = create_signal("Test Signal", "This is a test signal", {}, "https://example.com", "123")
    assert signal.title == "Test Signal"
    assert signal.description == "This is a test signal"
    assert signal.revenue_data == {}
    assert signal.backlink == "https://example.com/signals/123"
