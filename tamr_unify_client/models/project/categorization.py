from tamr_unify_client.models.machine_learning_model import MachineLearningModel
from tamr_unify_client.models.project.resource import Project


class CategorizationProject(Project):
    """A Categorization project in Unify."""

    def model(self):
        """Machine learning model for this Categorization project.
        Learns from verified labels and predicts categorization labels for unlabeled records.

        :returns: The machine learning model for categorization.
        :rtype: :class:`~tamr_unify_client.models.machine_learning_model.MachineLearningModel`
        """
        alias = self.api_path + "/categorizations/model"
        return self.client._get_class(MachineLearningModel)(self.client, None, alias)
