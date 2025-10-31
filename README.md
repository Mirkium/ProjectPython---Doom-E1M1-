# Recréation de DOOM (1993) – Niveau E1M1 en Python/Pygame

> **Projet étudiant – Python / Pygame**
>
> Objectif : recréer fidèlement le premier niveau de **DOOM (1993)** en utilisant **Python** et **Pygame**, dans le cadre d’un apprentissage du développement de moteur 2.5D et des mécaniques de FPS rétro.

---

## Vision du jeu

Reproduire fidèlement l’expérience du premier niveau de DOOM tout en exploitant des technologies modernes et accessibles.  
Le but est d’allier **apprentissage technique**, **respect de l’œuvre originale** et **création d’un prototype jouable**.

---

## Objectifs du projet

- Recréer le niveau **E1M1** de DOOM (géométrie, ennemis, objets, ambiance).
- Implémenter un **moteur 2.5D** fonctionnel (rendu raycasting ou BSP).
- Reproduire le **gameplay classique** : déplacements rapides, tirs, IA basique.
- Créer une base de code **modulaire** pour d’autres niveaux futurs.

---

## Références et inspiration

- **DOOM (id Software, 1993)**
- **Wolfenstein 3D (1992)**
- Tutoriels raycasting Python : *Lode Vandevenne*, *Permadi*
- Ressources techniques : format **WAD**, **BSP trees**, sprites DOOM.

---

## Gameplay & mécaniques clés

- Déplacements rapides du joueur en vue subjective  
- Tir instantané (*hitscan*) avec munitions limitées  
- IA ennemie basique : détection, poursuite, attaque  
- Objets interactifs : portes, interrupteurs, munitions, soins  
- Objectif final : atteindre la sortie du niveau en survivant  

---

## Direction artistique & sonore

Le projet conserve l’identité visuelle de DOOM :
- Textures pixelisées et teintes sombres  
- Éclairages rouges/orangés pour l’ambiance  
- Sprites et sons **libres de droit**, inspirés de l’original  

---

## Architecture technique (Python / Pygame)

- **Pygame** → gestion fenêtre, entrées clavier/souris, rendu logiciel  
- **JSON** → stockage de la géométrie du niveau  
- **Rendu 2.5D** via BSP ou raycasting amélioré  
- **Classes principales :**
  - `Map`, `Player`, `Renderer`, `SpriteSystem`, `Collision`, `AI`
- **Gestion d’événements** : portes, déclencheurs, scripts simples  

---

## Équipe & répartition des rôles

**Deux développeurs :**
- **Dev A** : moteur (rendu, chargement du niveau, IA, sprites)  
- **Dev B** : gameplay (joueur, collisions, armes, sons, HUD)

Travail collaboratif via **Git** et **branches de fonctionnalités**.

---

## Conceptualisation – Étapes du projet

### Phase 1 : Mécaniques de base
1.1 La map  
1.2 Les déplacements  
1.3 Tirer  

### Phase 2 : Contenu & ambiance
2.1 IA ennemie  
2.2 Les assets (textures, sprites)  
2.3 Les sons  

### Phase 3 : Finalisation
3.1 Les tests et corrections  
3.2 Optimisation et packaging  

---

## Installation

Assurez-vous d’avoir **Python 3.10+** et **Pygame** installés.

```bash
py -3 -m pip install pygame
