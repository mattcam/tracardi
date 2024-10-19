import aiohttp
from lxml import etree
from tracardi.service.plugin.domain.register import Plugin, Spec, MetaData, Documentation, PortDoc, Form, FormGroup, \
    FormField, FormComponent
from tracardi.service.plugin.domain.result import Result
from tracardi.service.plugin.domain.config import PluginConfig
from tracardi.service.plugin.runner import ActionRunner
from pydantic import field_validator
from tracardi.domain.profile import Profile

class Configuration(PluginConfig):
    api_provider: str
    model: str
    prompt: str
    output_format: str

    @field_validator('api_provider')
    @classmethod
    def api_provider_must_not_be_empty(cls, value):
        if value.strip() == "":
            raise ValueError("API provider must not be empty.")
        return value
    def api_provider_must_be_valid(cls, value):
        if value.strip().lower() != "cloudflare":
            raise ValueError("API provider must be a valid API provider.")
        return value

    @field_validator('model')
    @classmethod
    def model_must_not_be_empty(cls, value):
        if value.strip() == "":
            raise ValueError("Model must not be empty.")
        return value
    
    @field_validator('prompt')
    @classmethod
    def prompt_must_not_be_empty(cls, value):
        if value.strip() == "":
            raise ValueError("Prompt must not be empty.")
        return value

    @field_validator('output_format')
    @classmethod
    def output_format_must_not_be_empty(cls, value):
        if value.strip() == "":
            raise ValueError("Output format must not be empty.")
        return value    
    def output_format_must_be_valid(cls, value):
        if value.strip().lower() != "json":
            raise ValueError("Output format must be a valid type.")
        return value

def validate(config: dict):
    return Configuration(**config)

class genAIPromptAction(ActionRunner):
    
    config: Configuration
    
    async def set_up(self, init):
        self.config = validate(init)

    async def run(self, payload: dict, in_edge=None) -> Result:

        dot = self._get_dot_accessor(payload)
        
        try:
            
            print('A')
            
            api_provider=dot[self.config.api_provider]
            model=dot[self.config.model]
            prompt=dot[self.config.prompt]
            output_format=dot[self.config.output_format]
            print('B')
            
            llm_template = """Human: {question}
            AI Assistant: You are a friendly assistant """
            print('C')

            llm_prompt = PromptTemplate.from_template(llm_template)
            print('D')

            if api_provider == 'cloudflare':
                try:
                    llm = CloudflareWorkersAI(account_id='ABC', api_token='123',model=model)
                except Exception as e:
                    print(f"Error initializing CloudflareWorkersAI: {e}")
                    raise
            
            print('E')
            print(llm)
            llm_chain = LLMChain(prompt=llm_prompt, llm=llm)
            print('F')
            print(llm_chain)
            print(prompt)
            response = llm_chain.run(prompt)
            print('G')

            if output_format == "json":
                return {
                    "port":"result", 
                    "value": {
                        "output": response,
                        "prompt": prompt
                    }
                }
            
        except Exception as e:
            print('**********************')
            return Result(value={"message": str(e)}, port="error")  
 
def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module=__name__,
            className=genAIPromptAction.__name__,
            inputs=["payload"],
            outputs=["result", "error"],
            version="1.0.3",  
            init={
                "api_provider": "",  
            },
            form=Form(groups=[
                FormGroup(
                    name="genAIPrompt configuration",
                    fields=[
                        FormField(
                            id="api_provider",
                            name="API Provider",
                            description="The provider that will be used for the LLM request. Options include ['cloudflare'].",
                            component=FormComponent(type="dotPath", props={
                                "label": "API Provider"
                            })
                        ),
                        FormField(
                            id="model",
                            name="Model",
                            description="The model to be used with the request.",
                            component=FormComponent(type="dotPath", props={
                                "label": "Model"
                            })
                        ),
                        FormField(
                            id="prompt",
                            name="Prompt",
                            description="The prompt for the request.",
                            component=FormComponent(type="dotPath", props={
                                "label": "Prompt"
                            })
                        ),
                        FormField(
                            id="output_format",
                            name="Output Format",
                            description="The output format that will be returned. Options include ['json'].",
                            component=FormComponent(type="dotPath", props={
                                "label": "Output Format"
                            })
                        ),
                    ])
            ]),
            license="MIT",
            author="Matt Cameron",
            manual="Sitemap",  

        ),
        metadata=MetaData(
            name='genAI Prompt',
            desc='Submits a request to a LLM service provider.',
            icon='genAIPromptAction',
            group=['genAIPrompts'],
            documentation=Documentation(
                inputs={
                    "payload": PortDoc(desc="This port takes payload object.")
                },
                outputs={
                    "result": PortDoc(desc="Returns response from genAIPromptAction service."),
                    "error": PortDoc(desc="Returns error message if plugin fails.")
                }
            )
        )
    )
