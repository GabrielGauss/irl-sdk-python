"""Data models matching the IRL Engine wire format."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class TradeAction(str, Enum):
    LONG = "Long"
    SHORT = "Short"
    NEUTRAL = "Neutral"


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"
    TWAP = "TWAP"


@dataclass
class AuthorizeRequest:
    # Agent identity
    agent_id: str                    # UUID string — must be registered in the MAR
    model_id: str                    # Human-readable model identifier
    model_hash_hex: str              # SHA-256 of the agent's model weights (hex)
    prompt_version: str = "v1"
    feature_schema_id: str = "default"
    hyperparameter_checksum: str = "0" * 64

    # Trade intent
    action: TradeAction = TradeAction.NEUTRAL
    asset: str = ""
    order_type: OrderType = OrderType.MARKET
    venue_id: str = ""
    quantity: float = 0.0
    notional: float = 0.0
    notional_currency: str = "USD"
    multiplier: float = 1.0
    limit_price: Optional[float] = None
    stop_price: Optional[float] = None
    client_order_id: Optional[str] = None
    reduce_only: bool = False

    # Temporal context
    agent_valid_time: int = 0        # Unix ms of the agent's decision time

    # Filled automatically by IRLClient.authorize()
    heartbeat: Optional[dict] = None
    regulatory: Optional[dict] = None


@dataclass
class AuthorizeResult:
    trace_id: str
    reasoning_hash: str
    authorized: bool
    shadow_blocked: bool
