# Prompt Vocabulary — The Second Receipt

> Extracted from the Cinematic Style Guide. This file is consumed by the Prompt Engineer agent during shard compilation.

## Required Substitutions

| Instead of... | Use... |
|---------------|--------|
| "cinematic" / "epic" | "naturalistic, grounded realism, sober, mathematically rigid composition, 35mm deep focus" |
| "dark" / "moody" | "crushed `#0B101A` charcoal-blue shadows, flat negative space, unfeeling void, zero fill light" |
| "beautiful" / "magical" | "tactile texture, weathered dignity, organic parchment tones, heavy suspended dust motes" |
| "dramatic lighting" | "clinical fluorescent overheads, precise digital uplight, heavy directional window spill" |
| "cold lighting" *(Elias/technology)* | "harsh `#5B8DD9` digital tablet uplight, single source, casting sharp geometric shadows on the face" |
| "cold lighting" *(city/hallways)* | "unflattering `#8FBCAA` fluorescent overheads, clinical cyan tint, sterile `#F0F4F8` institutional bounce, zero diffusion" |
| "warm lighting" *(day)* | "thick `#F0C04A` golden-hour directional window spill, heavy atmospheric volume, light hitting suspended dust motes, illuminating `#7B3F2A` mahogany woodgrain" |
| "warm lighting" *(night/siege)* | "isolated `#D4722A` practical tungsten lamp pool, concentrated pocket of light fighting off dark edges, warm light absorbing into organic parchment surfaces" |
| "vintage" / "retro" / "antique" *(Mara's world)* | "aged contemporary, lived-in, accumulated history, weathered analog decay, generational wear" |
| "cyberpunk" / "sci-fi" / "futuristic" *(Elias's world)* | "sterile corporate modernism, banal bureaucracy, mundane contemporary interfaces, oppressive glass and steel" |

## Banned Words

| Word | Reason | Alternative |
|------|--------|-------------|
| "cinematic" / "epic" | Triggers high-gloss orange/teal grading, anamorphic flares, heroic framing | "naturalistic, grounded realism, sober, 35mm deep focus" |
| "dark" / "moody" | Generates `#000000` pure-black shadows, foggy thriller mist, high-contrast noir rim-lighting | "crushed `#0B101A` charcoal-blue shadows, flat negative space, zero fill light" |
| "beautiful" / "magical" | Introduces fairy-tale blooms, soft-focus halos, glittering particles | "tactile texture, weathered dignity, heavy suspended dust motes" |
| "dramatic lighting" | Produces aggressive chiaroscuro, neon slashes, theatrical spotlights | "clinical fluorescent overheads, precise digital uplight" |
| "vintage" / "retro" / "antique" | Applies sepia filters, period-piece costuming, steampunk elements — breaks present-day setting | "aged contemporary, lived-in, accumulated history, generational wear" |
| "cyberpunk" / "sci-fi" / "futuristic" | Generates neon grids, holographic screens, dystopian tech-wear — the corporate evil must be boring and real | "sterile corporate modernism, banal bureaucracy, mundane contemporary interfaces" |
| "warm" *(unspecified)* | Too vague — must encode source, weight, and scene context | Use thermal encoding substitutions above |
| "cold" *(unspecified)* | Too vague — must encode material and structural light source | Use thermal encoding substitutions above |
