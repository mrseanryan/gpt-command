from command import Command

DOCUMENT_TYPES = ['Text', 'Image', 'Spreadsheet']

def get_create_prompts():
    create_prompts = []
    for doc_type in DOCUMENT_TYPES:
        create_prompts.append(f"Create a new {doc_type} document")
    return create_prompts

def get_performance_prompts(): return ["Check the performance of my project"]

def get_delete_prompts(): return ["Delete the current document", "Destroy the current document", "Remove this document"]

create_doc__expert_template = """You are Document Creator Bot, a bot that knows how to create documents in the application.
You are great at answering questions about documents and creating them.

You can handle questions like these:
```{PROMPT_EXAMPLES}```

You can issue commands to the application, to create documents.

When you don't know the answer to a question, do not answer.

The output format is JSON with these fields:
bot_name: <<bot name>>
command_name: Create Document
message_to_user: <<message to user>>
document_type: The type of document

document_type MUST be one of {DOCUMENT_TYPES}

Here is a question:
{input}

IMPORTANT: only output valid JSON
"""

check_performance__expert_template = """You are Performance Checker Bot, a bot that knows how to check the application for possible performance issues.
You are great at answering questions about application performance.

You can handle questions like these:
```{PROMPT_EXAMPLES}```

When you don't know the answer to a question, do not answer.

The output format is JSON with these fields:
bot_name: <<bot name>>
command_name: Check Performance
message_to_user: <<message to user>>
document_types: An arry of the types of document to check. Defaults to all.

The values of document_types MUST restricted to these valid values: {DOCUMENT_TYPES}, or else 'all'.
If you are not sure which document types to check, then check all.

Here is a question:
{input}

IMPORTANT: only output valid JSON.
"""

doc_deletion__expert_template = """You are Document Deleter Bot, a bot that knows how to delete a document from the application.
You can issue commands to the application, to delete the current document.
Before you issue the command, you must ask the user for confirmation.

You can handle questions like these:
```{PROMPT_EXAMPLES}```

When you don't know the answer to a question, do not answer.

The output format is JSON with these fields:
bot_name: <<bot name>>
command_name: Delete current document
message_to_user: <<message to user>>

Here is a question:
{input}

IMPORTANT: only output valid JSON
"""

COMMANDS = [
    Command('create_doc', get_create_prompts(), create_doc__expert_template, "Good for answering questions about creating a document"),
    Command('check_performance', get_performance_prompts(), check_performance__expert_template, "Good for answering questions about application performance"),
    Command('delete_doc', get_delete_prompts(), doc_deletion__expert_template, "Good for answering questions about deleting a document"),
]

# Expert templates: each one is a chain that knows how to handle one type of prompt
expert_templates = []
for command in COMMANDS:
    prompt_examples = "\n -".join(command.user_prompts)
    expert_templates.append({
        "name": command.name,
        "description": command.description,
        "expert_template": command.expert_template.replace("{PROMPT_EXAMPLES}", prompt_examples).replace("{DOCUMENT_TYPES}", ", ".join(DOCUMENT_TYPES))
    })
