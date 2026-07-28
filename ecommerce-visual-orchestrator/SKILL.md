---
name: ecommerce-visual-orchestrator
description: Plan, write, generate, revise, and quality-check coordinated ecommerce main-image sets and continuous long detail-page masters with deterministic publishable slices. Use for Alibaba.com or other international ecommerce visual planning, English selling-point copy, image-generation prompts, product-construction consistency, white-background catalog images, long-image slicing, and final batch acceptance.
---

# Ecommerce Visual Orchestrator

Coordinate ecommerce copy strategy and visual production as one locked workflow.

## Workflow

1. Collect platform, market, product facts, dimensions, materials, features, reference images, image count, language, and output size.
2. Separate verified facts from inferred benefits. Do not invent technical performance or absolute fit claims.
3. Build a product construction lock before writing prompts. Record silhouette, material, print, pockets, waistband, drawstring construction, visible components, positions, proportions, knot state, and forbidden hardware.
4. Plan each image with one primary communication task. Avoid repeating the same selling point or composition.
5. Write concise market-appropriate copy, then write the visual prompt around that copy and the construction lock.
6. Generate draft images with the image-generation skill when requested.
7. Build the detail page as one continuous long-image master, then create publishable slices from that accepted master.
8. Inspect the master at full size, inspect every slice individually, and inspect all slices as a contact sheet. Reject failures before copying them into the final folder.
9. Save final project assets in stable, clearly named folders and report their paths.

## Default 5-image main set

- Main 01: lifestyle hero and primary appeal.
- Main 02: silhouette, drape, or movement.
- Main 03: one important construction or adjustment feature.
- Main 04: mandatory pure-white catalog image, preferably with a full-body model.
- Main 05: specifications, size, or compact proof summary.

For Main 04, first generate a complete full-body model wearing the product against pure `#FFFFFF`. Use no text, badge, icon, props, floor line, border, watermark, or decorative background. If the model version fails acceptance for product accuracy, anatomy, framing, or background purity, use a complete product-only white-background image instead. Preserve the verified product silhouette and proportions.

## Detail-page planning

1. Create and approve one complete long-image master before slicing. Default to `800 × 8000 px` and ten `800 × 800 px` slices when the user provides no other dimensions.
2. Prefer this content flow: product presentation → core benefits → functional details → material and sizing → multi-angle views → use or care guidance.
3. Keep the page visually continuous: use consistent color and natural transitions; avoid obvious dividers and feathering; keep text, people, and critical product details away from slice boundaries.
4. Preserve product consistency across the page: color, pattern, silhouette, material, and the position, length, and proportion of components. Do not invent structures or hardware.
5. Keep products and models fully visible without accidental cropping. Vary model poses and angles. Show material texture without enlarging patterns excessively, and avoid disruptive white-background product images.
6. Keep copy concise and accurate.
7. Cut accepted masters losslessly with `scripts/slice_detail_long_image.py`. Number slices in reading order, verify that they reconstruct the master exactly, and inspect text, composition, product construction, and boundary continuity before delivery.

## Product construction lock

Treat structural details as non-negotiable invariants across every image:

- Distinguish internal from external components.
- State the exact visible component count.
- State the precise emergence/attachment position.
- State proportional length, width, and alignment using stable landmarks.
- State tied/untied state and adjustability.
- List forbidden components such as rings, eyelets, buckles, zippers, or extra cords.
- For multi-panel images, repeat the lock for every panel.

## Copy rules

- Use only supplied or visually supported facts.
- Convert facts to measured benefits without exaggeration.
- Avoid unsupported claims such as cooling technology, guaranteed breathability, wrinkle-free, or fits every body/leg shape.
- Prefer language such as `roomy`, `relaxed`, `wide-leg`, `easy movement`, and `warm-weather styling` when supported.
- Keep image copy short enough to remain legible at the requested output size.

## Prompt rules

For each image specify: role, subject, composition, scene, construction lock, exact text, style, output ratio, invariants, and forbidden artifacts. For revisions, request one targeted change and explicitly preserve everything else.

## Final acceptance

Reject and regenerate when any check fails:

- Correct image count, names, format, and dimensions.
- White-background image uses an accepted complete full-body model when possible, otherwise a complete product-only fallback, and fully complies with the no-decoration rule.
- Silhouette matches the reference at waist, hips, crotch, thigh, hem, and overall width.
- Component count, position, length, alignment, hardware, and knot state match the construction lock.
- Multi-panel and multi-image sets keep the same construction.
- The detail-page master follows the requested dimensions and content flow.
- Reassembling numbered slices reproduces the master pixel-for-pixel with no gap, overlap, scaling, or color shift.
- Text, people, and critical product details remain clear of cut lines, and transitions stay visually natural.
- Text is exact, readable, grammatical, and non-duplicative.
- Each image still communicates its task when the text is hidden (Picture Solo Test).
- The set contains meaningful visual variety without drifting from the product.

Do not overwrite accepted final assets until the replacement candidate passes these checks.
