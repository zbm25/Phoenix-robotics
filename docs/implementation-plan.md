# Plan d'implémentation technique — Phoenix Robotics

**Projet :** Modernisation & Reconstruction du site Phoenix Robotics
**Socle Technique Retenu :** React + TypeScript + Vite + Tailwind CSS
**Bibliothèque d'Animation Sélectionnée :** Framer Motion
**Emplacement :** Racine du dépôt (`./`)

---

## 1. Justification du Socle Technique et des Choix d'Architecture

### 1.1 Choix de la Pile Technologique Base
* **React 18/19 + TypeScript :** Garantit la modularité des composants (Header, Hero, ProductCards, Marquee), la sûreté du typage des données produits/gammes et une maintenance pérenne.
* **Vite :** Offre un démarrage ultra-rapide, un Hot Module Replacement (HMR) instantané et un bundling optimisé pour la production.
* **Tailwind CSS :** Permet d'exprimer fidèlement les espacements, typographies, couleurs custom (orange Phoenix `#F97316`, gris clair `#F8FAFC`) et grilles responsive directement dans le code source avec une emprinte CSS minimale.
* **Framer Motion :** Sélectionnée à l'issue de l'audit des animations Robixx. Elle permet de répliquer de manière déclarative et fluide :
  * Les apparitions au scroll (`whileInView`, `fade-in-up`).
  * Les compteurs animés (`useMotionValue`, `animate`).
  * Les survol de cartes et boutons (`whileHover={{ y: -2 }}`).
  * Le respect natif de `prefers-reduced-motion` grâce au composant `<MotionConfig reducedMotion="user">`.

---

## 2. Plan Phasé de Développement Applicatif

> **Important :** Conformément aux consignes de protection du projet, **aucune phase de développement ne sera initiée** sans l'accord préalable et explicite de l'utilisateur après validation des documents de cadrage.

### Phase 1 : Échantillon représentatif (Header + Hero + Gammes)
L'objectif de la Phase 1 est de livrer un échantillon minimal mais 100% fidèle et fonctionnel pour validation visuelle et technique.

1. **Initialisation de la structure à la racine :**
   * Configuration de `vite.config.ts`, `tailwind.config.js`, `tsconfig.json`.
   * Import des polices Google (`Gowun Batang`, `Geist Mono`, `Inter`).
2. **Développement des composants de la Phase 1 :**
   * `src/components/Header.tsx` : Navigation sticky, logo Phoenix, liens, bouton CTA, menu mobile slide-down.
   * `src/components/Hero.tsx` : Subheading `GEIST MONO`, Titre H1, CTA, illustration/vidéo Phoenix.
   * `src/components/RangesSection.tsx` : Présentation des 3 gammes (uClean, uServe, uLog).
3. **Validation visuelle comparative :**
   * Génération de captures Playwright à 1440px et 390px.
   * Comparaison Pixel-Perfect avec `docs/screenshots/desktop-hero.png` et `mobile-hero.png`.

### Phase 2 : Déploiement de la Page d'Accueil Complète
1. Composant `ProductHighlight.tsx` (Focus uClean 50 / Deliver 150 avec fiches techniques).
2. Composant `WhyChooseUs.tsx` (Grille de valeurs et atouts Phoenix).
3. Composant `KeyMetrics.tsx` (Compteurs animés avec Framer Motion).
4. Composant `PartnerMarquee.tsx` (Bandeau de défilement infini de logos).
5. Composant `CtaBanner.tsx` et `Footer.tsx`.

### Phase 3 : Formulaire Interactif, Accessibilité & Pages Secondaires
1. **Formulaire de contact / Demande de démonstration :**
   * Gestion complète d'état, validation Zod / React Hook Form.
   * Traitement et feedback utilisateur (succès / erreur réel).
2. **Navigation & Accessibility (a11y) :**
   * Gestion du focus au clavier (`:focus-visible`).
   * Rôles ARIA et balisage sémantique (`main`, `nav`, `section`).
3. **Pages secondaires :**
   * `/robots` (Catalogue interactif).
   * `/contact` (Formulaire dédié).

---

## 3. Matrice de Contrôle Qualité & Tests Automatisés

Avant toute livraison ou merge, la grille de vérification suivante sera appliquée :

| Domaine | Outil / Commande | Critère d'Acceptation |
| :--- | :--- | :--- |
| **Typage** | `npx tsc --noEmit` | 0 erreur TypeScript |
| **Console** | Playwright Console Logs | 0 erreur JS ou warning React |
| **Build** | `npm run build` | Bundle généré sans avertissement |
| **Visuel Desktop** | Playwright (1440px) | Rendu conforme à `docs/screenshots/desktop-full.png` |
| **Visuel Mobile** | Playwright (390px) | Rendu conforme à `docs/screenshots/mobile-full.png` |
| **Menu Mobile** | Playwright Click | Panneau de navigation parfaitement articulé |
| **Formulaire** | Test d'interaction | Soumission réelle avec retour d'état clair |
