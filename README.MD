# Basic Helm Chart

This repository contains a template for a helm chart, including CI/CD to my repository.

## TL;DR

```sh
$ helm repo add hexf https://charts.repo.hexf.me/
$ helm install hexf/basic-chart
```

## Prerequisites
* Kubernetes 1.12+
* Helm 3.0-beta3+

## Installing the Chart

To install the chart with the release name `my-release`

```sh
$ helm repo add hexf https://charts.repo.hexf.me/
$ helm install --name my-release hexf/basic-chart
```

These command will deploy the chart with the default configuration

## Uninstalling the Chart

To uninstall the `my-release` deployment:

```sh
$ helm delete my-release
```

## Parameters

The following is a list of parameters configurable for this chart, along with their default values and descriptions
| **Parameter**       | **Description**                                     | **Default**                          |
|---------------------|-----------------------------------------------------|--------------------------------------|
| `image.registry`    | Registry to pull image from                         | `docker.io`                          |
| `image.repository`  | Image to pull for chart                             | `hexf/chart`                         |
| `image.tag`         | Tag for image                                       | `{APP_VERSION}`                      |
| `image.pullPolicy`  | Image pull Policy                                   | `IfNotPresent`                       |
| `image.pullSecrets` | Specifies docker-registry secrets names as an array | `[]` (does not pull secrets to pods) |
| `nameOverride`      | String to override the fullname template            | `nil`                                |
| `replicaCount`      | Number of replicas to deploy                        | `1`                                  |
