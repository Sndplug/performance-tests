from grpc import Channel, insecure_channel

def build_gateway_grpc_client() -> Channel:
    """
    Функция создаёт экземпляр grpc.Channel с базовыми настройками для сервиса http-gateway.

    :return: Готовый к использованию объект insecure_channel.
    """
    return insecure_channel("localhost:9003")

def build_gateway_locust_grpc_client(environment: Environment) -> Channel:
    """
    Фабричная функция для создания gRPC-канала, адаптированного для Locust.
    В канал автоматически встраивается интерцептор LocustInterceptor,
    который регистрирует вызовы в системе метрик Locust.

    :param environment: Среда выполнения Locust (необходима для отправки событий).
    :return: gRPC-канал с интерцептором, пригодный для нагрузочного тестирования.
    """
    # Создаём экземпляр интерцептора, передаём в него окружение Locust
    locust_interceptor = LocustInterceptor(environment=environment)

    # Создаём обычный канал
    channel = insecure_channel("localhost:9003")

    # Оборачиваем канал интерцептором, чтобы все запросы проходили через него
    return intercept_channel(channel, locust_interceptor)