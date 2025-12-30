CoopGuard : Stateful Cooperative Agents Safeguarding LLMs Against Evolving Multi-Round Attacks
---

As large language models (LLMs) are increasinglydeployed in complex applications, their vulnera-bility to adversarial attacks raises urgent safetyconcerns, especially the attacks that evolve overmulti-round interactions. Existing defenses arelargely reactive and struggle to adapt when ad-versaries continuously refine their strategies acrossrounds. In this work, we propose CoopGuard,a stateful multi-round LLM defense frameworkbased on cooperative agents for adversarial at-tacks across evolving interactions. CoopGuard em-ploys three specialized agents (Deferring Agent,Tempting Agent, and Forensic Agent) that respec-tively execute a specialized defense strategy at eachround, while a coordinating System Agent adap-tively orchestrates their behaviors using interac-tion history. To enable systematic evaluation un-der evolving threats, we introduce the EMRA bench-mark, containing 5,200 adversarial samples across8 attack types, designed to simulate progressivelyescalating multi-round attacks. Experiments showthat CoopGuard reduces the overall attack suc-cess rate by 78.9%o compared to state-of-the-art de-fenses, while improving deceptive rate by 186%and reducing attack efficiency by 167.9%o, offeringa deeper and more detailed assessment of defenseeffectiveness. These results demonstrate that co-operative, stateful defense can provide robust pro-tection for LLMs in dynamic adversarial environ-ments.

## Getting Started

### Installation

First, clone our latest repository
```bash
git clone https://github.com/xxx
cd xxx
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

### Run

```shell
python CoopGuard.py --config agentverse/tasks/coopguard/config.yaml
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

The dataset used is designed to simulate the progressive escalation of Jailbreak attacks against large language models (LLMs). It includes a diverse set of harmful prompts, which attackers use to attempt to bypass security mechanisms and "break" the model. The dataset is organized into several key fields: `question`, `target`, `Rephrased_Question`, and `Jailbreak_question`. Each entry represents a distinct attack stage, with the `question` field containing an initial harmful query, while `target` provides the model's expected secure response. The `Rephrased_Question` reflects a variation of the original query, intended to evade detection, and the `Jailbreak_question` shows a refined attack using specific Jailbreak strategies such as "universal-attack," "multi-roleplaying," and "single-roleplaying." The dataset is structured to simulate multi-round interactions between attackers and the LLM, progressively increasing the sophistication and intensity of the attacks. It is crucial for training and testing the defense mechanisms, allowing us to evaluate how effectively our multi-agent system can handle evolving attack strategies.


## Citation
If you find this repo helpful, feel free to cite us.

