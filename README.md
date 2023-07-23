# gpt-command
Map natural language instructions to specific commands, suitable for controlling Home Automation or an App

## Dependencies

Requires a LLM - by default, uses OpenAI's ChatGPT.
But since langchain is used, then other sources could be used.

## Usage

To use as a CLI (Command Line Interface) REPL (Read-Eval-Print Loop) prompt:
```go.sh```

or to use as a web server:

```go_web.sh```

For the web server, you need to pass the user prompt as GET query parameter 'p'.

Example:

- http://localhost:8083/?p=I%20need%20a%20new%20letter

So, another application can use the web server to send in natural language prompts from the user, and receive specific commands in JSON format.

The other application can then execute the given command.

## Commands

Commands with prompts are configured to suit your application.

Example - see [config__application_commander.py](config__application_commander.py).

### Example Output

```
How can I help you with your project? >Create a new paper
---
>> I need a new text document

{
    "bot_name": "Document Creator Bot",
    "command_name": "Create Document",
    "message_to_user": "Creating a new Text Document",
    "document_type": "Text"
}

How can I help you with your project? >I don't need this anymore
---
>> I don't need this anymore

{
    "bot_name": "Document Deleter Bot",
    "command_name": "Delete current document"
    "message_to_user": "Are you sure you want to delete the current document?"
}

How can I help you with your project? >A budget, like in Excel
---
>> A budget, like in Excel

{
    "bot_name": "Document Creator Bot",
    "command_name": "Create Document",
    "message_to_user": "Creating a new spreadsheet document...",
    "document_type": "Spreadsheet"
}
```

# Non-Command user prompts

User prompts that are not related to any of the known Commands, are sent directly to the LLM.

Examples:

```
>> Who won the battle of Agincourt, and why was it fought?
{"general_response": " The battle of Agincourt was fought in 1415 during the Hundred Years' War between the English and French. The English army, led by King Henry V, was victorious in the battle. The French army was significantly larger, but the English were able to win thanks to their superior tactics. "}
```

```
>> What is my favourite color?
{"general_response": " I'm sorry, I don't know. "}
```

## Set up

```
pip3 install --upgrade langchain openai
```

Set environment variable with your OpenAI key:

```
export OPENAI_API_KEY="xxx"
```

Add that to your shell initializing script (`~/.zprofile` or similar)

Load in current terminal:

```
source ~/.zprofile
```

## Test

`test.sh`

or

`python3 test.py`
