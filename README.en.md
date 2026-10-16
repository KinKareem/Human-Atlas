# Human Anatomy 3D Atlas

[Bahasa Indonesia](README.md) | **English**

A learning website for human anatomy with interactive 3D models. Users can rotate, zoom, and click structures directly (bones, muscles, nerves, organs, blood vessels, and the lymphatic system), then read the name (Indonesian, Latin, English), description, function, relations (innervation, blood supply, related structures), and clinical correlations.

> **Language note:** the application interface and the anatomical text are currently written in **Indonesian**. Latin and English names are shown alongside where available. This README is a translation of the Indonesian one.
>
> **Important:** the content is written for study purposes and is **not a substitute for medical references**. Please verify it against an anatomy textbook before using it as formal teaching material.

---

## Table of contents

1. [Features](#features)
2. [Data coverage](#data-coverage)
3. [Running and deploying](#running-and-deploying)
4. [Repository structure](#repository-structure)
5. [Technology used](#technology-used)
6. [How the project was developed](#how-the-project-was-developed)
7. [Data format](#data-format)
8. [Adding a new system or structure](#adding-a-new-system-or-structure)
9. [Known limitations](#known-limitations)
10. [Credits](#credits)
11. [License](#license)

---

## Features

- **Interactive 3D space**: rotate (drag), zoom (scroll or pinch), pan (right click), reset, and auto-rotate.
- **Hierarchical sidebar** with Skeleton, Muscles, Nerves, and Organs tabs, grouped by region or system, with search.
- **Click directly on the model** to select a structure, with a name label on hover (desktop).
- **Highlight or Isolate**: other structures are faded or hidden.
- **Side filter** for the right or left side of the body.
- **Skeleton context**: bones appear faintly behind muscles, nerves, and organs so their position is easy to understand.
- **Description panel** as a card that can be opened, closed, and resized; the sidebar can be opened, closed, and resized.
- **Light and dark themes** with a dotted background like a diagram canvas.
- **Per-system loading (lazy loading)**: model data is downloaded only when a system is selected.
- Works on mobile (responsive layout).

## Data coverage

All models come from a single male body (see [Credits](#credits)). Structure counts are per sidebar "item" (right and left sides merged); a mesh is an individual 3D object.

| System | Items | Meshes | Triangles | Notes |
|---|---:|---:|---:|---|
| Skeleton | 159 | 277 | 329 k | Bones and cartilage; ID/Latin/English names; full descriptions |
| Muscles | 211 | 591 | 266 k | Indonesian/Latin names for the main muscles |
| Nerves | 120 | 468 | 152 k | Indonesian/Latin names for the main nerves |
| Respiratory | 48 | 88 | 169 k | Lungs, bronchi down to segmental level, trachea, pharynx, pleura, diaphragm |
| Digestive | 40 | 55 | 199 k | Mouth, salivary glands, GI tract, liver, biliary system, pancreas, omenta |
| Male reproductive | 10 | 20 | 37 k | Testis to penis |
| Urinary | 5 | 8 | 20 k | Kidneys, ureters, bladder, urethra |
| Endocrine | 10 | 13 | 31 k | Hypothalamus, pituitary, pineal, thyroid, parathyroids, adrenals, thymus |
| Heart and great vessels | 49 | 49 | 273 k | Chambers, valves, coronary vessels, pulmonary circulation, aorta, great veins |
| Blood vessels (6 regions) | 368 | 627 | 3.5 M | Arteries and veins by region; about 60 major vessels with names and detailed explanations |
| Lymphatic | 106 | 159 | 111 k | Lymph node groups, spleen, palatine tonsil |

Level of explanation:

- **Detailed** (description, function, innervation, blood supply, related structures, clinical correlations): all bones, all organ systems (respiratory, digestive, male reproductive, urinary, endocrine, heart), and about 60 major vessels.
- **General**: muscles and nerves outside the main structures, the remaining blood vessels, and lymph node groups use a general explanation per type. The page shows a note whenever an explanation is general for a group.

## Running and deploying

The page loads `data/*.json` with `fetch`, so it **cannot be opened through `file://`**. Use any static server.

### Locally

```bash
git clone <your-repo-url>
cd <repo-name>
python3 -m http.server 8000
# open http://localhost:8000
```

### GitHub Pages

1. Push the entire repository contents.
2. Settings, then Pages.
3. Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
4. The site is available at `https://<username>.github.io/<repo>/`.

Total data is about 60 MB; the largest file is about 16 MB, below GitHub's 100 MB per-file limit. Keep in mind that git stores the history of every change to the data files.

## Repository structure

```
.
├── index.html          # The app (HTML, CSS, JS in a single file)
├── LICENSE             # Code license (MIT)
├── README.md           # Indonesian README
├── README.en.md        # English README
├── data/
│   ├── LICENSE             # Full CC BY-SA 4.0 text (data and text)
│   ├── NOTICE.md           # Data origin, changes, and attribution
│   ├── atlas_rangka.json   # skeleton
│   ├── atlas_otot.json     # muscles
│   ├── atlas_saraf.json    # nerves
│   ├── atlas_organ.json    # respiratory
│   ├── atlas_cerna.json    # digestive
│   ├── atlas_repro.json    # male reproductive
│   ├── atlas_urin.json     # urinary
│   ├── atlas_endo.json     # endocrine
│   ├── atlas_jantung.json  # heart and great vessels
│   ├── atlas_vsKa.json     # vessels: head-neck (arteries)
│   ├── atlas_vsKv.json     # vessels: head-neck (veins)
│   ├── atlas_vsTo.json     # vessels: thorax
│   ├── atlas_vsAb.json     # vessels: abdomen and pelvis
│   ├── atlas_vsLe.json     # vessels: arm and hand
│   ├── atlas_vsTu.json     # vessels: leg and foot
│   └── atlas_limfa.json    # lymphatic
└── tools/              # Python scripts that process the models (reference)
```

Data file names follow the layer keys in `index.html` (`atlas_<key>.json`).

## Technology used

**Application (front-end)**

- Plain HTML, CSS, and JavaScript (no framework and no build step), all in a single `index.html`.
- [three.js](https://threejs.org/) r128 for 3D rendering (`MeshStandardMaterial`, `Raycaster`), loaded from the cdnjs CDN.
- `OrbitControls` from the `three@0.128.0` package (jsDelivr CDN) for rotate, zoom, and pan.
- CSS variables for the light and dark themes, `ResizeObserver` to fit the canvas, Pointer Events for panel dragging and model clicking.

**Data processing (tools, offline)**

- Python 3 with `numpy` (and `scipy` available) to read OBJ files, remove duplicates, simplify meshes, and pack binary data.
- Node.js to check script syntax and rebuild the data block of the page.

**Hosting**

- The development version was published as a web page with separate data files.
- The version in this repository uses relative `data/…` paths, so it suits GitHub Pages or any other static server.

**Development**

- The project was developed iteratively together with an AI assistant (Claude, Anthropic): architecture design, code, model-processing scripts, and the anatomy text. See [Credits](#credits) and [Known limitations](#known-limitations) regarding content verification.

## How the project was developed

The order of work, from the beginning to now:

1. **Content design.** Define the outline: cells and tissues, eleven organ systems, regional anatomy, and a uniform data structure for every structure (ID/Latin/English names, category and location, description and function, relations, clinical correlations).
2. **Interface prototype.** A two-part layout: sidebar on the left, 3D space and description panel on the right. The first version used simple procedural 3D shapes (cylinders and spheres) as a placeholder.
3. **Real models.** The Z-Anatomy OBJ file (the whole atlas, about 1.3 GB, 4,878 objects) was processed into data light enough for the web.
4. **Layers added step by step**: skeleton, then muscles and nerves, then organs by system, then blood vessels and the lymphatic system.
5. **Interface improvements**: light and dark theme, dotted background, direct clicking on the model, highlight and isolate, side filter, resizable panels, mobile layout fixes.
6. **Per-system data separation (lazy loading)** to keep the page small and let new systems be added without a single-file size limit.

### Model processing pipeline (`tools/`)

1. **Extraction**: read the OBJ line by line (streaming) and keep the chosen objects, selected by order index and name pattern.
2. **Selection**: choose object ranges for each system. For example, bones from the start indices, organs from the viscera range, vessels from the artery and vein range.
3. **Duplicate removal**: many tubular structures (ureters, urethra, some bronchi and ducts, almost all vessels) are stored as two identical objects in the source. Objects with identical geometry are dropped.
4. **Simplification**: for the skeleton, muscles, nerves, respiratory, and digestive systems, meshes are simplified with *vertex clustering* (merging vertices on a grid) with a per-object triangle target. For the other systems (reproductive, urinary, endocrine, heart, vessels, lymphatic) there is **no reduction in detail**; two vessel meshes that exceeded the 16-bit index limit were split into several parts without losing detail.
5. **Quantization and packing**: vertex positions are quantized to 16 bits inside the layer's bounding box, triangle indices are 16-bit, and everything is base64-encoded and written as JSON.
6. **Grouping and naming**: structures are grouped by side, type, or region; Indonesian and Latin names are written for the main structures.
7. **Writing content**: description, function, innervation, blood supply, related structures, and clinical correlations are written per structure or per group.

### Design decisions

- **A single HTML file with no build step** so it is easy to host and understand.
- **Separate data per system** so the initial page is small (about 350 KB) and a model is downloaded only when needed.
- **Structures lying on the surface of other structures** (liver segments, taeniae coli) are hidden until selected, to avoid flickering from coincident surfaces.
- **Thin membranes** (pleura, mucosa, omenta, mesocolon) are drawn transparent and excluded from clicking on the model so they do not block structures behind them.
- **Vessel regions** are determined from the structure's centroid position (height and distance from the midline), because vessel names carry no region information.

## Data format

Each `data/atlas_<key>.json` contains:

```json
{
  "b": "<base64 binary>",
  "m": {
    "mn": [x, y, z],
    "sc": 1.7,
    "meta": [["Object_name.r", vertexCount, triangleCount, vertexOffset, indexOffset], "..."]
  }
}
```

- The binary holds all vertex positions (3 × quantized `uint16` per vertex) followed by all triangle indices (`uint16`).
- World position is computed as `mn + value / 65535 × sc` on each axis.
- `vertexOffset` and `indexOffset` are counted in `uint16` units within the same binary stream.
- The lists of names, groups, and description text are in `index.html`:
  - `BL[key].g`: sidebar groups and items (`id`, `n` main name, `l` Latin, `e` English, `r` region, `s` side, `p` mesh indices, `d` description key, `g` when the explanation is general).
  - `DET[key]`: text (`desc`, `fn`, `nerve`, `blood`, `rel`, `clin`).
  - `AID`: map of layer keys (hosting-platform version); in this repository the data path is built from `data/atlas_<key>.json`.

## Adding a new system or structure

1. **Extract and pack** objects from the OBJ with the scripts in `tools/` to produce `data/atlas_<key>.json` and the mesh list.
2. **Create item groups** with `id` (base object name), `n`, `l`, `e`, `r`, `s`, `p` (mesh indices), and `d` (text key).
3. **Add text** to `DET` (six fields), or use a general key with `g: 1`.
4. **Register the layer** in `index.html`:
   - add `BL[key]`,
   - add the key to `NAMES`, `TITLE`, `LATIN`, `HELP`, and `EM`,
   - add the key to the `isOrg` function if you want organ coloring,
   - add an option in the organ-system dropdown.
5. **Color**: adjust the `ocol` function if you need specific per-structure colors.

> The scripts in `tools/` are for reference: they use local paths and need the source OBJ file (not included because of its size). Adjust the paths before running them.

## Known limitations

- **Male body model**: female reproductive organs are not present.
- **Structures missing from the source model**, among others the ileum, cecum, rectum, and anal canal as separate objects; the superior vena cava; the interventricular septum; the SA and AV nodes; the pericardium; alveoli and the inner larynx; lymphatic vessels and the thoracic duct.
- **General explanations** for most blood vessels, muscles and nerves outside the main structures, and lymph node groups; English names from the source file are still used in many places.
- **Automatic grouping**: vessel and lymph node regions, and the separation of muscles and nerves from the source file, are determined from name patterns and position. Some structures at region borders may land in a less fitting group.
- **Model quality**: the skeleton, muscles, nerves, respiratory, and digestive systems were simplified; fine detail is reduced compared with the original model.
- **Content verification**: the anatomy text was prepared with AI assistance and has not been reviewed by an anatomy expert or clinician. Check it against references before using it for formal teaching.
- **Performance**: the head-neck arteries layer is about 16 MB and about 1.3 million triangles; it may feel heavy on older devices. Hover labels are turned off automatically on very dense layers.

## Credits

- **[Z-Anatomy](https://github.com/Z-Anatomy)**: source of the 3D models (the whole atlas in Blender/OBJ format), licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Relevant repositories: *Models-of-human-anatomy* and *The-blend*.
- **BodyParts3D**: © The Database Center for Life Science (DBCLS), Japan. The 3D model database on which Z-Anatomy is based. Official download page: <https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html>.
- **[three.js](https://threejs.org/)**: 3D rendering library (MIT license), including `OrbitControls`.
- **Terminologia Anatomica**: the international standard for anatomical terminology, used as the reference for Latin names.
- **Claude (Anthropic)**: the AI assistant that helped with design, coding, data-processing scripts, and writing the anatomy text for this project.

Suggested attribution text to show on the site or in slides:

> 3D models: BodyParts3D © The Database Center for Life Science, via Z-Anatomy (CC BY-SA 4.0), processed and simplified for the web.

## License

**This section is not legal advice.** Please re-check the original license terms before publishing or using the project commercially.

**Summary:** the application code is licensed **MIT**; the 3D model data and the anatomy text are licensed **CC BY-SA 4.0**. License files: [`LICENSE`](LICENSE) (MIT, repository root), [`data/LICENSE`](data/LICENSE) (full CC BY-SA 4.0 text), and [`data/NOTICE.md`](data/NOTICE.md) (data origin, changes, attribution).

| Component | License | Notes |
|---|---|---|
| 3D models (`data/`) | **CC BY-SA 4.0** (derived from Z-Anatomy and BodyParts3D) | Attribution is required and derivative works must be shared under the same license (*share-alike*). The models here have been selected, deduplicated, quantized, and partly simplified, so they count as derivative works. |
| Application code (logic in `index.html`, `tools/`) | **MIT** | The `LICENSE` file at the repository root. Covers the code only, not the model data or the anatomy text. |
| Description and translation text (inside `index.html`) | **CC BY-SA 4.0** | Matches the model data license. The text is embedded in `index.html` together with the code, so that file carries two licenses: code logic MIT, anatomy text CC BY-SA 4.0. |
| three.js | MIT | Loaded from a CDN. |

### Source license terms (Z-Anatomy)

License: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

Statement in the Z-Anatomy README (quoted as written):

> With regard to this content, you are licensed to:
> * freely access part or whole of this database, and acquire data;
> * freely redistribute part or whole of the data from this database;
> * and freely create and distribute database and other derivative works based on part or whole of the data from this database, under the license, as long as you comply with the following conditions:
> * You must attribute this database in the manner specified by the author or licensor when distributing part or whole of this database or any derivative work.
> * You must distribute any derivative work based on part or whole of the data from this database under the same license.

What this means for this project:

- You **may** access, redistribute, and create derivative works from the model data.
- **Attribution is required**, in the manner specified by the licensor, whenever you distribute the data or a derivative work. The quote above does not detail the attribution format, so check the Z-Anatomy README or official page for the requested format. The attribution text in [Credits](#credits) is an initial suggestion.
- **Derivative works must use the same license** (CC BY-SA 4.0). The `data/` folder in this repository is a derivative work, so it must be licensed CC BY-SA 4.0.

Things to keep in mind:

1. **Per-part licenses in the source.** For BodyParts3D, the attribution requested for version 4.0 reads: *"BodyParts3D, © The Database Center for Life Science licensed under CC Attribution 4.0 International"*; older versions use CC BY-SA 2.1 Japan. Z-Anatomy states CC BY-SA 4.0 (see the terms above). However, I came across a report that **some structures carry a non-commercial license** (for example the kidneys and inner ear); I have not verified this myself and it is not mentioned in the README quote above. The kidneys are used in this project's urinary system. Before any commercial use, check the per-model licenses in the Z-Anatomy repository.
2. **Complete the license files.** Make sure `LICENSE` (MIT) has the correct year and copyright holder, and `data/LICENSE` contains the full CC BY-SA 4.0 text copied from the Creative Commons site.
3. **Keep the attribution** on the site (for example in the footer or an info panel) and in the README.

---

*Created for educational purposes. If you find an anatomical or naming error, please open an issue or send a correction.*
