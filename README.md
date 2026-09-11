# CodeAlpha - Basic Network Sniffer

## Description du projet

Basic Network Sniffer est un projet de cybersécurité développé en Python
avec la bibliothèque Scapy.

L'objectif de ce projet est de capturer et d'analyser des paquets réseau
en temps réel. Le programme permet d'observer les communications réseau
et d'identifier différents protocoles utilisés.

## Objectifs

Les principaux objectifs du projet sont :

- Capturer les paquets réseau en temps réel.
- Afficher l'adresse IP source.
- Afficher l'adresse IP destination.
- Identifier les principaux protocoles réseau.
- Analyser les paquets ARP.
- Afficher les adresses MAC source et destination.
- Détecter le trafic DNS.
- Afficher les requêtes DNS.
- Afficher une partie limitée du contenu des paquets.
- Afficher la taille des paquets.
- Compter le nombre de paquets capturés.

## Fonctionnalités

### Analyse des paquets IP

Pour les paquets IP, le programme affiche :

- L'adresse IP source
- L'adresse IP destination
- Le protocole utilisé
- La taille du paquet

### Détection des protocoles

Le programme peut identifier plusieurs protocoles :

- TCP
- UDP
- ICMP
- IP
- ARP

### Analyse ARP

Pour les paquets ARP, le programme affiche :

- L'adresse IP source
- L'adresse IP destination
- L'adresse MAC source
- L'adresse MAC destination
- La taille du paquet

### Analyse DNS

Lorsque du trafic DNS est détecté, le programme affiche :

- La présence du DNS
- Le nom de la requête DNS

### Analyse du Payload

Lorsqu'un paquet contient des données supplémentaires, le programme
affiche une quantité limitée d'octets du payload.

Cette fonctionnalité permet d'observer la structure des paquets sans
afficher une quantité excessive de données.

## Technologies utilisées

- Python 3
- Scapy 2.7.0

## Installation

Installer les dépendances nécessaires avec la commande :

```bash
python -m pip install -r requirements.txt