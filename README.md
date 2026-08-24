# ATLAS AI MEDIA

ATLAS AI MEDIA é uma plataforma agentic de inteligência e produção de
conteúdo digital.

O objetivo é transformar sinais de mercado em conteúdo original, publicável
e mensurável, usando automação, provedores especializados, quality gates e
aprendizagem por dados reais.

## Fonte oficial de verdade

Documentos atuais:

- `ATLAS_NEXT_CHAT_HANDOFF.md` — retomada rápida;
- `ATLAS_PROJECT_STATE.md` — estado oficial;
- `ATLAS_ARCHITECTURE.md` — arquitetura;
- `ATLAS_ROADMAP.md` — prioridades;
- `ATLAS_MAINTENANCE_PLAN.md` — manutenção;
- `ATLAS_DOCUMENTATION_INDEX.md` — precedência documental;
- `CHANGELOG.md` — histórico.

## Ambiente

- Windows 11;
- PowerShell / VS Code;
- Python 3.14;
- `.venv`;
- pacote declarado em `pyproject.toml`: `atlas-ai-media` 0.4.0.

Raiz operacional:

`C:\Users\avell\Downloads\ATLAS_AI_DEV_v0.4.0\Projetos_atlas_ai_media`

## Direção do produto

O ATLAS permanece responsável por:

- inteligência de mercado;
- pesquisa;
- roteiro;
- storyboard;
- prompts/shot specs;
- cost control;
- QA;
- montagem;
- thumbnail;
- publicação;
- analytics;
- learning.

A geração visual passa a ser uma camada substituível.

## Estado atual

A rota local de personagem e os batches cinematográficos não atingiram o
padrão visual exigido e foram retirados do caminho crítico.

```text
LOCAL_CHARACTER_GENERATION = R&D_ONLY
DETERMINISTIC_STORY_ENGINE = NOT_PRODUCTION_APPROVED
PRODUCTION_VISUAL_ENGINE = EXTERNAL_PROVIDER_ROUTE
NIM_PROOF_OF_PRODUCTION = NEXT
```

O próximo passo é testar manualmente no `nim.video` uma sequência curta de
15–25 segundos antes de qualquer integração ou produção completa.

## Publicação

- upload privado: comprovado;
- analytics: comprovado;
- publicação pública: bloqueada por padrão;
- serviço pago: somente com aprovação explícita.

## Manutenção

Em 17/08/2026:

- 86/86 ZIP/PS1/BAT históricos foram arquivados;
- 0 arquivos foram excluídos;
- a raiz foi confirmada com 0 ZIP, 0 PS1 e 0 BAT.

Para trocar de chat, normalmente basta enviar:

`ATLAS_NEXT_CHAT_HANDOFF.md`
---

## 🎬 Narrative Series Factory V1

**Série atual:** O Milionário Disfarçado
**Status do EP1:** SCRIPT_READY → próximo: AUTONOMOUS_EPISODE_MEDIA_PLANNING

### Como executar:

```powershell
# Preparar EP1 (zero custo, local)
python scripts\run_narrative_series_factory_v1.py --prepare-episode-1

# Gerar roteiro do EP1 (preflight + execução)
python scripts\run_narrative_episode_script_generation_v1.py --preflight
python scripts\run_narrative_episode_script_generation_v1.py --execute-free --provider auto
```

### Documentação:

- `SCRIPTS_STATUS.md` — mapa completo de scripts
- `ATLAS_PROJECT_STATE.md` — estado atual do projeto
- `CHANGELOG.md` — histórico de mudanças

### Política de scripts antigos:

- 🟢 **Ativos**: usados pela fábrica/pipeline v4
- 🟡 **Congelados**: piloto cinematográfico (P&D, não mover)
- 🔴 **Arquivados**: obsoletos movidos para `archive/`

