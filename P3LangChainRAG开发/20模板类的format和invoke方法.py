from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi

"""
PromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
FewShotPromptTemplate -> StringPromptTemplate -> BasePromptTemplate  -> RunnableSerializable -> Runnable
ChatPromptTemplate -> BaseChatPromptTemplate -> BasePromptTemplate  -> RunnableSerializable -> Runnable
Tongyi -> BaseLLM -> BaseLanguageModel -> RunnableSerializable -> Runnable
ChatTongyi -> BaseChatModel -> BaseLanguageModel -> RunnableSerializable -> Runnable
"""

template = PromptTemplate.from_template("我的邻居是: {lastname}，最喜欢: {hobby}")
# 传参
res = template.format(lastname = "张大名", hobby="钓鱼")
print(res, type(res))
# 传字典
res2 = template.invoke({"lastname": "周揭露", "hobby": "唱歌"})
print(res2, type(res2))