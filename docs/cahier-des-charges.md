# Cahier des charges — Phoenix Robotics

**Projet :** Refonte du site vitrine Phoenix Robotics
**Modèle de référence :** [Robixx (Webflow)](https://robixx-128.webflow.io/)
**Nom de travail commercial :** Phoenix Robotics
**Statut :** Version 1.0 (Phase d'Analyse et Cahier des charges)

---

## 1. Périmètre du projet V1

### 1.1 Objectifs
Reprendre fidèlement le design, la disposition, le rythme visuel et les animations du modèle de référence Robixx, adaptés au positionnement et aux gammes réelles de Phoenix Robotics.

### 1.2 Périmètre initial (Phase 1 d'échantillonnage)
Avant de déployer l'intégralité du site, la première phase de développement applicatif sera limitée à :
1. **Header & Navigation supérieure** (avec menu responsive mobile).
2. **Hero Section (Premier écran)** avec appel à l'action.
3. **Une section représentative** (La section de présentation des gammes de robots Phoenix).

### 1.3 Périmètre V1 complet (Page d'accueil & pages secondaires)
* **Page d'accueil (`/`) :**
  * Header & Navigation
  * Hero Section
  * Présentation des 3 Gammes (uClean, uServe, uLog)
  * Focus Produit Phare (ex: uClean 50 ou Deliver 150)
  * Pourquoi choisir Phoenix Robotics (Avantages opérationnels)
  * Chiffres clés & Déploiements (Compteurs animés)
  * Témoignages clients & Partenaires (Marquee logos)
  * Bannière CTA "Prêt à automatiser vos opérations ?"
  * Footer
* **Pages secondaires V1 :**
  * Gammes & Fiches Robots (`/nos-robots`, `/robots/uclean`, `/robots/userve`, `/robots/ulog`)
  * Secteurs d'activité / Applications (`/secteurs`)
  * À propos de Phoenix Robotics (`/a-propos`)
  * Contact & Demande de démo (`/contact`)

---

## 2. Adaptation à Phoenix Robotics & Charte Graphique

### 2.1 Identité visuelle
* **Nom officiel :** Phoenix Robotics.
* **Typographies :**
  * Titres principaux : Modèle sobre, épuré et moderne (style `Gowun Batang` ou `Geist / Inter` à fort poids visuel), non futuriste.
  * Surtitres / Badges : Monospace moderne (`Geist Mono`).
  * Corps de texte : `Inter` (sans-serif, lisibilité optimale).
* **Palette de couleurs :**
  * **Couleur Principale / Accent :** Orange Phoenix (`#F97316` / `#E65100`). *(Remplace le rouge brique `#ac1717` du template Robixx)*.
  * **Fond principal :** Blanc pur (`#FFFFFF`).
  * **Fonds secondaires / Cartes :** Gris clair très doux (`#F8FAFC`, `#F1F5F9`).
  * **Textes & Éléments sombres :** Noir carbone / Gris très foncé (`#0F172A`, `#1E293B`).
  * **Bordures & Séparateurs :** Gris subtil (`#E2E8F0`).

### 2.2 Correspondance (Mapping) des sections Robixx -> Phoenix Robotics

| Section Robixx | Thématique Robixx (Template) | Équivalent Phoenix Robotics (V1) |
| :--- | :--- | :--- |
| **Hero Section** | *Built for intelligent automation* (Grippers industriels) | **L'automatisation intelligente des services et du bâtiment** |
| **OUR SOLUTIONS** | Precision Robotic Gripping, Integrated Systems | **NOS GAMMES DE ROBOTS** : uClean, uServe, uLog |
| **PRODUCT OVERVIEW** | ARC Grip X1 (Pince industrielle) | **ZOOM PRODUIT** : Robot uClean 50 (Autonomie & Nettoyage Haute Performance) |
| **WHY CHOOSE US** | Precision at scale, continuous operation | **POURQUOI PHOENIX ROBOTICS** : Fiabilité 24/7, Intégration facile, ROI rapide |
| **OUR LOCATIONS** | 387+ Deployments worldwide | **PHOENIX EN CHIFFRES** : +200 robots déployés, 99.8% de disponibilité |
| **WHAT OUR CLIENTS SAY** | Témoignages industriels | **TÉMOIGNAGES CLIENTS** (Secteurs hôtellerie, santé, logistique) |
| **READY TO AUTOMATE** | Request a quote | **DEMANDEZ UNE DÉMONSTRATION EN CONDITIONS RÉELLES** |

---

## 3. Règle stricte d'intégrité des données & Liste des Assets à fournir

### 3.1 Protection contre les données fictives
* **Aucun témoignage fictif**, aucun faux chiffre de certification ni fausse caractéristique produit ne doit être présenté comme un fait réel.
* Les textes génériques du template seront remplacés uniquement par du contenu validé par Phoenix Robotics.

### 3.2 Liste des assets à fournir par Phoenix Robotics
Pour finaliser le site sans placeholder, Phoenix Robotics devra fournir :
1. **Logos & Médias de marque :**
   * Logo Phoenix Robotics au format SVG (versions fond clair, fond sombre, pictogramme).
   * Favicon SVG / PNG.
2. **Visuels & Vidéos :**
   * Photos HD sur fond neutre et en situation réelle pour :
     * Gamme **uClean** (robots autonomes de nettoyage professionnel).
     * Gamme **uServe** (robots d'accueil et de service).
     * Gamme **uLog** (robots de transport logistique : Deliver 80, Deliver 150, Lift).
   * Vidéos de démonstration courtes (10-15s, loop mp4/webm) pour la Hero section.
3. **Fiches Techniques Produit :**
   * Dimensions, poids, autonomie, vitesse, capacité de charge (payload pour Deliver 80/150/Lift), temps de charge, type de navigation (LiDAR, VSLAM).
4. **Textes & Contenus rédactionnels :**
   * Textes de présentation de l'entreprise, propositions de valeur, cas d'usage par secteur.
   * Formulaires : adresses email de destination pour les demandes de démo et de devis.

---

## 4. Interactions et Critères de Qualité

### 4.1 Comportement des interactions
* **Formulaire de contact / Demande de démo :** Doit être pleinement fonctionnel (validation des champs, traitement de soumission, message de confirmation, gestion des erreurs). Un formulaire simulé ne sera jamais considéré comme opérationnel.
* **Navigation responsive :** Menu fluide sur mobile (390px) avec fermeture au clic extérieur ou ESC.
* **Accessibilité :**
  * Support de `prefers-reduced-motion` pour désactiver les effets de défilement pour les personnes sensibles.
  * Navigation au clavier complète avec états `:focus-visible` distincts.
  * Contrastes de couleurs conformes WCAG AA.

### 4.2 Critères de validation visuelle (Tests comparatifs)
* Réalisation de captures comparatives entre la référence Webflow et le site Phoenix aux dimensions de contrôle :
  * **Desktop :** 1440px
  * **Mobile :** 390px
* Vérification de l'absence d'erreurs dans la console navigateur (`console.error`).
* Validation stricte du build TypeScript (`tsc --noEmit`) et de la compilation production.
