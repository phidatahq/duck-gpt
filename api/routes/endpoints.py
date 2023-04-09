from dataclasses import dataclass


@dataclass
class ApiEndpoints:
    PING: str = "/ping"
    HEALTH: str = "/health"
    DUCKGPT: str = "/duckgpt"


endpoints = ApiEndpoints()
