# Cidade Sob Vidro — Guia completo de jogar, compilar e exportar

> **Status atual do repositório:** protótipo jogável inicial.
> Ainda **não** contém o jogo final com todos os assets, animações e conteúdos narrativos completos.

## 1) Pré-requisitos

### Linux (Ubuntu 22+)
- Godot 4.2+ (Standard, sem .NET)
- Git 2.40+
- Git LFS
- Python 3.11+

### Windows 10+
- Godot 4.2+ (Standard, sem .NET)
- Git + Git LFS
- Python 3.11+
- Export Templates instalados no Godot
- `rcedit` (recomendado para ícone e metadata do executável)

## 2) Clonar e preparar

```bash
git clone <url-do-repo>
cd Cidade-sob-vidro-game
git lfs install
git lfs pull
```

## 3) Validação de assets antes de rodar/build

### Build de desenvolvimento
```bash
python3 scripts/tools/validate_assets_checklist.py --mode dev
```

### Build de release
```bash
python3 scripts/tools/validate_assets_checklist.py --mode release
```

## 4) Como jogar (rodar localmente)

### Pela interface do Godot
1. Abra o Godot.
2. Clique em **Import**.
3. Selecione `project.godot`.
4. Aguarde a importação.
5. Clique em **Run Project**.

### Controles atuais
- `WASD` movimenta personagem.
- `SHIFT` corre (consome stamina).
- `E` interage e dispara texto contextual.

## 5) Como compilar/exportar

### Exportar para Linux
1. Godot → **Project** → **Export**.
2. Adicione preset **Linux/X11**.
3. Configure saída: `build/linux/CidadeSobVidro.x86_64`.
4. Clique em **Export Project**.
5. Execute:
   ```bash
   chmod +x build/linux/CidadeSobVidro.x86_64
   ./build/linux/CidadeSobVidro.x86_64
   ```

### Exportar para Windows
1. Godot → **Project** → **Export**.
2. Adicione preset **Windows Desktop**.
3. Configure saída: `build/windows/CidadeSobVidro.exe`.
4. Clique em **Export Project**.
5. Execute `CidadeSobVidro.exe`.

## 6) Pipeline sugerido para chegar no jogo completo

1. Implementar autoloads (`GameManager`, `SaveSystem`, `QuestManager`, etc).
2. Fechar sistemas gameplay (combate, inventário, facções, mapa, hacking).
3. Produzir assets por lotes na ordem definida em `docs/project_blueprint.md`.
4. Atualizar `assets_checklist.json` por asset.
5. Só liberar release quando todos estiverem `APPROVED`.
6. Validar com testes e builds automatizados.

## 7) CI de build (GitHub Actions)

Este repositório inclui workflow básico para validar checklist de assets em cada push/PR.

