import os
import json
from typing import List
from agentverse.message import Message


def get_evaluation(setting: str = None, messages: List[Message] = None, agent_nums: int = None) -> List[dict]:
    evaluation = []
    
    # 确保我们不超出 messages 列表的范围
    for i in range(agent_nums):
        if i < len(messages):  # 检查索引是否有效
            agent_response = messages[i]
            evaluation_dict = {
                "agent_id": i,
                "message": agent_response
            }
            evaluation.append(evaluation_dict)
        else:
            # 如果消息为空或超出范围，可以处理为 None 或其他值
            evaluation.append({
                "agent_id": i,
                "message": "No valid response"
            })
    
    return evaluation
