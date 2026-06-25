import pytest
from prd_generator import generate_prd, export_to_gist, export_to_local, generate_links, Idea

def test_generate_prd():
    idea = Idea(
        title="Test Idea",
        problem="Test Problem",
        icp="Test ICP",
        success_metric="Test Success Metric",
        validation_data={"Test Key": "Test Value"},
    )
    prd = generate_prd(idea)
    assert prd.startswith("# Test Idea")
    assert "Test Problem" in prd
    assert "Test ICP" in prd
    assert "Test Success Metric" in prd
    assert "Test Key: Test Value" in prd

def test_export_to_gist():
    prd = "Test PRD"
    gist_title = "Test Gist"
    result = export_to_gist(prd, gist_title)
    assert result == "Gist exported: Test Gist"

def test_export_to_local():
    prd = "Test PRD"
    file_name = "test_prd.md"
    result = export_to_local(prd, file_name)
    assert result == "File saved: test_prd.md"

def test_generate_links():
    idea = Idea(
        title="Test Idea",
        problem="Test Problem",
        icp="Test ICP",
        success_metric="Test Success Metric",
        validation_data={"Test Key": "Test Value"},
    )
    links = generate_links(idea)
    assert links["source_queries"] == "https://example.com/source-queries/Test Idea"
    assert links["wtp_evidence"] == "https://example.com/wtp-evidence/Test Idea"

def test_empty_idea():
    idea = Idea(
        title="",
        problem="",
        icp="",
        success_metric="",
        validation_data={},
    )
    prd = generate_prd(idea)
    assert prd == "# \n## Problem\n\n## ICP\n\n## Success Metric\n\n## Validation Data\n"
