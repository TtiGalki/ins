import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def privet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hydra Dominatus")


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
