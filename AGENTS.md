# Directives Permanentes d'Ingénierie — Phoenix Robotics

Ce document définit les consignes permanentes à respecter pour tout agent d'IA, développeur ou contributeur intervenant sur le dépôt **Phoenix Robotics**.

---

## 1. Portée et Documents de Référence

Le périmètre d'action de ce projet est régi par les trois documents principaux situés dans le dossier `docs/` :

* **`docs/reference-audit.md`** : Analyse comparative et inventaire complet du site de référence (Robixx Webflow), comprenant les mesures typographiques, les couleurs, la composition et les détails d'inspection.
* **`docs/cahier-des-charges.md`** : Spécifications fonctionnelles, périmètre V1, adaptation à l'identité Phoenix Robotics (Orange, Blanc, Gris clair, gammes uClean, uServe, uLog) et gestion des contenus/assets.
* **`docs/implementation-plan.md`** : Architecture technique (React + TS + Vite + Tailwind + Framer Motion), plan de déploiement par phases et grille de contrôle qualité.

---

## 2. Consignes de Sécurité et de Protection du Projet

1. **Restriction du dépôt :**
   * Travailler exclusivement dans le dépôt `zbm25/Phoenix-robotics` et sur la branche assignée.
   * Ne jamais modifier l'ancien site Webflow, sa configuration Vercel ou son nom de domaine.
   * Ne jamais fusionner ni déployer en production sans accord explicite.
2. **Phase documentaire d'abord :**
   * Attendre systématiquement l'accord explicite de l'utilisateur avant d'initialiser ou de développer du code applicatif.
3. **Respect strict de l'intégrité des données :**
   * Ne jamais transformer aucun témoignage, chiffre, certification ou caractéristique du modèle Robixx en un fait concernant Phoenix Robotics.
   * Ne jamais inventer de données produit.

---

## 3. Normes et Directives Techniques de Développement (Post-accord)

Lorsque la phase de développement applicatif sera autorisée :

1. **Stack Technique Obligatoire :**
   * Emplacement : Racine du dépôt (`./`).
   * Technologies : **React + TypeScript + Vite + Tailwind CSS + Framer Motion**.
2. **Qualité et Rigueur :**
   * Respect des critères d'accessibilité (`prefers-reduced-motion`, navigation au clavier).
   * Formulaires réels et fonctionnels (aucun formulaire factice/simulé).
   * Contrôle strict du build (`npm run build`) et vérification TypeScript (`tsc --noEmit`).
3. **Vérification Visuelle Comparative :**
   * Avant toute soumission, exécuter Playwright pour capturer les rendus desktop (1440px) et mobile (390px) et valider la fidélité par rapport aux captures de référence dans `docs/screenshots/`.
