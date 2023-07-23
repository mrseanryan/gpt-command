# gpt-command
Map natural language instructions to specific commands, suitable for controlling Home Automation or an App

## Dependencies

Requires a LLM - by default, uses OpenAI's ChatGPT.
But since langchain is used, then other sources could be used.

## Usage

```go.sh```

### Example Output

```
How can I help you with your project? >Create a new paper
---
>> Create a new paper

{"bot_name": "Document Creator Bot", "command_name": "Create Document", "document_type": "Paper"}
How can I help you with your project? >I don't need this anymore
---
>> I don't need this anymore

{
    "bot_name": "Document Deleter Bot",
    "command_name": "Delete current document"
}
How can I help you with your project? >I need to do some calculations
---
>> I need to do some calculations
 Sure, what kind of calculations?
How can I help you with your project? >A budget, like in Excel
---
>> A budget, like in Excel

{
"bot_name": "Document Creator Bot",
"command_name": "Create Document",
"document_type": "Spreadsheet"
}
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
