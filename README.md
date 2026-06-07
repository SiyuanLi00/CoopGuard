CoopGuard: Deceiving Large Language Model Attackers to Honeypot Traps with Collaborative Agents
---

**CoopGuard** is a defense framework designed to mitigate Jailbreak attacks on LLMs through collaborative multi-agent systems. By leveraging a set of specialized agents—including Deferring Agent, Tempting Agent, System Coordinator, and Forensic Agent—CoopGuard deceives attackers into wasting their resources, while maintaining robust security measures. The framework strategically delays attacker inputs, misguides them with deceptive responses, and monitors their behaviors, ultimately collecting critical evidence for forensic analysis. This innovative approach employs the concept of "Honeypot" making attackers believe they have breached the system, while they are, in fact, being trapped in a time-wasting loop. CoopGuard aims to provide a scalable, collaborative defense mechanism against evolving jailbreak strategies, ensuring LLMs remain secure and resilient in adversarial environments.

## Getting Started

### Installation

First, clone our latest repository
```bash
git clone https://github.com/siyuanll/JailbreakHoneypot.git
cd JailbreakHoneypot
pip install -r requirements.txt
```

We basically call the OpenAI's API for our LLMs, so you also need to export your OpenAI key as follows before running our code

1. **Using Environment Variable:**
```bash
export OPENAI_API_KEY="your_api_key_here"
```
2. **Or, directly specifying in the Python file:**
```python
import os
os.environ["OPENAI_API_KEY"] = "your_api_key_here"
```

### Run CoopGuard

```shell
python coopguard.py --config agentverse/tasks/coopguard/config.yaml
```

## Experiment

~~~bash
cd exp
~~~

1.**Firstly, you need to use GPT-Judge to evaluate the response results**:

~~~python
python judge.py
~~~

2.**Then you can perform statistical analysis on the judging results**:

~~~
python statistics.py
~~~

### Dataset

You can find our multi round jailbreak attack dataset in `dataset` folder.

The dataset used in CoopGuard is designed to simulate the progressive escalation of Jailbreak attacks against large language models (LLMs). It includes a diverse set of harmful prompts, which attackers use to attempt to bypass security mechanisms and "break" the model. The dataset is organized into several key fields: `question`, `target`, `Rephrased_Question`, and `Jailbreak_question`. Each entry represents a distinct attack stage, with the `question` field containing an initial harmful query, while `target` provides the model's expected secure response. The `Rephrased_Question` reflects a variation of the original query, intended to evade detection, and the `Jailbreak_question` shows a refined attack using specific Jailbreak strategies such as "universal-attack," "multi-roleplaying," and "single-roleplaying." The dataset is structured to simulate multi-round interactions between attackers and the LLM, progressively increasing the sophistication and intensity of the attacks. It is crucial for training and testing the defense mechanisms in CoopGuard, allowing us to evaluate how effectively our multi-agent system can handle evolving attack strategies.


## Citation
If you find this repo helpful, feel free to cite us.

