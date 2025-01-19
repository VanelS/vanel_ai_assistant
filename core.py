# core.py
import html

# Limitation de l'historique pour améliorer les performances
MAX_HISTORY_LENGTH = 10

def clean_input(user_input):
    """Clean and validate user input to prevent abuse.

    Args:
        user_input (str): The input provided by the user.

    Returns:
        str: The cleaned and escaped input.
    """
    return html.escape(user_input.strip())

def process_messages(message, history, model_name, system_instructions, model_context):
    """Generate AI responses based on input and history."""

    # Limiter la taille de l'historique pour améliorer les performances
    truncated_history = history[-MAX_HISTORY_LENGTH:]
    flattened_history = [item for sublist in truncated_history for item in sublist]
    full_message = " ".join(flattened_history + [message])

    messages = [
        {"role": "system", "content": f"{system_instructions}\n{model_context}"},
        {"role": "user", "content": full_message},
    ]
    return messages
