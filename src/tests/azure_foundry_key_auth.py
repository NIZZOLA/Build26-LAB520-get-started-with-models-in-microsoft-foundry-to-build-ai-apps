# pip install openai azure-ai-projects>=2.1.0

from openai import OpenAI

project_endpoint = "https://ai-3tbayj7xermkm.services.ai.azure.com/api/projects/foundry-lab-project"
api_key = "<your-api-key>"  # Substitua pela sua chave de API se não estiver usando Azure AD auth

# Sem AIProjectClient — usa OpenAI direto com a chave
client = OpenAI(
    base_url=project_endpoint.rstrip("/") + "/openai/v1",
    api_key=api_key,
)

my_agent   = "programador"
my_version = "1"

response = client.responses.create(
    model="gpt-4.1-mini",   # modelo base (o agente pode sobrescrever)
    input=[{"role": "user", "content": "Tell me what you can help with."}],
    extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")