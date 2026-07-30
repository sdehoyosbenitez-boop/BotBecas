class NotificationService:

    def __init__(self, telegram):

        self.telegram = telegram

    async def notify(self, scholarships):

        for scholarship in scholarships:

            await self.telegram.send_scholarship(
                scholarship
            )
