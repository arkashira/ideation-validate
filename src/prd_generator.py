import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Idea:
    title: str
    problem: str
    icp: str
    success_metric: str
    validation_data: Dict[str, str]

def generate_prd(idea: Idea) -> str:
    prd = f"# {idea.title}\n"
    prd += f"## Problem\n{idea.problem}\n"
    prd += f"## ICP\n{idea.icp}\n"
    prd += f"## Success Metric\n{idea.success_metric}\n"
    prd += f"## Validation Data\n"
    for key, value in idea.validation_data.items():
        prd += f"- {key}: {value}\n"
    return prd

def export_to_gist(prd: str, gist_title: str) -> str:
    # Simulate GitHub Gist export
    return f"Gist exported: {gist_title}"

def export_to_local(prd: str, file_name: str) -> str:
    # Simulate local download
    return f"File saved: {file_name}"

def generate_links(idea: Idea) -> Dict[str, str]:
    links = {
        "source_queries": f"https://example.com/source-queries/{idea.title}",
        "wtp_evidence": f"https://example.com/wtp-evidence/{idea.title}",
    }
    return links
