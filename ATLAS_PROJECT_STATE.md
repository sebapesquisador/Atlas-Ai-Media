# ATLAS — PROJECT STATE

> Última atualização: 2026-08-21 08:30 (GMT-3)
> Versão: 0.4.0
> Responsável: Sebastiao + MyHub Nitro

---

## 🎯 Estado atual da Narrative Series Factory V1

### Série: **O Milionário Disfarçado**

| Campo | Valor |
|---|---|
| series_id | o-milionario-disfarcado |
| season_id | season-001 |
| episode_id | o-milionario-disfarcado-s01e01 |
| episode_number | 1 |
| production_unit | EPISODE |
| aspect_ratio | 9:16 |
| target_duration | 60-90 segundos |
| status | **SCRIPT_READY** |
| current_stage | AGENTIC_EPISODE_SCRIPT_GENERATION |
| **next_stage** | **AUTONOMOUS_EPISODE_MEDIA_PLANNING** |
| provider | gemini-3.6-flash |
| paid_credits_used | 0 |
| llm_call_performed | true |
| external_call_performed | true |
| paid_provider_used | false |
| public_publication_allowed | **BLOCKED** |
| automatic_publication | **DISABLED** |
| owner_scene_coordination_required | false |

### Artefatos gerados (EP1):

- \outputs/narrative_series/o-milionario-disfarcado/season-001/series_bible.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/season_arc.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/narrative_monetization_policy.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/episode_production_contract.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/episode_screenplay.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/episode_screenplay_qa.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/script_generation_receipt.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/script_generation_manifest.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/provider_cost_gate.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/episode_controller_state.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/episode_factory_manifest.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/agentic_episode_plan.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/cliffhanger_policy_report.json\
- \outputs/narrative_series/o-milionario-disfarcado/season-001/episode-001/narrative_script_generation_preflight.json\

---

## 📂 Estado da organização

### Módulos oficiais em \tlas/narrative_series/\:

- \models.py\ — contratos canônicos
- \monetization.py\ — política freemium
- \provider_gate.py\ — gates de custo
- \script_controller.py\ — controlador de roteiro
- \script_generation.py\ — QA de roteiro
- \storage.py\ — persistência atômica
- \contracts.py\ — builder do contrato EP1
- \controller.py\ — orquestrador principal
- \gentic.py\ — NarrativeDevelopmentAgent
- \llm_execution.py\ — router LLM zero-custo
- \cliffhanger.py\ — política de cliffhangers

### Ponto de entrada oficial:

\\\powershell
python scripts\\run_narrative_series_factory_v1.py
\\\

### Classificação de scripts:

Ver \SCRIPTS_STATUS.md\ para o mapa completo.

- 🟢 **Ativos**: ~100 scripts usados pela fábrica/pipeline v4
- 🟡 **Congelados**: ~150 scripts do piloto cinematográfico (P&D)
- 🔴 **Arquivados**: 11 scripts obsoletos movidos para \rchive/\

---

## 🚦 Próximos passos

1. **AUTONOMOUS_EPISODE_MEDIA_PLANNING** — próximo estágio oficial do EP1
2. Implementar storyboard autônomo do EP1
3. Implementar planejamento de shots
4. Implementar aquisição de assets
5. Implementar renderização cinematográfica
6. Implementar montagem final
7. Implementar upload privado (YouTube)
8. Implementar analytics + performance learning

---

## 🛡️ Governança

- **Nenhum script antigo do piloto é deletado**
- **Toda mudança deve ser registrada no CHANGELOG.md**
- **Toda classificação de script deve ser registrada no SCRIPTS_STATUS.md**
- **Arquivos arquivados devem ter SHA-256 registrado em archive/ARCHIVE_MANIFEST.json**
