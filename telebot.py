import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Retrieve the Telegram API key
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")

# Check if the API key is loaded properly
if TELEGRAM_API_KEY is None:
    print("Error: TELEGRAM_API_KEY not found. Please set it in the .env file.")
    exit()

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the user starts the bot."""
    await update.message.reply_text("Hello! I am your math bot. Send me a math problem to solve!")

# Define the function to handle math calculations
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Evaluate the math expression sent by the user."""
    try:
        expression = update.message.text  # Get the text from the message
        result = eval(expression)  # Evaluate the expression
        await update.message.reply_text(f"The result is: {result}")
    except Exception as e:
        await update.message.reply_text("Invalid math expression. Please try again.")

# Main function to set up and run the bot
def main():
    # Create the application with the bot token
    app = Application.builder().token(TELEGRAM_API_KEY).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))

    # Register the message handler to calculate expressions
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    # Start polling for updates
    print("Bot is running...")
    app.run_polling()

# Entry point for the script
if __name__ == "__main__":
    main()
