from azure.identity import DefaultAzureCredential
from azure.mgmt.kubernetesconfiguration import SourceControlConfigurationClient
from azure.mgmt.containerservice import ContainerServiceClient

sub_id = "your subscription ID"
client = SourceControlConfigurationClient(credential=DefaultAzureCredential(), subscription_id=sub_id)

def list_kubernetes_clusters_with_tag(resource_group_name, tag_key, tag_value):
    try:
        # Set up Azure credentials
        credentials = DefaultAzureCredential()
        # Container Service Client
        container_client = ContainerServiceClient(credentials,sub_id)

        # Get a list of Kubernetes clusters in the specified resource group
        clusters = container_client.managed_clusters.list_by_resource_group(resource_group_name)

        # Print information about each cluster
        for cluster in clusters:
            cluster_name = cluster.name
            if cluster.tags and tag_key in cluster.tags and cluster.tags[tag_key] == tag_value:
                cluster_location = cluster.location
                container_client.managed_clusters
                print(f"Cluster Name: {cluster_name}, Location: {cluster_location}, was found matching the auto on/off tags")
                
                # Stop the cluster
                print(f"Stopping Cluster: {cluster_name}")
                container_client.managed_clusters.begin_stop(resource_group_name, cluster_name).result()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    resource_group_name = "your resource group"
    tag_key = "[your tag key]"
    tag_value = "true"
    list_kubernetes_clusters_with_tag(resource_group_name, tag_key, tag_value)
