# Cidade Sob Vidro — Project Blueprint

## Visão Geral
- **Título:** Cidade Sob Vidro
- **Subtítulo:** Uma distopia transparente
- **Gênero:** RPG narrativo 2D com combate em turnos
- **Plataformas alvo:** Windows 10+ e Linux (Ubuntu 22+)
- **Classificação indicativa:** PEGI 18 / Adults Only
- **Duração estimada:** 20h campanha principal + 15h conteúdo secundário

## Direção Visual
- Estilo 2D ilustrado em atmosfera cyberpunk distópica com horror corporal.
- Renderização com arte estática e parallax multi-camada (3 a 5 camadas por cenário).
- Paleta fria (azul/ciano/cinza), neon em amarelo/laranja e contraste de sangue em `#C1001F`.
- Sprites detalhados com animações de idle, movimento, combate e morte contextual por dano.

## Stack Técnica
- **Engine:** Godot 4.2+
- **Linguagem:** GDScript
- **Banco:** SQLite via plugin `godot-sqlite`
- **Narrativa:** Dialogic 2 + integração Ink
- **Dados:** JSON (diálogos/quests), INI (config), CSV/PO (localização)
- **VCS:** Git + Git LFS para binários
- **CI/CD:** GitHub Actions (lint, testes, build Windows/Linux)

## Sistemas Centrais
### Exploração e Movimento
- Movimento em 8 direções com colisão por TileMap.
- Estados de velocidade: walk (120), run (220), sneak (60).
- Corrida consome stamina com regeneração passiva.
- NPCs com `NavigationAgent2D`.

### Diálogo e Narrativa
- Diálogos ramificados com impacto de reputação.
- Skill checks com **Influência** e **Técnica** (chance visível).
- Memória de NPC e 7 finais possíveis.

### Combate por Turnos
- Iniciativa por Técnica + rolagem d6.
- Atributos principais: HP, Energia, Influência, Técnica, Defesa, Evasão.
- Efeitos de status: Queimadura, Choque, Medo, Confusão, Hackeado, Invisível.
- Árvore de habilidades com 3 trilhas (12 skills cada), 6 híbridas, nível máximo 30.

## Fações e Reputação
- Conselho da Cúpula, Subterrâneos, Ordem do Vidro e Mercadores Livres.
- Escala de reputação de -100 a +100 com limiares de hostilidade/aliança.
- Reações dinâmicas do mundo baseadas em decisões do jogador.

## Estrutura de Conteúdo
- **Main quests:** 20
- **Side quests:** 45
- **Hidden quests:** 10
- **Distritos principais:** Distrito Central, Bairro Industrial, Subsolo Abandonado, Zona Alta, Mercado Noturno.
- **Eventos dinâmicos:** 1–3 por sessão
- **Ciclo dia/noite:** 20 minutos por ciclo

## História
- Cidade de Silex sob cúpula invisível há 80 anos.
- Protagonista (Kira/Ryn por padrão) é técnico(a) de manutenção que descobre anomalias.
- Atos narrativos:
  1. As Rachaduras
  2. Vozes no Vidro
  3. O Coração da Cúpula
  4. Escolha Final
- 7 finais, incluindo final secreto meta-narrativo (42 fragmentos de lore).

## Conteúdo Maduro e Gore
- Toggle de conteúdo intenso.
- Modo censurado substitui sangue por fluido técnico.
- Especificações para reações de impacto, mortes contextuais e detalhes ambientais.

## Requisitos Técnicos
### Mínimos
- CPU i3-8100 / Ryzen 3 2200G
- RAM 8 GB
- GPU UHD 630 / GTX 950 / RX 460
- 2 GB de armazenamento

### Recomendados
- CPU i5-10400 / Ryzen 5 3600
- RAM 16 GB
- GPU GTX 1060 / RX 580
- SSD, alvo de 60 FPS

## Pipeline de Assets (Mandatório)
- Todos os assets visuais devem ser gerados e aprovados antes de build de release.
- Criar/atualizar `assets_checklist.json` com status `PENDING`, `GENERATED` ou `APPROVED`.
- Total aproximado: **1465 assets**.

## Estrutura de Pastas (planejada)
- `scenes/` (world, ui, combat, dialogue, cutscenes)
- `scripts/` (systems, characters, ui, utils, autoloads)
- `assets/` (sprites, backgrounds, ui, audio, fonts)
- `data/` (dialogues, quests, items, enemies, localization)
- `database/`, `tests/`

## Roadmap
1. **Protótipo (6 semanas):** movimentação, diálogo básico, combate MVP, 1 distrito.
2. **Alpha (12 semanas):** 5 distritos, facções, Ato 1, inventário/save, 50% dos assets.
3. **Beta (10 semanas):** atos completos, 7 finais, áudio dinâmico, 100% dos assets.
4. **Release (4 semanas):** QA, balanceamento, otimização e checklist 100% aprovado.
