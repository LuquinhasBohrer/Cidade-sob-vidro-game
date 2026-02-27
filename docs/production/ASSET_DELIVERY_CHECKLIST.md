# Cidade Sob Vidro — Checklist de assets para você gerar e me enviar

Este documento transforma o escopo artístico em um checklist operacional para produção.

## Formato de entrega (obrigatório)

- PNG com fundo transparente (sprites/UI/VFX/icons).
- Backgrounds e cutscenes em PNG 1920x1080 (e versão 2x quando aplicável).
- Spritesheet + JSON metadata para animações frame-a-frame.
- Nomenclatura: `categoria/subcategoria/nome_asset_variacao.ext`.
- Entregar zip por lote (ex.: `batch_01_style_and_protagonist.zip`).

## Lotes e quantidades

### 1) Style reference (1)
- 1 imagem mestra de estilo do projeto.

### 2) Personagens principais (sprites + retratos)
- Protagonista (2 variantes: female/male):
  - Overworld 64x64: idle, walk, run, sneak (4 direções).
  - Combate 128x128: combat_idle, attack_basic, skill_cast, take_damage, death.
  - Retratos 256x256: 7 expressões por variante.
- NPCs principais: Sable, Vela Dorn, Kael, Profeta Liss.
- Inimigos: guarda_conselho, fanatico_ordem, seguranca_mercenario, drone_seguranca, mutante_subsolo, chefe_nucleo_corrompido (256x256).

### 3) Cenários com parallax
- Distritos: central (dia/noite), industrial, subsolo, zona alta, mercado noturno.
- 3 a 5 camadas por cenário (`layer_1_far` ... `layer_5_foreground`).
- Interiores: sala_interrogatorio, laboratorio_experimentos, qg_subterraneos, torre_conselho_interior, nucleo_cupula, templo_ordem_vidro.

### 4) UI/HUD
- Barras HP/Energia, moldura minimapa, quest tracker, indicador dia/noite, ícones de facção.
- Main menu background, inventory panel, skill tree BG, dialogue box, combat UI frame.

### 5) Ícones
- Item icons: 80 (armas 20, armaduras 15, consumíveis 25, key items 10, eletrônicos 10).
- Status effects: 6 (Queimadura, Choque, Medo, Confusão, Hackeado, Invisível).

### 6) VFX spritesheets
- blood_splatter_small, blood_splatter_large, blood_pool_forming, electric_discharge,
  fire_burst, hack_interface, critical_hit_flash, poison_gas, death_particles,
  overkill_flash, rain_overlay, neon_flicker.

### 7) Ilustrações de cutscene (10)
- opening_cinematic, first_crack, execution_scene, experiment_revelation,
  dome_core_reveal, kael_transformation, ending_liberation,
  ending_authoritarian, ending_collapse, ending_secret_zoom_out.

### 8) Tilesets
- central_district, industrial, underground, elite_zone, market, interiors_generic.
- Atlas 512x512, tile 32x32 com variações completas.

## Quantidade total alvo

- Aproximadamente **1465 assets** (conforme blueprint).

## Como me enviar para integração rápida

1. Envie em lotes na ordem: style -> protagonista -> backgrounds -> NPCs/enemies -> UI -> icons -> VFX -> cutscenes -> tilesets.
2. Cada lote deve incluir um `manifest.json` com:
   - `asset_id`
   - `arquivo`
   - `tipo` (sprite/background/ui/icon/vfx/cutscene/tileset)
   - `status` (`GENERATED`/`APPROVED`)
3. Se possível, já valide consistência visual dentro do lote antes do envio.

