# Scientific 2D and 3D figures

[View the annotated gallery](../../docs/visual_gallery.md). F5/F7/F8 are model-generated slices; F1/F2/F3/F4/F6 show observed points only. No fitted surface is implied for unresolved functions.

| Function | 2D | 3D | Type |
|---|---|---|---|
| F1 | [View](f1_2d.svg) | [View](f1_3d.svg) | Observed points only |
| F2 | [View](f2_2d.svg) | [View](f2_3d.svg) | Observed points only |
| F3 | [View](f3_2d.svg) | [View](f3_3d.svg) | Observed points only |
| F4 | [View](f4_2d.svg) | [View](f4_3d.svg) | Observed points only |
| F5 | [View](f5_2d.svg) | [View](f5_3d.svg) | Reconstructed equation slice |
| F6 | [View](f6_2d.svg) | [View](f6_3d.svg) | Observed points only |
| F7 | [View](f7_2d.svg) | [View](f7_3d.svg) | Reconstructed equation slice |
| F8 | [View](f8_2d.svg) | [View](f8_3d.svg) | Reconstructed equation slice |

**Rebuild:** `node results/figures/build_visual_gallery.mjs` from the repository root (Node.js 18+). See the [source generator](../../results/figures/build_visual_gallery.mjs) and [manifest](gallery_manifest.json).

The plots use 278 coordinate-labelled observations because the R11 F7 query input was not retained. The full study still has 279 observed scores. F1 plots use clipped log10(score); F5 model plots use log1p(score). [Provenance](../../docs/evidence_provenance.md).
