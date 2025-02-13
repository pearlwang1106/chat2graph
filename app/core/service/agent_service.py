from app.core.agent.leader import Leader
from app.core.common.singleton import Singleton
from app.core.reasoner.dual_model_reasoner import DualModelReasoner
from app.core.sdk.legacy.data_importation import get_data_importation_expert_config
from app.core.sdk.legacy.graph_analysis import get_graph_analysis_expert_config
from app.core.sdk.legacy.graph_modeling import get_graph_modeling_expert_config
from app.core.sdk.legacy.graph_query import get_graph_query_expert_config
from app.core.sdk.legacy.leader_config import get_leader_config
from app.core.sdk.legacy.question_answering import get_graph_question_answeing_expert_config

graph_modeling_expert_config = get_graph_modeling_expert_config()
data_importation_expert_config = get_data_importation_expert_config()
graph_query_expert_config = get_graph_query_expert_config()
graph_analysis_expert_config = get_graph_analysis_expert_config()
graph_question_answering_expert_config = get_graph_question_answeing_expert_config()


class AgentService(metaclass=Singleton):
    """Leader service"""

    def __init__(self):
        # initialize the leader
        self._reasoner = DualModelReasoner()
        self._leaders = [Leader(agent_config=get_leader_config(reasoner=self._reasoner))]

        # configure the multi-agent system
        self.leader.state.create_expert(graph_modeling_expert_config)
        self.leader.state.create_expert(data_importation_expert_config)
        self.leader.state.create_expert(graph_query_expert_config)
        self.leader.state.create_expert(graph_analysis_expert_config)

    @property
    def leader(self) -> Leader:
        """Get the leader. The agent service now manages only one leader."""
        if len(self._leaders) == 0:
            raise ValueError("No leader found.")
        return self._leaders[0]
