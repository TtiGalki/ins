import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def privet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hydra Dominatus")

async def d20(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = random.randint(1, 20)
    await update.message.reply_text(str(number))

async def nine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Ще не вмерла Україна, і слава, і воля,\n"
        "Ще нам, браття молодії, усміхнеться доля.\n"
        "Згинуть наші вороженьки, як роса на сонці,\n"
        "Запануєм і ми, браття, у своїй сторонці.\n\n"
        "Душу, тіло ми положим за нашу свободу.\n"
        "І покажем, що ми, браття, козацького роду.\n\n"
        "Станем, браття, в бій кровавий від Сяну до Дону\n"
        "В ріднім краю панувати не дамо нікому;\n"
        "Чорне море ще всміхнеться, дід Дніпро зрадіє,\n"
        "Ще у нашій Україні доленька наспіє.\n\n"
        "Душу, тіло ми положим за нашу свободу.\n"
        "І покажем, що ми, браття, козацького роду.\n\n"
        "А завзяття, праця щира свого ще докаже,\n"
        "Ще ся волі в Україні піснь гучна розляже,\n"
        "За Карпати відоб'ється, згомонить степами,\n"
        "України слава стане поміж народами.\n\n"
        "Душу, тіло ми положим за нашу свободу.\n"
        "І покажем, що ми, браття, козацького роду."
    )


def main() -> None:
    token = os.getenv("BOT_TOKEN")
    webhook_url = os.getenv("WEBHOOK_URL")
    port = int(os.getenv("PORT", 8080))

    if not token:
        raise ValueError("BOT_TOKEN не задан!")
    if not webhook_url:
        raise ValueError("WEBHOOK_URL не задан!")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("hi", privet))
    app.add_handler(CommandHandler("d20", d20))
    app.add_handler(CommandHandler("900", nine))

    logger.info("Бот запущен. Webhook mode...")
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        secret_token=None,
        webhook_url=f"{webhook_url}/webhook",
        url_path="/webhook",
    )


if __name__ == "__main__":
    main()
