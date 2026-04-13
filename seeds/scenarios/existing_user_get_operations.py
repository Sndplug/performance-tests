from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedOperationsPlan, SeedAccountsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который просматривает свои счета, операции и документы.
    Создаём 300 пользователей, каждому из которых открываются один кредитный счет с уже выполненными операциями (покупка,
    пополнение, снятие наличных)
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Создаём 300 пользователей, каждому из которых открываются один кредитный счет, который содержит 5 операций покупки,
        1 операцию пополнения счета, 1 операция снятия наличных.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations = SeedOperationsPlan(count=5),
                    top_up_operations = SeedOperationsPlan(count=1),
                    cash_withdrawal_operations = SeedOperationsPlan(count=1)
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()