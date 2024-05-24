from openai import OpenAI

def Summary_Generation(url):
    client = OpenAI(api_key="API-KEY")
    #print("URL:",url)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": f"""Create a summary of the following article in 3 bullet points. Total words should be strictly less than 60 words. Do not return anything else. If link provided is not an article then return "None"\n""",
            },
            {"role": "user", "content": f"{url}"},
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # ans = response.choices[0].message.content
    summary = response.choices[0].message.content

    return summary
