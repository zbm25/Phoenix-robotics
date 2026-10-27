# Audit technique et visuel du site de référence (Robixx)

**URL de référence :** [https://robixx-128.webflow.io/](https://robixx-128.webflow.io/)
**Date d'inspection :** 27 Octobre 2026
**Outil d'inspection :** Playwright (Chromium Headless) & Inspection du DOM/CSS
**Captures de référence :** Stockées sous `docs/screenshots/`

---

## 1. Contexte et preuves d'inspection

### 1.1 Dépôt et environnement de travail
* **Dépôt GitHub :** `zbm25/Phoenix-robotics`
* **Branche active :** `jules-2184949766406421033-dd6de686`
* **Environnement d'exécution :** Sandbox sécurisée Linux avec Node.js v22 et Python 3 + Playwright.

### 1.2 Limites et méthodologie d'inspection
* **Preuves disponibles :** Captures d'écran desktop (1440px) et mobile (390px), captures d'états d'interaction (`docs/screenshots/*`), fichier d'extraction DOM/CSS (`docs/screenshots/inspection-data.json`), et inspection du fichier CSS distitué par Webflow (`robixx-128.webflow.shared.a5ba8e4bc.css`).
* **Absence d'export propriétaire :** Aucun export ZIP ni accès Webflow Designer fourni. L'analyse repose à 100% sur de l'ingénierie inversée publique du rendu web.
* **Distinction explicite :**
  * **Vérifié :** Propriétés CSS computed, structure HTML, typographies téléchargées, hiérarchie de titres, réactivité des boutons.
  * **Hypothèse / Estimation :** Paramètres précis des courbes de bézier (easing) et durées exactes d'animation JS Webflow (Interactions v2), évaluées par observation des propriétés de transition CSS et du comportement au défilement.
  * **Inaccessible :** Code source non minifié Webflow IX2, événements internes JS propriétaires Webflow.

---

## 2. Inventaire des sections de la page d'accueil et des pages secondaires

### 2.1 Page d'accueil (Home)
1. **Header & Navigation :**
   * Bar de navigation fixe avec logo, liens principaux (`Home`, `About Us`, `Solutions`, `Products`, `Industries`, `Pricing`, `Blog`), et bouton CTA `Request a quote`.
2. **Hero Section (Large Photo Section) :**
   * Subheading surtitre : `PRECISION ROBOTICS FOR MODERN AUTOMATION` (Font Geist Mono, rouge/marron `#ac1717`).
   * Titre H1 principal : `Built for intelligent automation` (Font Gowun Batang, 70px, noir `#000000`).
   * Description courte & CTA `Book a Demo` / `Watch video`.
   * Image/Vidéo d'arrière-plan ou illustration principale (bras robotique industriel).
3. **Section "OUR SOLUTIONS" (Grille de solutions) :**
   * Subheading : `OUR SOLUTIONS`
   * Titre H2 : `Automation solutions built to scale with your operations`
   * Grille de 3 cartes de solutions (`Precision Robotic Gripping`, `Integrated Automation Systems`, `Built for Your Unique Workflow`).
4. **Section "PRODUCT OVERVIEW" (Focus produit ARC Grip X1) :**
   * Subheading : `PRODUCT OVERVIEW`
   * Titre H2 : `ARC Grip X1`
   * Métriques et caractéristiques techniques (Payload, Repeatability, Max Grip Force, Weight).
5. **Section "WHY CHOOSE US" (Atouts & Caractéristiques) :**
   * Subheading : `WHY CHOOSE US`
   * Titre H2 : `Built for results. Engineered for performance.`
   * Grille d'atouts (Precision at Scale, Seamless Integration, Continuous Operation).
6. **Section "OUR LOCATIONS WORLDWIDE" (Chiffres & Implantation) :**
   * Subheading : `OUR LOCATIONS WORLDWIDE`
   * Titre H2 : `Powering automation worldwide.`
   * Compteur numérique interactif / animation de chiffres (3, 8, 7, 6, 5...) et carte vectorielle.
7. **Section "WHAT OUR CLIENTS SAY" (Témoignages & Avis) :**
   * Subheading : `WHAT OUR CLIENTS SAY`
   * Citation client et carrousel/cartes d'avis utilisateurs.
8. **Bannière "Achievement Marquee" :**
   * Bandeau de défilement horizontal continu de logos / partenaires.
9. **Section "READY TO AUTOMATE YOUR WORKFLOW?" (CTA Final) :**
   * Bannière avec titre d'appel à l'action et bouton `Request a quote` sur fond visuel sombre/vidéo.
10. **Footer (Pied de page) :**
    * Inscription newsletter (`NEWS, UPDATES & INDUSTRY TRENDS`), navigation complète par catégories, mentions légales, copyright `128.DIGITAL / Webflow`.

### 2.2 Arborescence des pages accessibles du modèle
* `/about-us` (Présentation entreprise & équipe)
* `/solutions` & `/solutions/[slug]` (Catalogue et détail des solutions)
* `/products` & `/products/[slug]` (Produits & fiches fiches produits)
* `/industries` & `/industry/[slug]` (Secteurs d'activité)
* `/pricing` (Offres & Tarifs)
* `/testimonials`, `/our-clients`, `/our-partners` (Preuve sociale)
* `/blog` & `/blog-posts/[slug]` (Articles & Actualités)
* `/contact-us` (Formulaire de contact & prise de rdv)
* `/faq`, `/changelog`, `/licenses`, `/style-guide`, `/instructions` (Pages utilitaires Webflow)

---

## 3. Règles visuelles et Système de Design

### 3.1 Typographie
* **Titres principaux (H1, H2, H3) :** `"Gowun Batang", serif` / `sans-serif`
  * H1 Hero : 70px / Line-height 1.1 / Font-weight 700
  * H2 Section : 50px / Line-height 1.15 / Font-weight 700
* **Surtitres / Subheadings / Badges :** `"Geist Mono", monospace` / `sans-serif`
  * Taille : 14px / Font-weight 500 / Letter-spacing 0.05em / Uppercase
  * Couleur par défaut sur le template : `#ac1717` (Rouge brique / bordeaux)
* **Corps de texte (Body) :** `"Inter", sans-serif`
  * Taille de base : 18px / Line-height 27px (1.5) / Font-weight 400
  * Couleur par défaut : Noir `#000000` ou gris sombre `#1a120d`

### 3.2 Palette de couleurs du template d'origine (Robixx)
* **Couleur d'accentuation / Surtitres :** `#ac1717` (Rouge brique)
* **Fond principal :** Blanc `#ffffff`
* **Fonds secondaires / Cartes :** Gris très clair `#f7f7f7`, `#ececec`
* **Textes sombres :** `#000000`, `#1a120d`, `#333333`
* **Textes secondaires / Muted :** `#6b5f5f`, `#758696`, `#8d8d8d`
* **Bordures & Séparateurs :** `#e7e7e7`, `#dadada`

### 3.3 Composition, Largeurs et Espacements
* **Largeur maximale des conteneurs (`container`) :** ~1280px - 1440px avec padding latéral de 24px à 40px.
* **Espacements verticaux entre sections (`padding-top` / `padding-bottom`) :**
  * Grandes sections : 100px à 120px sur desktop, 60px à 80px sur mobile.
  * Sections moyennes : 60px à 80px.
* **Bordures et Arrondis (`border-radius`) :**
  * Cartes & Boutons : Coins très légers (0px à 4px / 8px max) conférant un aspect industriel et structuré.

---

## 4. Interactions, Animations et Micro-interactions

### 4.1 Inventaire des animations observées
1. **Survol des boutons (Button Hover) :**
   * *Déclencheur :* Cursor hover.
   * *Effet :* Changement de couleur de fond (du sombre au rouge ou de l'orange au noir), légère translation vers le haut (-2px) ou expansion de la bordure.
   * *Durée estimée :* 200ms - 300ms, easing `ease-in-out`.
2. **Effet d'apparition au défilement (Scroll Reveal) :**
   * *Déclencheur :* Intersection Observer / Scroll position.
   * *Effet :* Opacité 0 -> 1, translation Y (fade-in-up +20px à 0px).
   * *Durée estimée :* 600ms, easing `cubic-bezier(0.16, 1, 0.3, 1)`.
3. **Chiffres animés / Compteurs (Locations/Deployments) :**
   * *Déclencheur :* Entrée dans le viewport.
   * *Effet :* Incrémentation rapide des valeurs numériques.
4. **Marquee continu (Logos Partenaires) :**
   * *Déclencheur :* Animation automatique en boucle (CSS `@keyframes` ou JS animation loop).
   * *Effet :* Translation X infinie de 0% à -50%.
5. **Menu Mobile (Responsive Nav) :**
   * *Déclencheur :* Clic sur le bouton Hamburger.
   * *Effet :* Ouverture en déroulé vertical / slide-down du panneau de navigation.

### 4.2 Prise en compte de `prefers-reduced-motion`
* Pour les utilisateurs ayant activé l'option "Réduire les animations" dans leur système d'exploitation :
  * Désactivation des translations au scroll (opacité directe à 1).
  * Arreêt du défilement automatique du marquee.
  * Durée de transition des boutons réduite ou instantanée.

---

## 5. Captures de référence et enregistrements
Toutes les pièces justificatives visuelles sont disponibles dans le dossier `docs/screenshots/` du dépôt :
* `desktop-full.png` (Déroulé complet 1440px)
* `desktop-hero.png` (Premier écran 1440px)
* `desktop-hover.png` (Test de survol)
* `mobile-full.png` (Déroulé complet 390px)
* `mobile-hero.png` (Premier écran mobile 390px)
* `mobile-menu-open.png` (Menu hamburger déplié 390px)
* `inspection-data.json` (Fichier brut d'extraction DOM/CSS)
