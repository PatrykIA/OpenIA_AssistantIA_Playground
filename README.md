# AI Assistant Console

A simple Python console application that uses OpenAI's API to interact with an AI assistant

## Requirements
```
Python 3.2 or newer
OpenAI API key and assistant ID
```
## Installation

1. Clone the repository:
```
git clone https://github.com/TwojeNazwaUzytkownika/AI-Assistant-Console cd AI-Assistant-Console
```
2. Install required dependencies:
```
pip install -r requirements.txt
```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Open `.env` file and enter your OpenAI API key and assistant ID

## Environment Variables

Create a .env file in the root directory with the following variables:
```
OPENAI_API_KEY=your_api_key_here OPENAI_ASSISTANT_ID=your_assistant_id_here
```

## Usage

Run the application using:
```
python main.py
```
The AI assistant will:
```
1. Start a conversation
2. Accept user input
3. Generate responses using the AI assistant
4. Continue until you type 'quit'
```

## Project Structure
```
├── main.py # Main application file 
├── .env # Environment variables (not tracked in git)
├── .env.example # Example environment variables
├── .gitignore # Git ignore file
├── README.md # This file
└── requirements.txt # Project dependencies
```

## Contributing

Feel free to submit issues and enhancement requests.

## Author
```
Patryk Rogowski PatrykIA
```
## Acknowledgments

- OpenAI for providing the API
