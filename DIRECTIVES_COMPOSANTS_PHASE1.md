# Directives de Spécifications Techniques et Visuelles — Phase 1
**Projet :** Refonte du site vitrine Phoenix Robotics
**Périmètre :** Livrable documentaire de spécification (Header, Hero, RangesSection)
**Date :** Février 2026
**Auteur :** Architecte Front-End Senior

---

## Sommaire
1. [Système de design et constantes Tailwind](#1-système-de-design-et-constantes-tailwind)
   - 1.1 Largeurs de conteneurs et grilles responsive
   - 1.2 Tokens de couleurs, bordures et ombres
   - 1.3 Échelle typographique (Mesures Robixx vs Adaptations Phoenix)
   - 1.4 Origine et gestion des rendus visuels & 3D
   - 1.5 Configuration Motion & gestion de `prefers-reduced-motion`
2. [Spécifications détaillées par composant](#2-spécifications-détaillées-par-composant)
   - 2.1 Composant Header (`src/components/Header.tsx`)
   - 2.2 Composant Hero (`src/components/Hero.tsx`)
   - 2.3 Composant RangesSection (`src/components/RangesSection.tsx`)
3. [Gestion des médias d'attente (Placeholders)](#3-gestion-des-médias-dattente-placeholders)
   - 3.1 Dimensions, ratios et styles des conteneurs
   - 3.2 Spécifications d'intégration des visuels réels à venir
4. [Prompts modulaires de génération pour AI Studio](#4-prompts-modulaires-de-génération-pour-ai-studio)
   - 4.1 Prompt 1 : Header & Méga-menus
   - 4.2 Prompt 2 : Hero Section
   - 4.3 Prompt 3 : RangesSection (4 Gammes)

---

## 1. Système de design et constantes Tailwind

### 1.1 Largeurs de conteneurs et grilles responsive

#### Mesures observées sur la référence Robixx :
- **Largeur maximale centrale :** `1280px` (classe CSS Webflow `w-container` / `container-xl`).
- **Padding latéral (Desktop ≥ 1024px) :** `32px` (`px-8`).
- **Padding latéral (Tablette / Mobile < 1024px) :** `16px` à `24px` (`px-4` à `px-6`).
- **Alignement :** Centré automatiquement (`mx-auto`).

#### Adaptation Phoenix Robotics dans Tailwind CSS (`tailwind.config.js`) :
```javascript
module.exports = {
  theme: {
    extend: {
      maxWidth: {
        'site': '1280px',
      },
      padding: {
        'container-desktop': '2rem',   // 32px
        'container-mobile': '1.25rem', // 20px
      }
    }
  }
}
```

---

### 1.2 Tokens de couleurs, bordures et ombres

#### Distinctions Référence Robixx vs Adaptation Phoenix Robotics :

| Token | Référence Robixx | Adaptation Phoenix Robotics | Code Tailwind / Hex | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Accent principal** | Rouge brique (`#AC1717`) | **Orange Phoenix** | `orange-500` / `#F97316` | Badges, surtitres, accents d'interaction, CTA secondaires |
| **Accent hover** | Rouge foncé (`#8C1212`) | **Orange Phoenix Sombre** | `orange-600` / `#EA580C` | Survol des boutons CTA |
| **Fond principal** | Blanc pur (`#FFFFFF`) | **Blanc pur** | `bg-white` / `#FFFFFF` | Structure de page, cartes principales |
| **Fond technique** | Gris doux (`#F7F7F7`) | **Gris Technique Doux** | `bg-slate-50` / `#F8FAFC` | Fond des conteneurs 3D, badges neutres |
| **Fond carte / Surface**| Gris très clair (`#ECECEC`) | **Gris Surface** | `bg-slate-100` / `#F1F5F9` | Arrière-plan de cartes produit au survol |
| **Texte principal** | Noir carbone (`#000000`) | **Noir Carbone** | `text-slate-900` / `#0F172A` | Titres H1, H2, H3, textes à fort contraste |
| **Texte secondaire** | Gris moyen (`#6B5F5F`) | **Gris Ardoise** | `text-slate-600` / `#475569` | Paragraphes, descriptions, liens nav secondaires |
| **Bordures** | Gris subtil (`#DADADA`) | **Gris Bordure** | `border-slate-200` / `#E2E8F0` | Séparateurs, bordures de cartes (1px solid) |

#### Bordures et Arrondis (Border Radius) :
- **Rayon par défaut cartes / conteneurs :** `rounded-lg` (`8px`) ou `rounded-xl` (`12px`).
- **Rayon des boutons :** `rounded-md` (`6px`) ou `rounded-full` pour les pilules de badges.
- **Épaisseur des bordures :** `border` (`1px solid #E2E8F0`).

#### Ombres architecturales (Shadows) :
- **Ombre de carte au repos :** `shadow-sm` (`0 1px 2px 0 rgba(15, 23, 42, 0.05)`).
- **Ombre de carte au survol / Conteneur 3D :** `shadow-xl` / `shadow-[0_20px_50px_rgba(15,23,42,0.08)]` (Ombre portée douce et diffuse, sans néon ni glassmorphism).

---

### 1.3 Échelle typographique

#### Typographies configurées :
1. **Grands Titres & Noms de Robots :** `"Gowun Batang", serif`
   *Note d'architecture :* C'est la police signature de Robixx. Elle donne l'élégance éditoriale et la distinction industrielle au site.
2. **Surtitres / Badges / Tags techniques :** `"Geist Mono", monospace`
   *Note d'architecture :* Apporte l'aspect technique, précis et robotique.
3. **Corps de texte & Navigation :** `"Inter", sans-serif`
   *Note d'architecture :* Assure une lisibilité optimale et moderne.

#### Matrice typographique (Mesures observées sur Robixx vs Classes Phoenix) :

| Niveau | Police | Taille observée (Robixx) | Interligne | Graisse | Classes Tailwind Phoenix |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Display H1 (Hero)** | `Gowun Batang` | 70px (Desktop) / 40px (Mobile) | 1.1 (77px) | 700 (Bold) | `font-serif text-4xl sm:text-6xl lg:text-[70px] leading-[1.1] font-bold text-slate-900` |
| **Section H2** | `Gowun Batang` | 50px (Desktop) / 32px (Mobile) | 1.15 (57.5px) | 700 (Bold) | `font-serif text-3xl sm:text-4xl lg:text-[50px] leading-[1.15] font-bold text-slate-900` |
| **Card H3 / Gammes** | `Gowun Batang` | 28px (Desktop) / 22px (Mobile) | 1.25 (35px) | 700 (Bold) | `font-serif text-xl lg:text-[28px] leading-[1.25] font-bold text-slate-900` |
| **Surtitre / Badge** | `Geist Mono` | 14px | 1.4 (19.6px) | 500 (Medium) | `font-mono text-xs sm:text-sm tracking-wider uppercase font-medium text-orange-500` |
| **Body (Texte) :** | `Inter` | 18px | 1.5 (27px) | 400 (Regular) | `font-sans text-base lg:text-[18px] leading-[1.5] font-normal text-slate-600` |
| **Navigation Link** | `Inter` | 15px | 1.2 (18px) | 500 (Medium) | `font-sans text-[15px] font-medium text-slate-700 hover:text-slate-900` |

---

### 1.4 Origine et gestion des rendus visuels & 3D

#### Clarification sur le rendu 3D du site de référence Robixx :
- **Constat technique :** Après inspection approfondie du DOM et des requêtes réseau de Robixx (`https://robixx-128.webflow.io/`), le rendu 3D **ne provient pas** d'une scène 3D interactive en temps réel Canvas/WebGL (Three.js), mais **d'images pré-rendues (PNG/WebP HD transparentes ou avec fond Studio)** et de **courtes vidéos boucle WebM/MP4**.
- **Effet de relief :** Le sentiment de profondeur est produit par :
  1. L'éclairage studio professionnel des visuels 3D pré-rendus (lumière rasante, ombres portées douces).
  2. L'encadrement dans des conteneurs HTML épurés (`border border-slate-200 bg-slate-50/50 rounded-xl shadow-xl`).
  3. Des micro-transformations CSS (`transform hover:scale-[1.01] transition-transform duration-500 ease-out`).
- **Consigne de mise en œuvre pour Phoenix Robotics :** Nous utiliserons la même approche : des conteneurs HTML/Tailwind rigides intégrant des visuels/médias pré-rendus de nos 4 gammes de robots, sans surcharger le client avec des chargeurs 3D lourds.

---

### 1.5 Configuration Motion & gestion de `prefers-reduced-motion`

Toutes les animations du site doivent s'appuyer sur **Framer Motion** et respecter la directive d'accessibilité `prefers-reduced-motion`.

#### Configuration globale dans Framer Motion :
```tsx
import { MotionConfig } from 'framer-motion';

export const MotionProvider = ({ children }: { children: React.ReactNode }) => (
  <MotionConfig reducedMotion="user">
    {children}
  </MotionConfig>
);
```

#### Catalogue précis des animations observées et leurs spécifications :

1. **Scroll Reveal (Apparition progressive) :**
   - **Élément concerné :** Surtitres, Titres H1/H2, Paragraphes, Cartes de gammes.
   - **Déclencheur :** Entrée de l'élément dans le viewport (`whileInView`).
   - **Déplacement :** `opacity: 0 -> 1`, `translateY: 24px -> 0px`.
   - **Durée :** `0.6s` (`duration: 0.6`).
   - **Courbe d'accélération (Easing) :** `[0.16, 1, 0.3, 1]` (cubic-bezier fluide style Apple/Webflow).
   - **Comportement au scroll :** Exécuté une seule fois (`viewport: { once: true, margin: "-50px" }`).
   - **Délai échelonné (Stagger) :** Enfant $n$ retardé de `n * 0.1s`.
   - **Variante Mobile :** Réduction du `translateY` à `12px` pour éviter les sauts de mise en page lors du défilement tactile.

2. **Effet Bouton Signature Robixx (Double texte glissant) :**
   - **Élément concerné :** Boutons CTA principaux (`Request a quote`, `Demander une démo`).
   - **Structure DOM requise :** Conteneur `overflow-hidden relative inline-flex`, contenant un groupe interne de deux `span` identiques superposés verticalement.
   - **Déclencheur :** Survol du curseur (`hover`).
   - **Déplacement :** Le texte 1 monte de `0% -> -100%`, le texte 2 monte de `100% -> 0%`.
   - **Durée & Easing :** `0.3s`, `easeOut` ou `cubic-bezier(0.16, 1, 0.3, 1)`.
   - **Légère élévation :** Translation globale du bouton vers le haut (`translateY(-2px)`).
   - **Variante Mobile :** Effet tactile désactivé ou remplacé par une variation de brillance au touch (`active:scale-[0.98]`).

3. **Survol des Cartes de Gammes :**
   - **Élément concerné :** Cartes de la `RangesSection`.
   - **Déclencheur :** Hover.
   - **Déplacement :** Carte `translateY(-4px)`, ombre `shadow-lg` vers `shadow-2xl`. Flèche d'action `translateX(4px)` et passage en couleur Orange `#F97316`.
   - **Durée :** `0.3s ease-out`.

---

## 2. Spécifications détaillées par composant

### 2.1 Composant Header (`src/components/Header.tsx`)

#### 2.1.1 Arborescence DOM exacte
```text
header (header.sticky.top-0.z-50.bg-white/90.backdrop-blur-md.border-b.border-slate-200)
└── div (div.max-w-site.mx-auto.px-container-mobile.lg:px-container-desktop)
    └── div (div.flex.items-center.justify-between.h-20)
        ├── a (a.flex.items-center.gap-2 -> Route `/`)
        │   ├── svg/img (Logo Phoenix Robotics - Pictogramme Orange + Texte Slate-900)
        │   └── span (span.font-serif.font-bold.text-xl.tracking-tight -> "PHOENIX ROBOTICS")
        ├── nav (nav.hidden.lg:flex.items-center.gap-8) [Navigation Desktop]
        │   ├── a (Link -> `/` - "Accueil")
        │   ├── div (div.relative.group) [Méga-menu "Nos Robots"]
        │   │   ├── button (button.flex.items-center.gap-1 -> "Nos Robots" + ChevronIcon)
        │   │   └── div (div.absolute.top-full.left-0.w-[600px].p-6.bg-white.border.border-slate-200.shadow-2xl.rounded-xl.hidden.group-hover:block)
        │   │       └── div.grid.grid-cols-2.gap-4
        │   │           ├── a (/robots/uclean) [Carte mini uClean - Icône + Titre + Description]
        │   │           ├── a (/robots/userve) [Carte mini uServe]
        │   │           ├── a (/robots/ulog) [Carte mini uLog]
        │   │           └── a (/robots/ulab) [Carte mini uLab]
        │   ├── div (div.relative.group) [Méga-menu "Secteurs"]
        │   │   ├── button (button.flex.items-center.gap-1 -> "Secteurs" + ChevronIcon)
        │   │   └── div (div.absolute.top-full.left-0.w-[520px].p-6.bg-white.border.border-slate-200.shadow-2xl.rounded-xl.hidden.group-hover:block)
        │   │       └── div.grid.grid-cols-2.gap-3
        │   │           ├── a (/secteurs/sante) [Santé & Hôpitaux]
        │   │           ├── a (/secteurs/retail) [Retail & Distribution]
        │   │           ├── a (/secteurs/hotellerie) [Hôtellerie & Tertiaire]
        │   │           └── a (/secteurs/industrie) [Industrie & Logistique]
        │   ├── a (Link -> `/a-propos` - "À propos")
        │   └── a (Link -> `/contact` - "Contact")
        ├── div (div.hidden.lg:flex.items-center) [Action CTA Desktop]
        │   └── a (Link -> `/contact` avec effet Double Texte Glissant)
        └── button (button.lg:hidden.p-2 -> Burger Menu Button) [Trigger Mobile]
            └── HamburgerIcon / CloseIcon

└── div (framer-motion AnimatePresence -> Panneau Menu Mobile Slide-Down)
    └── motion.div (w-full.bg-white.border-b.border-slate-200.px-6.py-8.lg:hidden)
        └── nav.flex.flex-col.gap-6
            ├── Accordions / Liens déroulants mobile pour "Nos Robots" et "Secteurs"
            ├── Liens directs "/a-propos", "/contact"
            └── Button CTA "Demander une démo" plein écran
```

#### 2.1.2 Classes Tailwind précises
- **Header conteneur :** `sticky top-0 z-50 w-full bg-white/95 backdrop-blur-md border-b border-slate-200/80 transition-all duration-300`
- **Conteneur intérieur :** `max-w-[1280px] mx-auto px-5 lg:px-8 h-20 flex items-center justify-between`
- **Liens de navigation :** `font-sans text-[15px] font-medium text-slate-700 hover:text-slate-900 transition-colors py-2 flex items-center gap-1.5 cursor-pointer`
- **Méga-menu déroulant container :** `absolute top-full left-1/2 -translate-x-1/2 mt-2 w-[640px] bg-white border border-slate-200 rounded-xl shadow-2xl p-6 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-200 ease-out z-50`
- **Item de Méga-menu :** `flex items-start gap-3.5 p-3 rounded-lg hover:bg-slate-50 transition-colors group/item`
- **Bouton CTA Desktop :** `relative inline-flex items-center justify-center px-5 py-2.5 bg-slate-900 hover:bg-orange-500 text-white font-sans text-sm font-semibold rounded-md overflow-hidden transition-colors duration-300 shadow-sm hover:shadow-md`

#### 2.1.3 Micro-interactions
1. **Effet double texte du bouton CTA Header :**
   - Au survol (`group-hover`), le premier `span` subit `transform -translate-y-full transition-transform duration-300 ease-out`.
   - Le second `span` (positionné en `absolute top-full`) subit `transform -translate-y-full transition-transform duration-300 ease-out`.
2. **Ouverture du Méga-menu :**
   - Déclenchée au survol du groupe (`group-hover`) sur desktop avec un léger fondu et glissement vertical (`opacity-100 translate-y-0`).
3. **Menu Mobile (Tiroir déroulant) :**
   - Déclenché au clic sur l'icône Hamburger.
   - Animation Framer Motion : `initial={{ opacity: 0, height: 0 }}`, `animate={{ opacity: 1, height: "auto" }}`, `exit={{ opacity: 0, height: 0 }}`, `transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}`.

#### 2.1.4 Interface TypeScript & Data
```typescript
export interface NavItem {
  label: string;
  href: string;
  children?: {
    title: string;
    description: string;
    href: string;
    badge?: string;
  }[];
}

export interface HeaderProps {
  currentPath?: string;
}

export const NAV_ITEMS: NavItem[] = [
  { label: 'Accueil', href: '/' },
  {
    label: 'Nos Robots',
    href: '/robots',
    children: [
      { title: 'uClean', description: 'Nettoyage autonome & assainissement sols', href: '/robots/uclean', badge: 'Pro' },
      { title: 'uServe', description: 'Accueil, guidage & service tertiaire', href: '/robots/userve' },
      { title: 'uLog', description: 'Transport logistique intérieur (Deliver 80/150, Lift)', href: '/robots/ulog', badge: 'Industrie' },
      { title: 'uLab', description: 'Robote mobile pour laboratoires & médical', href: '/robots/ulab', badge: 'Santé' },
    ]
  },
  {
    label: 'Secteurs',
    href: '/secteurs',
    children: [
      { title: 'Santé & Hôpitaux', description: 'Hygiène renforcée et logistique médicale', href: '/secteurs/sante' },
      { title: 'Retail & Distribution', description: 'Entretien continu et service client', href: '/secteurs/retail' },
      { title: 'Hôtellerie & Tertiaire', description: 'Accueil premium et nettoyage discret', href: '/secteurs/hotellerie' },
      { title: 'Industrie & Logistique', description: 'Transport autonome de charges lourdes', href: '/secteurs/industrie' },
    ]
  },
  { label: 'À propos', href: '/a-propos' },
  { label: 'Contact', href: '/contact' },
];
```

---

### 2.2 Composant Hero (`src/components/Hero.tsx`)

#### 2.2.1 Arborescence DOM exacte
```text
section (section.relative.bg-white.pt-12.pb-20.lg:pt-20.lg:pb-32.overflow-hidden)
└── div (div.max-w-site.mx-auto.px-container-mobile.lg:px-container-desktop)
    └── div (div.grid.grid-cols-1.lg:grid-cols-12.gap-12.lg:gap-8.items-center)
        ├── div (div.lg:col-span-7.flex.flex-col.items-start) [Colonne Texte Left]
        │   ├── div (motion.div) [Badge Surtitre]
        │   │   └── span (span.inline-flex.items-center.gap-2.px-3.5.py-1.5.rounded-full.bg-slate-50.border.border-slate-200)
        │   │       ├── span (span.w-2.h-2.rounded-full.bg-orange-500.animate-pulse)
        │   │       └── span (span.font-mono.text-xs.sm:text-sm.font-medium.text-orange-500.uppercase) -> "L'AUTOMATISATION INTELLIGENTE DES SERVICES"
        │   ├── h1 (motion.h1.mt-6.font-serif.text-4xl.sm:text-6xl.lg:text-[68px].leading-[1.1].font-bold.text-slate-900)
        │   │   └── "Des robots autonomes conçus pour l'excellence opérationnelle"
        │   ├── p (motion.p.mt-6.font-sans.text-base.lg:text-[18px].leading-relaxed.text-slate-600.max-w-2xl)
        │   │   └── "Phoenix Robotics conçoit et déploie des solutions robotiques mobiles pour le nettoyage, la logistique intérieure, le service et le domaine médical."
        │   └── div (motion.div.mt-8.flex.flex-wrap.items-center.gap-4) [Groupe CTA]
        │       ├── a (a.Link -> `/contact` - Bouton Principal Orange Double Texte Glissant)
        │       └── a (a.Link -> `/robots` - Bouton Secondaire Contour avec Flèche)
        └── div (div.lg:col-span-5.relative) [Colonne Média Right - Conteneur Rendu 3D]
            └── motion.div (motion.div.relative.rounded-2xl.border.border-slate-200.bg-slate-50/50.p-4.shadow-2xl)
                ├── div (div.relative.aspect-[4/3].w-full.overflow-hidden.rounded-xl.bg-slate-100)
                │   └── img/video (Visuel d'attente 3D Studio - Robot Phoenix)
                └── div (div.absolute.-bottom-6.-left-6.bg-white.border.border-slate-200.p-4.rounded-xl.shadow-xl.hidden.sm:flex.items-center.gap-3) [Badge de Réassurance]
                    ├── Icone Check/Shield Orange
                    └── div
                        ├── p.font-mono.text-xs.text-slate-500 -> "DISPONIBILITÉ OPERATIONNELLE"
                        └── p.font-sans.text-sm.font-bold.text-slate-900 -> "99.8% 24/7"
```

#### 2.2.2 Classes Tailwind précises
- **Badge Surtitre :** `inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-50 border border-slate-200 font-mono text-xs sm:text-sm font-semibold tracking-wider text-orange-500 uppercase`
- **Titre H1 :** `font-serif text-4xl sm:text-5xl lg:text-[68px] leading-[1.1] font-bold text-slate-900 tracking-tight`
- **Paragraphe Hero :** `font-sans text-base sm:text-lg lg:text-[18px] leading-[1.6] font-normal text-slate-600 max-w-xl`
- **Conteneur Rendu 3D :** `relative w-full rounded-2xl border border-slate-200 bg-slate-50/80 p-3 sm:p-4 shadow-[0_20px_50px_rgba(15,23,42,0.08)] backdrop-blur-sm group`
- **Cadre Image/Vidéo 3D :** `relative aspect-[4/3] w-full overflow-hidden rounded-xl bg-gradient-to-b from-slate-100 to-slate-200/60 flex items-center justify-center`

#### 2.2.3 Micro-interactions
1. **Entrée séquentielle Motion (Staggered Fade-In) :**
   - Badge Surtitre : `delay: 0.1s`
   - H1 : `delay: 0.2s`
   - Paragraphe : `delay: 0.3s`
   - CTA : `delay: 0.4s`
   - Conteneur 3D Média : `delay: 0.5s`, `initial={{ opacity: 0, scale: 0.95 }}`, `animate={{ opacity: 1, scale: 1 }}`.
2. **Survol du cadre 3D :**
   - Léger redressement : `whileHover={{ y: -4, transition: { duration: 0.3 } }}`.

#### 2.2.4 Interface TypeScript & Data
```typescript
export interface HeroProps {
  title?: string;
  subheading?: string;
  description?: string;
  primaryCtaText?: string;
  primaryCtaHref?: string;
  secondaryCtaText?: string;
  secondaryCtaHref?: string;
  mediaPlaceholderUrl?: string;
}

export const HERO_DATA: HeroProps = {
  subheading: "L'AUTOMATISATION INTELLIGENTE DES SERVICES",
  title: "Des robots autonomes conçus pour l'excellence opérationnelle",
  description: "Phoenix Robotics conçoit et déploie des solutions robotiques mobiles de pointe pour le nettoyage professionnel, la logistique d'intérieur, le service et le secteur médical.",
  primaryCtaText: "Demander une démo",
  primaryCtaHref: "/contact",
  secondaryCtaText: "Découvrir la gamme",
  secondaryCtaHref: "/robots",
};
```

---

### 2.3 Composant RangesSection (`src/components/RangesSection.tsx`)

#### 2.3.1 Arborescence DOM exacte
```text
section (section.py-20.lg:py-32.bg-slate-50/50.border-t.border-b.border-slate-200)
└── div (div.max-w-site.mx-auto.px-container-mobile.lg:px-container-desktop)
    ├── div (motion.div.flex.flex-col.items-center.text-center.max-w-3xl.mx-auto.mb-16) [En-tête de section]
    │   ├── span (span.font-mono.text-xs.sm:text-sm.font-semibold.text-orange-500.uppercase.tracking-wider) -> "NOS GAMMES DE ROBOTS"
    │   ├── h2 (h2.mt-3.font-serif.text-3xl.sm:text-4xl.lg:text-[50px].leading-[1.15].font-bold.text-slate-900) -> "Une réponse robotique sur-mesure pour chaque secteur"
    │   └── p (p.mt-4.font-sans.text-base.lg:text-[18px].text-slate-600) -> "Découvrez nos 4 gammes de robots mobiles autonomes conçues pour transformer vos opérations."
    │
    └── div (div.grid.grid-cols-1.md:grid-cols-2.lg:grid-cols-4.gap-6.lg:gap-8) [Grille des 4 Gammes]
        ├── Card 1 : uClean (Gamme Nettoyage Autonome)
        ├── Card 2 : uServe (Gamme Service & Accueil)
        ├── Card 3 : uLog (Gamme Logistique Intérieure)
        └── Card 4 : uLab (Gamme Robotique Médicale)
```

#### Structure détaillée d'une Carte Gamme (`RangeCard`) :
```text
article (motion.article.group.relative.bg-white.border.border-slate-200.rounded-xl.p-6.flex.flex-col.justify-between.hover:shadow-2xl.hover:border-orange-500/30.transition-all.duration-300)
├── div
│   ├── div (div.relative.aspect-[16/10].w-full.bg-slate-50.rounded-lg.overflow-hidden.mb-6.border.border-slate-100) [Zone Média 3D Frame]
│   │   ├── span (span.absolute.top-3.right-3.px-2.5.py-1.bg-white/90.backdrop-blur-sm.border.border-slate-200.rounded-md.font-mono.text-xs.font-medium.text-slate-700) -> Tag Modèles (ex: "uClean 50")
│   │   └── img (Visuel d'attente 3D Studio)
│   ├── h3 (h3.font-serif.text-2xl.font-bold.text-slate-900.group-hover:text-orange-500.transition-colors) -> "uClean"
│   └── p (p.mt-3.font-sans.text-sm.leading-relaxed.text-slate-600) -> "Nettoyage autonome et assainissement professionnel des sols."
└── div (div.mt-8.pt-4.border-t.border-slate-100.flex.items-center.justify-between)
    └── a (a.font-sans.text-sm.font-semibold.text-slate-900.group-hover:text-orange-500.inline-flex.items-center.gap-2)
        ├── "En savoir plus"
        └── ArrowRightIcon (framer-motion -> transition-transform group-hover:translate-x-1.5)
```

#### 2.3.2 Classes Tailwind précises
- **Grille de la section :** `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8`
- **Carte Gamme (Article) :** `group relative bg-white border border-slate-200 rounded-xl p-6 flex flex-col justify-between hover:shadow-xl hover:-translate-y-1.5 transition-all duration-300 cursor-pointer`
- **Cadre visuel carte :** `relative aspect-[16/10] w-full bg-slate-50 rounded-lg overflow-hidden border border-slate-100 flex items-center justify-center p-4`
- **Titre Carte H3 :** `font-serif text-2xl font-bold text-slate-900 group-hover:text-orange-500 transition-colors`
- **Description Carte :** `mt-2.5 font-sans text-sm leading-relaxed text-slate-600`

#### 2.3.3 Micro-interactions
- **Elevate Hover :** La carte subit `translateY(-6px)` au survol avec renforcement de l'ombre portée (`shadow-[0_20px_40px_rgba(15,23,42,0.08)]`).
- **Flèche de lien :** Glissement horizontal de `0px -> 6px` (`group-hover:translate-x-1.5`) avec passage de la couleur du texte et de l'icône du Slate-900 vers l'Orange Phoenix `#F97316`.

#### 2.3.4 Interface TypeScript & Data Factuelle Phoenix
```typescript
export interface RobotRange {
  id: string;
  name: string;
  badge: string;
  tagline: string;
  description: string;
  models?: string[];
  href: string;
  imagePlaceholderRatio: string;
}

export interface RangesSectionProps {
  title?: string;
  subheading?: string;
  description?: string;
  ranges?: RobotRange[];
}

export const PHOENIX_RANGES_DATA: RobotRange[] = [
  {
    id: 'uclean',
    name: 'uClean',
    badge: 'Nettoyage Pro',
    tagline: 'Laveuses & balayeuses autonomes',
    description: 'Nettoyage autonome et assainissement professionnel des sols pour grandes surfaces, centres commerciaux et hôpitaux.',
    models: ['uClean 50', 'uClean Pro'],
    href: '/robots/uclean',
    imagePlaceholderRatio: '16/10'
  },
  {
    id: 'userve',
    name: 'uServe',
    badge: 'Service & Accueil',
    tagline: 'Téléprésence & guidage',
    description: 'Accueil, guidage des visiteurs, téléprésence et service tertiaire pour l’hôtellerie, les sièges sociaux et la santé.',
    models: ['uServe Bot', 'uServe Touch'],
    href: '/robots/userve',
    imagePlaceholderRatio: '16/10'
  },
  {
    id: 'ulog',
    name: 'uLog',
    badge: 'Logistique Intérieure',
    tagline: 'Transport autonome de charges',
    description: 'Transport logistique intérieur sécurisé de marchandises et composants en milieu industriel et hospitalier.',
    models: ['Deliver 80', 'Deliver 150', 'Lift'],
    href: '/robots/ulog',
    imagePlaceholderRatio: '16/10'
  },
  {
    id: 'ulab',
    name: 'uLab',
    badge: 'Santé & Médical',
    tagline: 'Automatisation mobile de laboratoire',
    description: 'Automatisation robotique mobile sécurisée pour le transport d’échantillons, réactifs et matériel médical sensible.',
    models: ['uLab Mobile'],
    href: '/robots/ulab',
    imagePlaceholderRatio: '16/10'
  }
];
```

---

## 3. Gestion des médias d'attente (Placeholders)

### 3.1 Dimensions, ratios et styles des conteneurs
En attendant la fourniture des visuels HD pré-rendus 3D et des vidéos de démonstration par Phoenix Robotics, tous les médias de la Phase 1 seront représentés par des conteneurs de structure SVG/CSS élégants et neutres.

| Emplacement | Composant | Ratio d'aspect | Dimensions conseillées | Style du conteneur placeholder |
| :--- | :--- | :--- | :--- | :--- |
| **Hero Right Frame** | `Hero.tsx` | `4:3` (1.33:1) | `800x600px` | Fond `bg-gradient-to-b from-slate-100 to-slate-200/60`, cadre `border border-slate-200 rounded-xl`, pictogramme robot vectoriel central avec grille technique en filigrane CSS |
| **Gamme uClean** | `RangesSection.tsx` | `16:10` (1.6:1) | `640x400px` | Fond `bg-slate-50`, silhouette vectorielle robot de nettoyage + Badge Modèle `"uClean 50"` |
| **Gamme uServe** | `RangesSection.tsx` | `16:10` (1.6:1) | `640x400px` | Fond `bg-slate-50`, silhouette vectorielle robot d'accueil + Badge Modèle `"uServe Bot"` |
| **Gamme uLog** | `RangesSection.tsx` | `16:10` (1.6:1) | `640x400px` | Fond `bg-slate-50`, silhouette vectorielle robot plateau/lift + Badge Modèle `"Deliver 150"` |
| **Gamme uLab** | `RangesSection.tsx` | `16:10` (1.6:1) | `640x400px` | Fond `bg-slate-50`, silhouette vectorielle robot laboratoire + Badge Modèle `"uLab Mobile"` |

### 3.2 Spécifications d'intégration des visuels réels à venir
Les composants React doivent accepter une prop `imageUrl?: string`. Si la prop est omise ou invalide, le composant affichera le composant SVG/CSS Placeholder sans rompre la mise en page ni générer d'erreur DOM.

---

## 4. Prompts modulaires de génération pour AI Studio

Les trois prompts ci-dessous sont **autonomes, autoportants et directement exécutables par AI Studio**. Chaque prompt contient l'intégralité du contexte technique nécessaire, les dépendances requises, les classes Tailwind exactes et les règles d'intégrité à respecter.

---

### 4.1 Prompt 1 : Header & Méga-menus (`src/components/Header.tsx`)

```text
TU ES UN DÉVELOPPEUR FRONT-END EXPERT REACT / TYPESCRIPT / TAILWIND CSS.

TA MISSION :
Coder le composant Header complet et ultra-fidèle pour le site Phoenix Robotics dans le fichier `src/components/Header.tsx`.

DÉPENDANCES ET CONTEXTE GLOBAL :
- Stack : React 18/19, TypeScript, Tailwind CSS, Framer Motion, Lucide React (pour les icônes `ChevronDown`, `Menu`, `X`, `ArrowRight`).
- Polices d'écriture importées : `Gowun Batang` (serif), `Geist Mono` (mono), `Inter` (sans).
- Charte de couleurs : Fond blanc `#FFFFFF`, Texte principal `#0F172A` (slate-900), Accent Orange Phoenix `#F97316` (orange-500), Bordures `#E2E8F0` (slate-200).
- Conteneur global : max-width `1280px` (`max-w-[1280px]`), padding horizontal `px-5 lg:px-8`.

CONSIGNES STRICTES DE DÉVELOPPEMENT :
1. Structure Sémantique & Sticky Header :
   - Balise `<header>` fixée en haut avec `sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 h-20`.
   - Logo Phoenix Robotics à gauche : Pictogramme géométrique + Texte "PHOENIX ROBOTICS" en font `Gowun Batang` bold 20px, pointant vers `/`.

2. Navigation Desktop & Méga-menus multi-pages :
   - Lien "Accueil" (`/`).
   - Méga-menu "Nos Robots" (`/robots`) : Au survol desktop (`group-hover`), afficher un volet déroulant (`absolute top-full left-0 w-[600px] p-6 bg-white border border-slate-200 rounded-xl shadow-2xl transition-all duration-200`) avec une grille 2x2 présentant :
     * uClean (`/robots/uclean`) : "Nettoyage autonome & assainissement sols" (Badge "Pro")
     * uServe (`/robots/userve`) : "Accueil, guidage & service tertiaire"
     * uLog (`/robots/ulog`) : "Transport logistique intérieur (Deliver 80/150, Lift)" (Badge "Industrie")
     * uLab (`/robots/ulab`) : "Robotique mobile pour laboratoires & médical" (Badge "Santé")
   - Méga-menu "Secteurs" (`/secteurs`) : Volet déroulant 2x2 présentant :
     * Santé & Hôpitaux (`/secteurs/sante`)
     * Retail & Distribution (`/secteurs/retail`)
     * Hôtellerie & Tertiaire (`/secteurs/hotellerie`)
     * Industrie & Logistique (`/secteurs/industrie`)
   - Lien "À propos" (`/a-propos`).
   - Lien "Contact" (`/contact`).

3. Effet de Bouton Signature Robixx (Double Texte Glissant) :
   - Le bouton CTA à droite "Demander une démo" (`/contact`) doit implémenter l'effet de double texte glissant verticalement :
     * Structure : `<a className="relative inline-flex items-center justify-center px-5 py-2.5 bg-slate-900 hover:bg-orange-500 text-white font-sans text-sm font-semibold rounded-md overflow-hidden transition-colors duration-300 group">`
     * Texte 1 : `<span className="inline-block transition-transform duration-300 ease-out group-hover:-translate-y-full">Demander une démo</span>`
     * Texte 2 : `<span className="absolute inline-block transition-transform duration-300 ease-out translate-y-full group-hover:translate-y-0 text-white">Demander une démo</span>`

4. Menu Mobile Responsive :
   - Bouton Hamburger/Croix sur mobile (`lg:hidden`).
   - Tiroir déroulant mobile animé avec `framer-motion` (`AnimatePresence`) permettant de consulter tous les sous-menus et d'accéder aux pages dédiées.

5. Typage TypeScript :
   - Exporter l'interface `HeaderProps` et implémenter le composant avec typage strict sans aucun `any`.

NE MODIFIE AUCUN FICHIER EN DEHORS DE `src/components/Header.tsx`. NE CRÉE PAS DE CODE APPLICATIF SI TU ES EN PHASE DOCUMENTAIRE.
```

---

### 4.2 Prompt 2 : Hero Section (`src/components/Hero.tsx`)

```text
TU ES UN DÉVELOPPEUR FRONT-END EXPERT REACT / TYPESCRIPT / TAILWIND CSS / FRAMER MOTION.

TA MISSION :
Coder la section Hero principale complète dans le fichier `src/components/Hero.tsx`.

DÉPENDANCES ET CONTEXTE GLOBAL :
- Stack : React, TypeScript, Tailwind CSS, Framer Motion, Lucide React (`ArrowRight`, `ShieldCheck`).
- Polices : `Gowun Batang` (Titres), `Geist Mono` (Surtitres/Badges), `Inter` (Paragraphes et CTA).
- Palette : Fond Blanc `#FFFFFF`, Texte Slate-900 `#0F172A`, Accent Orange `#F97316`, Gris Technique `#F8FAFC`, Bordure `#E2E8F0`.
- Largeur maximale : `1280px` (`max-w-[1280px]`), padding horizontal responsive.

CONSIGNES STRICTES DE DÉVELOPPEMENT :
1. Structure Sémantique & Grid Layout :
   - Section `<section className="relative bg-white pt-12 pb-20 lg:pt-20 lg:pb-32 overflow-hidden">`.
   - Grille responsive : `grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center`.

2. Colonne Gauche (Texte & CTA - 7 colonnes Desktop) :
   - Surtitre / Badge : `<span className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-50 border border-slate-200 font-mono text-xs sm:text-sm font-medium text-orange-500 uppercase tracking-wider">` -> Texte : "L'AUTOMATISATION INTELLIGENTE DES SERVICES"
   - Titre H1 : `<h1 className="mt-6 font-serif text-4xl sm:text-5xl lg:text-[68px] leading-[1.1] font-bold text-slate-900 tracking-tight">` -> Texte : "Des robots autonomes conçus pour l'excellence opérationnelle"
   - Description : `<p className="mt-6 font-sans text-base sm:text-lg lg:text-[18px] leading-relaxed text-slate-600 max-w-xl">` -> Texte factuel Phoenix Robotics.
   - Groupe CTA :
     * CTA Principal : Bouton Orange `#F97316` avec effet de double texte glissant verticalement ("Demander une démo" -> `/contact`).
     * CTA Secondaire : Bouton contour Slate-200 avec icône `ArrowRight` ("Découvrir la gamme" -> `/robots`).

3. Colonne Droite (Cadre Média 3D Frame - 5 colonnes Desktop) :
   - Conteneur Rendu 3D : `<div className="relative w-full rounded-2xl border border-slate-200 bg-slate-50/80 p-3 sm:p-4 shadow-[0_20px_50px_rgba(15,23,42,0.08)]">`.
   - Cadre image ratio 4:3 (`aspect-[4/3]`) avec fond dégradé technique et visuel d'attente SVG/CSS haut de gamme.
   - Badge flottant de réassurance en bas à gauche : "DISPONIBILITÉ OPÉRATIONNELLE : 99.8% 24/7".

4. Animations Framer Motion & Accessibilité :
   - Utiliser `motion.div`, `motion.h1`, `motion.p` avec apparitions échelonnées au scroll (`whileInView={{ opacity: 1, y: 0 }}`, `initial={{ opacity: 0, y: 20 }}`).
   - Respecter `prefers-reduced-motion` en désactivant les offsets verticaux si la préférence utilisateur est activée.

5. Typage TypeScript : Exporter `HeroProps` et utiliser les données factuelles Phoenix sans inventer de faux chiffres.

NE MODIFIE AUCUN FICHIER EN DEHORS DE `src/components/Hero.tsx`.
```

---

### 4.3 Prompt 3 : RangesSection (`src/components/RangesSection.tsx`)

```text
TU ES UN DÉVELOPPEUR FRONT-END EXPERT REACT / TYPESCRIPT / TAILWIND CSS / FRAMER MOTION.

TA MISSION :
Coder la section de présentation des 4 Gammes de Robots Phoenix dans le fichier `src/components/RangesSection.tsx`.

DÉPENDANCES ET CONTEXTE GLOBAL :
- Stack : React, TypeScript, Tailwind CSS, Framer Motion, Lucide React (`ArrowRight`, `Sparkles`).
- Polices : `Gowun Batang` (Titres H2/H3), `Geist Mono` (Badges/Tags), `Inter` (Descriptions et liens).
- Palette : Fond `#F8FAFC/50`, Cartes `#FFFFFF`, Texte `#0F172A`, Accent Orange `#F97316`, Bordures `#E2E8F0`.

CONSIGNES STRICTES DE DÉVELOPPEMENT :
1. Structure de Section & En-tête :
   - Section `<section className="py-20 lg:py-32 bg-slate-50/50 border-t border-b border-slate-200">`.
   - Conteneur `max-w-[1280px] mx-auto px-5 lg:px-8`.
   - En-tête centré : Surtitre Mono "NOS GAMMES DE ROBOTS", Titre H2 Gowun Batang 50px "Une réponse robotique sur-mesure pour chaque secteur", Paragraphe descriptif.

2. Grille Responsive à 4 Colonnes :
   - `<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8">`.

3. Données des 4 Gammes Réelles Phoenix Robotics :
   - Carte 1 - uClean (`/robots/uclean`) : Nettoyage autonome et assainissement professionnel des sols (Modèle : uClean 50).
   - Carte 2 - uServe (`/robots/userve`) : Accueil, guidage, téléprésence et service tertiaire (Modèle : uServe Bot).
   - Carte 3 - uLog (`/robots/ulog`) : Transport logistique intérieur sécurisé (Modèles : Deliver 80, Deliver 150, Lift).
   - Carte 4 - uLab (`/robots/ulab`) : Automatisation robotique mobile pour laboratoires et environnements médicaux (Modèle : uLab Mobile).

4. Design & Micro-interactions des Cartes :
   - Style Carte : `bg-white border border-slate-200 rounded-xl p-6 flex flex-col justify-between hover:shadow-2xl hover:-translate-y-1.5 transition-all duration-300 group cursor-pointer`.
   - Cadre Média : Aspect ratio `16/10` (`aspect-[16/10]`), fond `bg-slate-50 border border-slate-100 rounded-lg` avec visuel d'attente SVG élégant et tag badge du modèle.
   - Lien bas de carte : Text "En savoir plus" + icône `ArrowRight` subissant une translation à droite `group-hover:translate-x-1.5` et un passage en couleur Orange `#F97316`.

5. Animations & Support `prefers-reduced-motion` :
   - Entrée en stagger des 4 cartes au défilement via Framer Motion.
   - Contournement automatique des animations si `prefers-reduced-motion` est détecté.

NE MODIFIE AUCUN FICHIER EN DEHORS DE `src/components/RangesSection.tsx`.
```

---

## Conclusion & Invariant de Phase 1

Le présent document `DIRECTIVES_COMPOSANTS_PHASE1.md` constitue la **référence unique, exhaustive et absolue** pour la fabrication des composants de la Phase 1 du projet Phoenix Robotics.

**Rappel des consignes permanentes (`AGENTS.md`) :**
- Aucun code applicatif ne doit être généré dans `src/` tant que le présent livrable documentaire n'a pas été formellement validé.
- L'intégrité des données factuelles Phoenix Robotics est préservée (4 gammes uClean, uServe, uLog, uLab).
- La fidélité visuelle, typographique (`Gowun Batang`, `Geist Mono`, `Inter`) et dynamique par rapport au modèle de référence Robixx est garantie à 100%.
