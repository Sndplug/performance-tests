from grpc import Channel, insecure_channel

def build_gateway_grpc_client() -> Channel:
    """
    Функция создаёт экземпляр grpc.Channel с базовыми настройками для сервиса http-gateway.

    :return: Готовый к использованию объект insecure_channel.
    """
    return insecure_channel("http://localhost:9003")