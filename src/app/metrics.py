from prometheus_client import Summary, Gauge, Counter, Info

PORT = Info("port", "port")
BASE_ROOT_CALLED = Counter("base_root_called", "base root called")
WEBSOCKET_ACTIVE = Gauge("websocket_active", "active websosckets")
WEBSOCKET_MSGS_RECEIVED = Counter(
    "websockets_msgs_received", "web socket msgs received"
)
