import logging
import math
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Set up logging to debug issues if any
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function to start the bot and send a greeting message
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! I am your MathBot. Ask me any math problem like "What is 4+4?" or "What is 2*3?"')

# Define a function to process math-related messages
async def calculate(update: Update, context: CallbackContext) -> None:
    message = update.message.text.strip()  # Get the message from the user and remove extra spaces
    
    try:
        # Ensure that the input is a valid mathematical expression using eval()
        allowed_characters = "0123456789+-*/().^sqrt"
        
        # Validate the message, ensuring it only contains valid characters
        if not all(c in allowed_characters for c in message):
            raise ValueError("Invalid characters in the expression")
        
        # Replace 'sqrt' with math.sqrt for proper evaluation
        message = message.replace("sqrt", "math.sqrt")
        
        # Evaluate the mathematical expression
        result = eval(message)
        
        # Send the result to the user
        await update.message.reply_text(f"The result is: {result}")
    
    except Exception as e:
        # Handle any errors (invalid expressions, etc.)
        await update.message.reply_text(f"Sorry, I couldn't understand that. Error: {str(e)}")

def main() -> None:
    # Replace with your bot's API token
    api_token = '7925177225:AAFjL-4G_4xguNl4HPgVxFlA_ms8bfD0Fms'

    # Create an Application object using the token
    application = Application.builder().token(api_token).build()

    # Add a command handler to start the bot
    application.add_handler(CommandHandler('start', start))

    # Add a message handler to process math messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
