# Basic Helm Chart

A Template helm chart - Does not deploy!

## TLDR

```sh
$ helm repo add hexf https://charts.hexf.me/
$ helm install hexf/basic-helm-chart
```

## Prerequisites

* Kuberentes 1.12+
* Helm 3.0-beta3+

## Installing the Chart

To install `Basic Helm Chart` with the release name `my-release`

```sh
$ helm repo add hexf https://charts.hexf.me/
$ helm install --name my-release hexf/basic-helm-chart
```

These command will deploy `Basic Helm Chart` with the default configuration

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```sh
$ helm delete my-release
```

## Parameters

The following is a list of parameters configurable for this chart, along with their description and default values.

**Parameter** | **Description** | **Default**
--- | --- | ---
`replicaCount` |  Number of replicas for this chart | `1`
`image.repository` |  Image Name | `hexf/no-image`
`image.pullPolicy` |  Image Pull Policy | `IfNotPresent`
`image.pullSecrets` |  Image Pull Secrets | `[]`
`nameOverride` |  | `nil`
`fullnameOverride` |  | `nil`
`serviceAccount.create` |  Specifies whether a service account should be created | `True`
`serviceAccount.name` |  The name of the service account to use. If not set and create is true, a name is generated using the fullname template | `nil`
`podSecurityContext` |  | `{}`
`securityContext` |  | `{}`
`service.type` |  | `ClusterIP`
`service.port` |  | `80`
`ingress.enabled` |  | `nil`
`ingress.annotations` | Ingress Annotations | `{}`
`ingress.hosts` |  | `[ordereddict([(&#x27;host&#x27;, &#x27;chart-example.local&#x27;), (&#x27;paths&#x27;, [])])]`
`ingress.tls` |  | `[]`
`resources` |  Resources to allocate to instances | `{}`
`nodeSelector` |  | `{}`
`tolerations` |  | `[]`
`affinity` |  | `{}`