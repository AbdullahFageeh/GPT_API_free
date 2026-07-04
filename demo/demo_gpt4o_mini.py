from openai import OpenAI
import os

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get("OPENAI_API_KEY", "YOUR API KEY"),
    base_url="https://api.chatanywhere.tech/v1"
)

# 非流式响应
def gpt_4o_mini_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    print(completion.choices[0].message.content)

# 流式响应
def gpt_4o_mini_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    stream = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        stream=True,
    )
    import sys
    # ⚡ Bolt: Optimize by caching sys.stdout.write and reducing attribute lookups
    write = sys.stdout.write
    for chunk in stream:
        choice = chunk.choices[0]
        content = choice.delta.content
        if content is not None:
            write(content)
    sys.stdout.flush()
    print()

if __name__ == '__main__':
    messages = [{'role': 'user','content': '你好，请介绍一下你自己。'},]
    # 非流式调用
    # gpt_4o_mini_api(messages)
    # 流式调用
    gpt_4o_mini_api_stream(messages)
