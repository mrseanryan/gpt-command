# gpt-command
Map natural language instructions to specific commands, suitable for controlling Home Automation or an App

## Dependencies

Requires a LLM - by default, uses OpenAI's ChatGPT.
But since langchain is used, then other sources could be used.

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
