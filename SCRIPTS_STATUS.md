# ATLAS — SCRIPTS STATUS MAP

> Última atualização: 2026-08-21
> Responsável: Sebastiao + MyHub Nitro
> Política: scripts antigos do piloto ficam congelados (P&D). Só obsoletos são arquivados.

---

## 🟢 ATIVOS — Usados pela Narrative Series Factory V1 ou pipeline oficial

| Script | Função |
|---|---|
| run_narrative_series_factory_v1.py | **PONTO DE ENTRADA OFICIAL** da fábrica |
| run_narrative_episode_script_generation_v1.py | Geração autônoma de roteiro do EP1 |
| run_atlas_v4.py | Pipeline v4 oficial |
| run_atlas_v4_reconciliation.py | Reconciliação do pipeline v4 |
| run_atlas_core.py | Núcleo ATLAS |
| run_pipeline.py | Pipeline genérico |
| run_maintenance.py | Manutenção do projeto |
| list_providers.py | Listagem de providers |
| analyze_youtube_market.py | Análise de mercado YouTube |
| run_youtube_integration.py | Integração YouTube |
| run_script_writer.py | Escrita de roteiro (legado v4) |
| run_storyboard.py / run_storyboard_v3.py | Storyboard |
| run_voice_planning.py / run_voice_tts_pipeline.py | Voz |
| run_narration_director_v1.py | Direção de narração |
| run_thumbnail_finalization_v1.py | Thumbnail |
| run_private_youtube_upload_v1.py | Upload privado |
| run_current_video_analytics_v1.py | Analytics |
| run_performance_learning.py | Aprendizado de performance |
| run_quality_gate_v1.py | Gate de qualidade |
| run_production_validation_v1.py | Validação de produção |
| run_editorial_intelligence.py | Inteligência editorial |
| run_market_intelligence.py | Inteligência de mercado |
| run_topic_discovery.py / run_topic_selection.py | Descoberta/seleção de tópicos |
| run_research_planning.py / run_research_report.py / run_research_evidence.py | Pesquisa |
| run_visual_intelligence.py / run_visual_intelligence_v3.py | Inteligência visual |
| run_evidence_extraction.py / run_evidence_validation.py | Validação de evidências |
| run_knowledge_synthesis.py | Síntese de conhecimento |
| run_opportunity_intelligence.py / run_opportunity_production_decision_v1.py | Oportunidades |
| run_viral_monetization_opportunity_v1.py | Oportunidade viral |
| run_agentic_viral_discovery_v1.py | Descoberta viral agêntica |
| run_autonomous.py / run_autonomous_market.py / run_autonomous_campaign_execution_v1.py | Autonomia |
| run_campaign_* (todos) | Pipeline de campanha |
| run_production_* (todos) | Pipeline de produção |
| run_rendering_pipeline_v3.py / run_video_render.py / run_video_editor_v1.py | Renderização/edição |
| run_voice_* (todos) | Pipeline de voz |
| run_narration_* (todos) | Pipeline de narração |
| run_timeline.py | Timeline |
| run_asset_* (todos) | Aquisição/planejamento de assets |
| run_media_acquisition_v3.py / run_hybrid_media_assembly_v3.py | Mídia |
| run_approved_asset_replacement_v1.py | Substituição de assets |
| run_semantic_asset_recovery_v1.py | Recuperação semântica |
| run_art_director_v1.py | Direção de arte |
| run_camera_direction_planner_v1.py | Planejamento de câmera |
| run_scene_rhythm_planner_v1.py | Ritmo de cena |
| run_narrative_episode_script_generation_v1.py | Roteiro narrativo |
| run_narration_polish.py | Polimento de narração |
| run_learning_eligibility_v1.py | Elegibilidade de aprendizado |
| run_observation_pipeline_v1.py | Pipeline de observação |
| run_public_release_v1.py | Release público |
| run_human_publication_approval_v1.py | Aprovação humana de publicação |
| run_final_master_pipeline_v1.py | Pipeline mestre final |
| run_full_* (todos) | Pipelines full-video |
| run_canonical_* (todos) | Validação canônica |
| run_controlled_* (todos) | Reintrodução controlada |
| run_identity_* (todos) | Identity backend |
| run_local_* (todos) | Engine local |
| run_gemini_* (todos) | Adapter Gemini |
| run_ip_adapter_* (todos) | IP-Adapter Face |
| run_photomaker_* (todos) | PhotoMaker |
| run_pulid_* | PuLID |
| run_stable_diffusion_* | Stable Diffusion |
| run_instantid_* | InstantID |
| run_reference_* (todos) | Referência de imagem/vídeo |
| run_strict_identity_* (todos) | Identity strict |
| run_character_* (todos) | Continuidade de personagem |
| run_v4_campaign_handoff_v1.py | Handoff campanha v4 |
| run_market_test_v4_bridge_v1.py | Bridge mercado v4 |
| run_production_acceleration_pivot_v1.py | Aceleração de produção |
| run_premium_voice_abstraction_v3.py | Abstração de voz premium |
| run_voice_consistency_engine_v1.py / run_voice_mastering_v1.py / run_voice_quality_stabilization_v3.py / run_voice_provider_selection.py | Voz avançada |
| run_locked_* (todos) | Voz/narração travada |
| run_single_segment_voice_proof.py | Prova de voz |
| run_advanced_voice_proof.py | Prova avançada de voz |
| run_automatic_identity_* (todos) | Identidade automática |
| run_commercial_strict_identity_backend_discovery_v1.py | Descoberta strict |
| run_external_provider_connectors_v3.py | Conectores externos |
| run_backfill_market_prediction_manifest.py | Backfill de predição |
| run_cleanup_analysis_packages.py | Limpeza de pacotes |
| run_apply_atlas_chat_handoff_2026_08_19.ps1 | Handoff de chat |
| run_reconcile_runway_cinematic_shot_metadata_v1.py | Reconciliação Runway |
| run_reset_paused_run_for_safety_remediation.py | Reset de segurança |
| run_install_local_engine_r13.ps1 | Instalação engine local |
| run_atlas_root_cleanup_apply_v1.py / run_atlas_root_cleanup_inventory_v1.py | Limpeza raiz |
| run_automatic_identity_orchestration_architecture_v1.py / run_automatic_identity_quality_agent_v1.py | Orquestração automática |

---

## 🟡 CONGELADOS — Piloto cinematográfico (P&D, NÃO mover)

> Política oficial: preservados como tecnologia reutilizável/vertical premium futura.
> ~150 scripts relacionados ao piloto cinematográfico congelado.

### Categorias:

- **Runway I2V** (~30 scripts): run_runway_i2v_*.py
- **Scene003** (~50 scripts): run_scene003_*.py
- **Cinematografia** (~15 scripts): run_cinematic_*.py
- **Identity backend** (~20 scripts): run_identity_*.py
- **Character reference** (~10 scripts): run_character_*.py
- **Local engine** (~15 scripts): run_local_*.py
- **Gemini adapter** (~5 scripts): run_gemini_*.py
- **IP-Adapter/PhotoMaker/PuLID/InstantID** (~15 scripts)
- **Strict identity** (~5 scripts): run_strict_identity_*.py
- **Controlled reintroduction** (~5 scripts): run_controlled_*.py
- **Canonical validation** (~5 scripts): run_canonical_*.py
- **Full video** (~10 scripts): run_full_video_*.py

**Nenhum desses scripts deve ser deletado ou movido sem aprovação explícita.**

---

## 🔴 ARQUIVADOS — Obsoletos (movidos para archive\)

| Script | Motivo | Para onde foi |
|---|---|---|
| run_narration_director_v1.py.backup_before_e402_fix | Backup antigo | archive/deprecated_scripts/ |
| run_private_upload_preparation_v1.py.backup_before_thumbnail_line_fix | Backup antigo | archive/deprecated_scripts/ |
| 39 | Arquivo sem extensão (lixo) | archive/deprecated_root_files/ |
| ATLAS_R17_1_ENGINE_DIAGNOSTIC.txt | Diagnóstico único | archive/deprecated_root_files/ |
| ATLAS_R44_DIAGNOSTICO.txt | Diagnóstico único | archive/deprecated_root_files/ |
| narrative_series_code_dump.txt | Dump já aplicado | archive/deprecated_root_files/ |
| narrative_series_remaining.txt | Dump já aplicado | archive/deprecated_root_files/ |
| ATLAS_NEW_CHAT_START_PROMPT_2026-08-19.txt | Prompt de chat antigo | archive/deprecated_root_files/ |
| fix_encoding.py | Utilitário único | archive/deprecated_root_files/ |
| test_gemini.py | Teste único | archive/deprecated_root_files/ |
| COLETAR_ATLAS_EP01_AUTONOMOUS_MEDIA_PLANNING.ps1 | Coletor único | archive/deprecated_root_files/ |

---

## 📌 Regras de governança

1. **Nenhum script antigo do piloto é deletado** — apenas arquivado se obsoleto.
2. **O ponto de entrada oficial é** \scripts\\run_narrative_series_factory_v1.py\.
3. **Este arquivo (SCRIPTS_STATUS.md) deve ser atualizado** sempre que um script for adicionado, arquivado ou reclassificado.
4. **SHA-256 de todos os arquivos arquivados** deve ser registrado em \rchive/ARCHIVE_MANIFEST.json\ (a ser criado).
