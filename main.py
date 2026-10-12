from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()

response = client.system_one(
    state="The deploy failed twice and customers are seeing 500s.",
    questions={
        "route": Choice(
            instructions="Which team should handle this?",
            criteria={
                "platform": "Infrastructure, deploys, runtime failures",
                "product": "Application behavior and product defects",
                "support": "Customer communication and follow-up",
            },
        ),
        "severity": Score(
            instructions="How severe is the incident?",
            criteria=["low", "medium", "high"],
        ),
        "urgent": Noul(
            instructions="This requires immediate attention",
        ),
    },
)

print(response.answers["route"].choice)
print(response.answers["route"].confidence)
print(response.answers["urgent"].noul)