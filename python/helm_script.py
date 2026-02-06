import yaml 
import subprocess

with open('/home/devops-cloud-project/helm/my-nginx-chart/values.yaml', 'r') as values:
    file= yaml.safe_load(values)
    
file['replicaCount'] = 3
file['ingress']['enabled'] = True
file['image']['tag'] = 'v1.2.0'
file['grafana']['ingress']['enabled'] = True
file['prometheus']['server']['retention'] = '10d'
file['resources'] = {
     'limits':{
        'cpu': '100m',
        'memory': '128Mi'
      },

    'requests':{
        'cpu': '100m',
        'memory': '128Mi'
    }
}

with open('/home/devops-cloud-project/helm/my-nginx-chart/values.yaml', 'w') as values:
    yaml.dump(file, values, default_flow_style=False)

result= subprocess.run(['helm', 'upgrade', 'my-nginx-chart', '/home/devops-cloud-project/helm/my-nginx-chart', '--install'], capture_output=True, text=True)
print(result.stdout)
print("\nCurrent pods:")
subprocess.run(['kubectl', 'get', 'pods'])
