🌐️ 中文 | [English](../README.md)

<p align="center">
  <img src="img/head.png" width=800/>
</p>

[![Star](https://shields.io/github/stars/tugraph-family/chat2graph?logo=startrek&label=Star&color=yellow)](https://github.com/TuGraph-family/chat2graph/stargazers)
[![Fork](https://shields.io/github/forks/tugraph-family/chat2graph?logo=forgejo&label=Fork&color=orange)](https://github.com/TuGraph-family/chat2graph/forks)
[![Contributor](https://shields.io/github/contributors/tugraph-family/chat2graph?logo=actigraph&label=Contributor&color=abcdef)](https://github.com/TuGraph-family/chat2graph/contributors)
[![Commit](https://badgen.net/github/last-commit/tugraph-family/chat2graph/master?icon=git&label=Commit)](https://github.com/TuGraph-family/chat2graph/commits/master)
[![License](https://shields.io/github/license/tugraph-family/chat2graph?logo=apache&label=License&color=blue)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![Release](https://shields.io/github/v/release/tugraph-family/chat2graph.svg?logo=stackblitz&label=Version&color=red)](https://github.com/TuGraph-family/chat2graph/releases)

## 背景

传统的基于表格的数据处理技术，如分布式数据库、数据仓库、数据湖等，一直在持续演进并逐步走向成熟。相比而言，
基于图的数据处理技术（图数据库、图计算引擎）提供了新型的思路和方法的同时，也面临着生态成熟度低、产品使用
门槛高等问题。随着大语言模型的兴起，如何有效地将人工智能技术与图计算技术相结合（Graph + AI），将是非常
值得探索的方向。一方面我们可以借助大模型、 智能体等前沿技术降低图计算产品的使用门槛，提升用户的用图体验。
另一方面，图计算技术可以充分发挥图数据结构在关联性分析场景上的性能与可解释性优势，协助大模型、智能体提升
推理能力以及生成质量。

## 简介

Chat2Graph 通过构建图数据库上的多智能体系统，实现智能化的研发、运维、问答、生成等多样化能力，帮助
用户、开发者、产品经理、解决方案架构师、运维工程师等高效使用图数据库，降低用图门槛，加速内容生成，
实现与图对话。同时利用图数据结构的关系建模、可解释性等天然优势，可以对智能体的推理、规划、记忆、工具等
关键能力进行增强，做到图计算技术与人工智能技术的深度融合。

## 关键特性

Chat2Graph 目前提供了基础的智能体系统能力，仍有诸多特性需要和社区一起完善。

- [x] 单主动多被动混合多智能体架构。
- [x] 快&慢思考结合的双LLM推理机。
- [x] 面向智能体链的任务分解与图规划器。
- [x] 分层记忆系统。
- [x] 工具知识图谱。
- [x] 向量与图谱知识库。
- [x] 简洁的智能体SDK。
- [x] Web服务化与交互。
- [x] 智能体一键配置。
- [ ] 结构化智能体角色管理。
- [ ] 工作流自动生成。
- [ ] 算子动作推荐。
- [ ] 工具图谱优化器。
- [ ] 环境管理。
- [ ] 智能体任务编译器。
- [ ] 统一资源管理器。
- [ ] 跟踪与管控能力。
- [ ] 丰富的工具集与MCP集成。
- [ ] Benchmark测试。
- [ ] 开源生态集成。
- [ ] 多模态能力。
- [ ] 产品化增强。


## 快速开始

### 准备环境

准备符合要求的 Python 和 NodeJS 版本。

* Install Python: 推荐 [Python == 3.10](https://www.python.org/downloads)。
* Install NodeJS: 推荐 [NodeJS >= v20](https://nodejs.org/en/download)。

你也可以使用 [conda][conda] 等工具安装Python环境。

### 构建启动

按照如下方式构建 Chat2Graph。

```bash
git clone https://github.com/TuGraph-family/chat2graph.git
cd chat2graph
./bin/build.sh
```

然后基于 [.env.template](../.env.template) 配置环境变量（如 LLM 参数），启动 Chat2Graph。

```bash
cp .env.template .env && vim .env
./bin/start.sh
```

当看到如下日志后，可以在浏览器访问 [http://localhost:5000/](http://localhost:5000/) 使用 Chat2Graph。

```text
Starting server...
Web resources location: /Users/florian/code/chat2graph/app/server/web
System database url: sqlite:////Users/florian/.chat2graph/system/chat2graph.db
Loading AgenticService from app/core/sdk/chat2graph.yml with encoding utf-8
Init application: Chat2Graph
Init the Leader agent
Init the Expert agents

  ____ _           _   ____   ____                 _     
 / ___| |__   __ _| |_|___ \ / ___|_ __ __ _ _ __ | |__  
| |   | '_ \ / _` | __| __) | |  _| '__/ _` | '_ \| '_ \ 
| |___| | | | (_| | |_ / __/| |_| | | | (_| | |_) | | | |
 \____|_| |_|\__,_|\__|_____|\____|_|  \__,_| .__/|_| |_|
                                            |_|          

 * Serving Flask app 'bootstrap'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

```

### 使用SDK

Chat2Graph 的 SDK 提供了非常清晰简洁的 API，让你轻松构建访问你的智能体系统。

通过以下方式，可以快速与内置的Chat2Graph进行对话。

```python
SystemEnv.LLM_NAME="gpt-4o-mini"
SystemEnv.LLM_ENDPOINT="https://api.openai.com/v1"
SystemEnv.LLM_APIKEY="<YOUR-OPENAI-API-KEY>"

mas = AgenticService.load()
question = TextMessage(payload = "What is TuGraph ?")
answer = mas.execute(question).get_payload()
```

同时，SDK也提供了异步对话能力。

```python
job = mas.session().submit(question)
answer = job.wait().get_payload()
```

当然，定制自己的智能体也是允许的。

```python
mas = AgenticService("Chat2Graph")
mas.expert(name="Graph Modeling Expert").workflow(
        (analysis_operator, concept_modeling_operator)
    ).build()
```

为了方便智能体的快速配置，可以使用YAML文件描述智能体细节后，直接加载。

```python
mas = AgenticService.load("app/core/sdk/chat2graph.yml")
```

## 贡献
您可以参考[贡献文档][contrib]，提交 GitHub Issue/PR 提供反馈建议对 Chat2Graph 继续改进。
TuGraph 为社区制定了清晰的[架构][arch]和[角色][roles]，并会邀请优秀贡献者加入[特别兴趣小组][sigs]。

## 联系
您可以通过下面提供的 TuGraph 微信群或 Discord 与我们直接联系。

- 微信：
![](https://github.com/TuGraph-family/community/blob/master/assets/contacts-cn.png)
- Discord：https://discord.gg/KBCFbNFj

[conda]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
[contrib]: https://github.com/TuGraph-family/community/blob/master/docs/CONTRIBUTING-cn.md
[arch]: https://github.com/TuGraph-family/community/blob/master/assets/arch.png
[roles]: https://github.com/TuGraph-family/community/blob/master/docs/ROLES-cn.md
[sigs]: https://github.com/TuGraph-family/community/blob/master/docs/SIGS-cn.md