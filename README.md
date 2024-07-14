# Chatbot README

## Description

This project implements a simple chatbot inspired by Eliza, capable of responding to user inputs based on predefined patterns. The bot uses Flask for the web framework, HTML/CSS for the frontend, and JavaScript for dynamic interaction with the user.

The chatbot simulates a conversation where it responds to user messages using predefined patterns similar to how Eliza, a famous early natural language processing computer program, functioned.

## Features

- **Prompt-based Responses**: Responds to user inputs based on predefined patterns stored in a Python dictionary.
- **Web Interface**: Provides a web-based chat interface similar to WhatsApp, with messages displayed alternately on the left and right sides.
- **Dynamic Messaging**: Messages are dynamically appended to the chat window using JavaScript without page reloads.

## Technologies Used

- Python
- Flask
- HTML/CSS
- JavaScript

## Installation

### Prerequisites

- Python (version 3.7 or higher)
- pip (Python package installer)
- Flask (`pip install flask`)

### Steps to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/VISHALKAVIYARASU/Mental_Health_Supporter.git
   cd Mental_Health_Supporter
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

   This will start the Flask development server locally.

4. **Open your web browser:**

   Navigate to `http://127.0.0.1:5000/` to access the chatbot interface.

## Usage

- **Chat Interface**: Enter messages in the input box at the bottom of the chat window and click "Send" to see the bot's responses.
- **Conversation**: The bot responds to user inputs based on predefined patterns stored in `app.py`. You can modify or extend these patterns to customize the bot's behavior.

## Example Conversation

User: Hello  
Bot: Hello, how can I help you?

User: I feel sad  
Bot: Why do you feel sad?

User: I am tired  
Bot: How long have you been tired?

## Known Issues

- Currently, the bot's responses are static and prompt-based. Future updates may include integrating with AI models for more dynamic responses.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
