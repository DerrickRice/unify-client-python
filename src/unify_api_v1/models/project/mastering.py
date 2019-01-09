from unify_api_v1.models.project.resource import Project
from unify_api_v1.models.machine_learning_model import MachineLearningModel
from unify_api_v1.models.dataset.resource import Dataset


class MasteringProject(Project):
    """A Mastering project in Unify."""

    def pairs(self):
        """Record pairs generated by Unify's binning model.
        Pairs are displayed on the "Pairs" page in the Unify UI.

        Call :func:`~unify_api_v1.models.dataset.resource.Dataset.refresh` from
        this dataset to regenerate pairs according to the latest binning model.

        :returns: The record pairs represented as a dataset.
        :rtype: :class:`~unify_api_v1.models.dataset.resource.Dataset`
        """
        alias = self.api_path + "/recordPairs"
        return Dataset(self.client, None, alias)

    def pair_matching_model(self):
        """Machine learning model for pair-matching for this Mastering project.
        Learns from verified labels and predicts categorization labels for unlabeled pairs.

        Calling :func:`~unify_api_v1.models.machine_learning_model.MachineLearningModel.predict`
        from this dataset will produce new (unpublished) clusters. These clusters
        are displayed on the "Clusters" page in the Unify UI.

        :returns: The machine learning model for pair-matching.
        :rtype: :class:`~unify_api_v1.models.machine_learning_model.MachineLearningModel`
        """
        alias = self.api_path + "/recordPairsWithPredictions/model"
        return MachineLearningModel(self.client, None, alias)

    def high_impact_pairs(self):
        """High-impact pairs as a dataset. Unify labels pairs as "high-impact" if
        labeling these pairs would help it learn most quickly (i.e. "Active learning").

        High-impact pairs are displayed with a ⚡ lightning bolt icon on the
        "Pairs" page in the Unify UI.

        Call :func:`~unify_api_v1.models.dataset.resource.Dataset.refresh` from
        this dataset to produce new high-impact pairs according to the latest
        pair-matching model.

        :returns: The high-impact pairs represented as a dataset.
        :rtype: :class:`~unify_api_v1.models.dataset.resource.Dataset`
        """
        alias = self.api_path + "/highImpactPairs"
        return Dataset(self.client, None, alias)

    def published_clusters(self):
        """Published record clusters generated by Unify's pair-matching model.

        Call :func:`~unify_api_v1.models.dataset.resource.Dataset.refresh` from
        this dataset to republish clusters according to the latest clustering.

        :returns: The published clusters represented as a dataset.
        :rtype: :class:`~unify_api_v1.models.dataset.resource.Dataset`
        """
        alias = self.api_path + "/publishedClusters"
        return Dataset(self.client, None, alias)