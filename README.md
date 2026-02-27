# Cidade-sob-vidro-game

Protótipo jogável inicial de **Cidade Sob Vidro** em Godot 4.2+.

## Status do projeto

- ✅ Existe um protótipo jogável com movimentação/interação.
- ⚠️ O jogo completo (todos os atos, sistemas, sprites/animações/imagens finais) **ainda não está finalizado** neste repositório.

## O que já está implementado

- Cena principal (`scenes/world/world.tscn`) com mapa base.
- Personagem controlável em 8 direções com corrida e stamina.
- Interação contextual simples (tecla `E`) para fluxo narrativo inicial.
- Sistema inicial de facções e tiers de reputação.
- Estrutura de dados JSON para facções e diálogo de abertura.
- `assets_checklist.json` com política de build e status dos assets de protótipo.
- Validador de checklist em `scripts/tools/validate_assets_checklist.py`.

## Como jogar e compilar (passo a passo completo)

Consulte:

- `docs/PLAY_BUILD_DEPLOY.md`

## Controles atuais

- `WASD`: mover
- `SHIFT`: correr
- `E`: interagir

## Documento completo de escopo do jogo final

A visão completa do projeto está em:

- `docs/project_blueprint.md`


## Planejamento de produção (7 dias)

- `docs/production/DELIVERY_PLAN_7_DAYS.md`
- `docs/production/ASSET_DELIVERY_CHECKLIST.md`

- `docs/production/ASSET_DELIVERY_MASTER.csv`
