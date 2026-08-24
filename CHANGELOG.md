# ATLAS AI Media — Changelog

## 2026-08-18 — Runway Gen-4.5 integrado ao Production Orchestrator

- preflight local e live credit check concluídos com sucesso;
- geração API Gen-4.5 concluída com task `SUCCEEDED`;
- output 5 s / 720x1280 validado e QA visual aprovado;
- capacidade `RUNWAY_GEN45_API_PRODUCTION_CAPABILITY = VERIFIED`;
- adicionada bridge fail-closed entre MEDIA e Runway Gen-4.5;
- seleção limitada a shots `lucas`-only enquanto essa é a única âncora canônica
  qualificada para o provider promovido;
- prompt passa a ser derivado da especificação cinematográfica do shot;
- `allow_external` e confirmação humana passam a ser propagados pelo Production
  Orchestrator;
- máximo de uma geração paga por ciclo;
- retry automático e full-batch pago permanecem bloqueados;
- novo gasto é bloqueado enquanto o último shot aguarda QA semântico;
- shots não elegíveis retornam ao provider router em vez de usar Lucas
  incorretamente.

## 2026-08-18 — Runway Gen-4.5 promovido após proof manual

- âncora `lucas_r50` localizada e confirmada pelo SHA-256 canônico em três cópias;
- `canonical_character_visual_style_lock/lucas_r50_canonical_anchor.png` promovida
  como fonte mestre;
- proof manual image-to-video executado no Runway Dev com `gen4.5`;
- duração configurada: 5 s;
- output: 720x1280 / 24 fps / vertical;
- custo de referência: 12 créditos/s, 60 créditos para 5 s;
- áudio ausente por design do proof visual;
- proof aprovado para continuidade da integração;
- vídeo do proof preservado e travado por SHA-256;
- nova camada `runway_gen45_production_provider.py` adicionada;
- provider exige proof aprovado, canonical válido, cost cap, API secret, saldo live
  e confirmação explícita antes de geração paga;
- retry automático permanece bloqueado;
- cadeia histórica `runway_i2v_*`/`gen4_turbo` deixa de ser a rota primária;
- `nim.video` passa de próximo passo obrigatório para fallback/radar;
- próximo marco: preflight Gen-4.5 e bridge com Production Orchestrator.

## 2026-08-17 — Pivot de produção visual

- rota local de geração fotorealista deixou de ser dependência de Production;
- `LOCAL_CHARACTER_GENERATION = R&D_ONLY`;
- lote antigo de 39 keyframes permanece rejeitado;
- SD1.5 + IP-Adapter foi tecnicamente comprovado;
- lote de 10 canonical coverage plates foi gerado com sucesso técnico, mas
  reprovado na revisão humana por identidade, semântica, repetição e qualidade;
- novas tentativas probabilísticas locais foram retiradas do caminho crítico;
- `nim.video` escolhido naquele checkpoint como próximo Proof of Production;
- decisão superada em 18/08 após proof Runway Gen-4.5 aprovado.

## 2026-08-17 — Master determinístico produzido e reprovado

- `ATLAS_PRODUCTION_V1_DETERMINISTIC_STORY_ENGINE` criou master completo;
- duração final: 177.864 s;
- 39/39 shots;
- 35 editorial cards;
- 4 assets dinâmicos preservados;
- 0 chamadas externas;
- 0 créditos pagos;
- revisão humana: qualidade visual abaixo do padrão mínimo;
- Story Engine V1 não foi promovido como formato de produção.

## 2026-08-17 — Scene-003 encerrada

- V5R3 preservado como resultado final da rota de reparo;
- micro-repair loop fechado;
- V5R4/V5R5 proibidos;
- scene-003 não deve bloquear a próxima arquitetura de produção.

## 2026-08-17 — Limpeza operacional da raiz

- 86 arquivos `.zip`, `.ps1` e `.bat` arquivados;
- nenhum arquivo excluído;
- SHA-256 validado após movimentação;
- raiz final confirmou 0 ZIP, 0 PS1 e 0 BAT.

## 2026-08-12 — Consolidação e manutenção concluídas

- documentação oficial consolidada;
- handoff criado;
- caches e resíduos temporários tratados;
- 148 arquivos históricos preservados;
- segredos redundantes tratados com segredo canônico preservado.

## v0.4.0 — Inteligência de Mercado

- motor multicritério de Market Intelligence;
- contratos de fontes;
- ranking auditável;
- decisões `PRODUCE`, `VALIDATE` e `REJECT`;
- deduplicação e risco autoral;
- YouTube Market Source;
- seleção automática de temas.

## Marcos anteriores

- Missão 1: API pública e contratos centrais estabilizados;
- Topic Discovery e Specific Topic Engine;
- pesquisa/editorial;
- thumbnail pipeline;
- YouTube private upload;
- analytics e performance learning.

Os números históricos de versão/incremento não constituem política SemVer
consistente. O `pyproject.toml` continua sendo a fonte para versão do pacote.

## 2026-08-18 - Runway orchestrator gate isolation hotfix V1

- Corrige o dispatch genérico do estágio VALIDATION para não exigir `human_score` quando nenhuma aprovação humana foi fornecida.
- Separa `paid_media_confirmation` de `human_confirmation`, evitando que `--confirm-paid-media` confirme acidentalmente gates humanos de VALIDATION, VOICE, RENDER, THUMBNAIL, ANALYTICS ou PRIVATE_UPLOAD.
- Mantém Runway Gen-4.5 fail-closed e sem retry automático.
- Adiciona CLI diagnóstica segura da bridge Runway, sem rede por padrão.


## 2026-08-18 - Runway shot semantic integrity hotfix V1

- Corrige `ACTION_COVERAGE` para não declarar somente o personagem primário quando
  a ação textual completa da cena contém múltiplos personagens.
- Adiciona gate fail-closed de consistência entre participantes nomeados em
  `visual_action` e `character_ids` antes de qualquer preflight Runway.
- Adiciona reconciliação determinística para atualizar shot list e visual asset
  plan históricos, preservando ids/ordem e atualizando hashes dos manifests.
- Nenhuma rede, geração ou crédito pago é usado pelo hotfix/reconciliação.


<!-- ATLAS_CHANGELOG_2026_08_19_NARRATIVE_PIVOT -->
## 2026-08-19 â€” Narrative Series / Revenue Pivot
- Piloto cinematogrÃ¡fico congelado como P&D.
- `scene-005` preflight pronto, sem geraÃ§Ã£o autorizada.
- `scene-006` Gen-4.5 preservada; QA local PASS; QA externo em hold por Gemini 3.6 503.
- PrÃ³ximo estÃ¡gio: `ATLAS_NARRATIVE_SERIES_FACTORY_V1`.
- Primeira sÃ©rie: `O MilionÃ¡rio DisfarÃ§ado`, temporada variÃ¡vel (~5 episÃ³dios de 60â€“90 s).
- Adicionado Narrative Monetization Engine: freemium/early access, assinatura e passe de temporada.
<!-- /ATLAS_CHANGELOG_2026_08_19_NARRATIVE_PIVOT -->


## [2026-08-21] — Organização e diagnóstico da Narrative Series Factory V1

### Diagnóstico
- Confirmado estado do EP1: **SCRIPT_READY** (Gemini 3.6 Flash, zero custo)
- Próximo estágio oficial: **AUTONOMOUS_EPISODE_MEDIA_PLANNING**
- 14 artefatos canônicos já gerados em `outputs/narrative_series/`

### Organização
- Criado `archive/deprecated_scripts/` e `archive/deprecated_root_files/`
- Movidos 11 arquivos obsoletos para archive:
  - 2 backups antigos de scripts
  - 9 arquivos raiz (diagnósticos únicos, dumps aplicados, lixo)
- Criado `SCRIPTS_STATUS.md` com classificação completa (~250 scripts)
- Atualizado `ATLAS_PROJECT_STATE.md` com estado real da fábrica

### Política
- Scripts do piloto cinematográfico (~150) mantidos congelados (P&D)
- Scripts ativos (~100) preservados em `scripts/`
- Scripts obsoletos (11) arquivados com rastreabilidade

### Próximos passos
- Implementar AUTONOMOUS_EPISODE_MEDIA_PLANNING do EP1
- Criar ARCHIVE_MANIFEST.json com SHA-256 dos arquivos arquivados
