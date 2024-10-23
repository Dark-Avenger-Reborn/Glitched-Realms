import subprocess
import json

class manager:
    def __init__(self):
        pass  # Initialize any necessary variables here if needed

    def run_kubectl(self, command):
        """Run a kubectl command."""
        try:
            result = subprocess.run(
                ["kubectl"] + command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error: {e.stderr}")

    def create_namespace(self, uuid):
        """Create a namespace for the user."""
        print(f"Creating namespace user-{uuid}...")
        return self.run_kubectl(["create", "namespace", f"user-{uuid}"])

    def list_pods(self, uuid):
        """List all pods in the user's namespace."""
        print(f"Listing pods in namespace user-{uuid}...")
        return self.run_kubectl(["get", "pods", "--namespace", f"user-{uuid}"])

    def create_pod(self, uuid, pod_name):
        """Create a pod in the user's namespace."""
        print(f"Creating pod {pod_name} in namespace user-{uuid}...")
        return self.run_kubectl([
            "run", pod_name, "--restart=Never", "--namespace", f"user-{uuid}"
        ])

    def delete_pod(self, uuid, pod_name):
        """Delete a pod in the user's namespace."""
        print(f"Deleting pod {pod_name} from namespace user-{uuid}...")
        return self.run_kubectl([
            "delete", "pod", pod_name, "--namespace", f"user-{uuid}"
        ])

    def get_pod_status(self, uuid, pod_name):
        """Get the status of a pod."""
        print(f"Getting status of pod {pod_name} in namespace user-{uuid}...")
        output = self.run_kubectl([
            "get", "pod", pod_name, "--namespace", f"user-{uuid}", "-o", "json"
        ])
        pod_info = json.loads(output)
        return pod_info["status"]["phase"]

    def connect_to_pod(self, uuid, pod_name):
        """Connect to a pod's shell in the user's namespace."""
        status = self.get_pod_status(uuid, pod_name)
        if status in ["Running"]:
            print(f"Connecting to pod {pod_name} in namespace user-{uuid}...")
            subprocess.call([
                "kubectl", "exec", "-it", pod_name, "--namespace", f"user-{uuid}", "--", "bash"
            ])
        else:
            print(f"Cannot connect to pod {pod_name}, current status: {status}")

    def delete_namespace(self, uuid):
        """Delete a user's namespace and all its resources."""
        print(f"Deleting namespace user-{uuid}...")
        return self.run_kubectl(["delete", "namespace", f"user-{uuid}"])
