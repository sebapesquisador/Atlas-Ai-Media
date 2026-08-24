# ATLAS AI MEDIA — Handoff para o Próximo Chat

**Atualizado:** 18/08/2026

## Papel de trabalho

- Usuário: dono do projeto, não operador técnico.
- Assistente: conduz arquitetura, engenharia, programação e sequência.
- Orientação: passo a passo, caminhos e comandos exatos.
- Evitar operação manual asset por asset.
- Serviço pago somente com gate e autorização explícita.
- Publicação pública continua bloqueada por padrão.

## Projeto

Raiz:

`C:\Users\avell\Downloads\ATLAS_AI_DEV_v0.4.0\Projetos_atlas_ai_media`

Run comercial:

`market-test-faith-human-001`

## Estado visual consolidado

A geração local de personagem permanece fora do caminho crítico:

`LOCAL_CHARACTER_GENERATION = R&D_ONLY`

O Story Engine determinístico V1 foi reprovado visualmente:

`DETERMINISTIC_STORY_ENGINE = NOT_PRODUCTION_APPROVED`

A scene-003 está encerrada:

`SCENE003_MICRO_REPAIR_LOOP = CLOSED`

## Lucas canônico

Fonte oficial:

`outputs\pipeline_v4\media\market-test-faith-human-001\canonical_character_visual_style_lock\lucas_r50_canonical_anchor.png`

SHA-256:

`5B441FDE450392F6CEB352359A1B293E9D78574F701F490E7172348E08AC8924`

O hash foi confirmado em três cópias idênticas em 18/08/2026. Usar o caminho
acima como fonte mestre.

## Runway Gen-4.5 — proof aprovado

Foi realizado no Runway Dev um image-to-video manual usando Lucas canônico.

Configuração:

- `gen4.5`;
- 5 segundos;
- `720x1280`;
- vertical;
- 12 créditos/s;
- 60 créditos estimados;
- sem áudio por design.

Proof preservado:

`outputs\pipeline_v4\media\market-test-faith-human-001\runway_gen45_manual_visual_proof\lucas_r50_gen45_manual_visual_proof_5s.mp4`

SHA-256:

`448B89DEAC51969CD0840FE012948A4FA068FE695F89429464D07255CD025DAC`

Decisão:

`RUNWAY_GEN45_MANUAL_VISUAL_PROOF = APPROVED`

Não gerar um segundo proof só para refinar o primeiro.

## Provider Gen-4.5 adicionado

Novo módulo:

`atlas\production\runway_gen45_production_provider.py`

Novo script:

`scripts\run_runway_gen45_production_provider_v1.py`

Política:

- proof manual e canonical são gates obrigatórios;
- custo default máximo = 60 créditos;
- saldo API live precisa ser consultado antes de paid execution;
- `--confirm-paid` é obrigatório para qualquer geração;
- retry automático = bloqueado;
- receipt torna a execução retomável quando já existe task id;
- áudio segue em pipeline separado.

## Cadeia Runway antiga

Os módulos anteriores `runway_i2v_*` usam majoritariamente `gen4_turbo` e devem
ser tratados como histórico/P&D, não como rota primária vigente.

Não apagar ainda.

## NIM

`nim.video` deixa de ser o próximo passo obrigatório. Mantê-lo apenas como
fallback/radar de provider.

## Próximo passo único

`RUNWAY_GEN45_PROVIDER_PREFLIGHT_VALIDATION`

1. aplicar o incremento Gen-4.5;
2. rodar Ruff e testes focados;
3. executar preflight local sem `--execute` e sem gasto;
4. confirmar que o provider reconhece proof/canonical/custo;
5. depois coletar o ponto real do Production Orchestrator para criar a bridge.

Não executar nova geração paga durante a validação desse incremento.

## Estado de retomada

```text
RESUME_POINT = RUNWAY_GEN45_PROVIDER_PREFLIGHT_VALIDATION
RUNWAY_GEN45_MANUAL_VISUAL_PROOF = APPROVED
RUNWAY_GEN45_PRODUCTION_PROVIDER_FOUNDATION = IMPLEMENTED
RUNWAY_GEN45_PAID_EXECUTION = FAIL_CLOSED
PRODUCTION_ORCHESTRATOR_RUNWAY_BRIDGE = NOT_YET_INTEGRATED
NIM_VIDEO = FALLBACK_RADAR
LOCAL_CHARACTER_GENERATION = R&D_ONLY
SCENE003_MICRO_REPAIR_LOOP = CLOSED
PUBLICATION_PUBLIC = BLOCKED_BY_DEFAULT
```

## Atualização — Runway Gen-4.5 integrado ao Production Orchestrator

A execução API Gen-4.5 foi concluída com sucesso e o vídeo resultante passou no
QA visual. A capacidade do provider deixa de ser apenas proof manual e passa a
ser `VERIFIED` para integração controlada.

Bridge V1 adicionada ao estágio `MEDIA`:

- somente próximo shot Lucas-only é elegível;
- nenhuma chamada externa sem `--allow-external`;
- live credit check pode ocorrer sem geração;
- gasto exige confirmação humana explícita;
- máximo de uma geração paga por ciclo;
- nenhuma segunda geração é permitida enquanto houver asset com QA pendente;
- multi-personagem retorna ao provider router;
- áudio continua desacoplado.

Novo ponto de retomada:

```text
RESUME_POINT = RUNWAY_GEN45_ORCHESTRATOR_BRIDGE_LOCAL_VALIDATION
RUNWAY_GEN45_API_PRODUCTION_CAPABILITY = VERIFIED
PRODUCTION_ORCHESTRATOR_RUNWAY_BRIDGE = IMPLEMENTED_V1
RUNWAY_GEN45_FULL_BATCH_PAID_EXECUTION = BLOCKED
RUNWAY_GEN45_AUTOMATIC_RETRY = BLOCKED
SEMANTIC_QA_BEFORE_NEXT_PAID_SHOT = REQUIRED
```

Primeiro teste após instalação deve ser local, sem `--allow-external` e sem
`--confirm-paid-media`.

## Próximo checkpoint - Runway orchestrator gate isolation hotfix V1

1. Instalar o hotfix e executar Ruff + testes focados/regressão no projeto completo.
2. Não usar `--allow-external` nem `--confirm-paid-media` durante a validação.
3. Após verde, executar a CLI diagnóstica local da bridge para confirmar seleção do próximo shot elegível sem rede e sem gasto.


## Atualização — semantic participant integrity hotfix V1

O teste local da bridge funcionou e selecionou `shot-002`, porém o próprio prompt
expôs uma inconsistência do plano: `character_ids=[lucas]` enquanto a ação visual
inclui Ana. Não fazer live credit check nem geração paga nesse estado.

Aplicar o hotfix de integridade semântica, executar testes, rodar a reconciliação
local do run `market-test-faith-human-001` e então repetir somente a bridge local.
A bridge deve continuar sem rede e sem gasto até que os metadados estejam coerentes.

```text
RESUME_POINT = RUNWAY_GEN45_SHOT_METADATA_RECONCILIATION
SEMANTIC_PARTICIPANT_GATE = REQUIRED
ALLOW_EXTERNAL = FALSE
CONFIRM_PAID_MEDIA = FALSE
```


<!-- ATLAS_HANDOFF_UPDATE_2026_08_19 -->
## AtualizaÃ§Ã£o de handoff â€” 19/08/2026
Estado/prioridade atual em `ATLAS_CHAT_HANDOFF_2026-08-19.md`. PrÃ³ximo estÃ¡gio: `ATLAS_NARRATIVE_SERIES_FACTORY_V1`. NÃ£o retomar o piloto cena por cena. Usar `ATLAS_NEW_CHAT_START_PROMPT_2026-08-19.txt` no novo chat.
<!-- /ATLAS_HANDOFF_UPDATE_2026_08_19 -->

