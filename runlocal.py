import laya_mlx as laya

agent = laya.load("aac6fef/laya-mlx")
result = agent.predict(
    "I need to withdraw money",
    {
        "solution": {
            "type": "choice",
            "instructions": "What should I do?",
            "criteria": ["Go to the bank", "Call the hotline", "Use the online banking"],
        }
    },
)
print(result["answers"]["solution"])