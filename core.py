# ref: https://python.langchain.com/docs/modules/chains/foundational/router

from langchain.chains.router import MultiPromptChain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

import config

def create_chain(expert_templates):

    llm = OpenAI()

    destination_chains = {}
    for p_info in expert_templates:
        name = p_info["name"]
        expert_template = p_info["expert_template"]
        prompt = PromptTemplate(template=expert_template, input_variables=["input"])
        chain = LLMChain(llm=llm, prompt=prompt)
        destination_chains[name] = chain
    default_chain = ConversationChain(llm=llm, output_key="text")

    from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
    from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

    destinations = [f"{p['name']}: {p['description']}" for p in expert_templates]
    destinations_str = "\n".join(destinations)
    router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
    router_prompt = PromptTemplate(
        template=router_template,
        input_variables=["input"],
        output_parser=RouterOutputParser(),
    )
    router_chain = LLMRouterChain.from_llm(llm, router_prompt)

    chain = MultiPromptChain(
        router_chain=router_chain,
        destination_chains=destination_chains,
        default_chain=default_chain,
        verbose=config.is_debug
    )
    return chain

def execute_prompt(user_prompt, chain):
    # Routes to the right 'expert' chain
    # Falls back to the default chain, which means sending the plain user prompt to the LLM
    return chain.run(user_prompt)
