# ATLAS AI MEDIA — Handoff Canônico para o Próximo Chat

**Checkpoint:** 19/08/2026 — 17:40 BRT  
**Pacote:** `atlas-ai-media` 0.4.0  
**Raiz operacional:** `C:\Users\avell\Downloads\ATLAS_AI_DEV_v0.4.0\Projetos_atlas_ai_media`  
**Run histórico/cinematográfico:** `market-test-faith-human-001`

## Como iniciar o próximo chat

Anexar este arquivo e enviar:

> **Continue o projeto ATLAS exatamente a partir do handoff anexado. Não reinicie o projeto, não volte ao fluxo manual cena por cena e não me peça para reconstruir o histórico. Preserve os gates de custo/segurança/publicação e prossiga do próximo estágio oficial: `ATLAS_NARRATIVE_SERIES_FACTORY_V1`.**

Este checkpoint prevalece sobre handoffs antigos quando houver conflito de prioridade ou estado.

## Governança

- O usuário é proprietário do ATLAS, não operador técnico.
- O assistente conduz arquitetura, engenharia, programação e estratégia técnica.
- Instruções operacionais devem ser exatas, simples e passo a passo.
- Preferência: atualização incremental por ZIP, SHA-256, backup, Ruff, pytest e execução controlada.
- Evitar edição manual pelo usuário.
- Prioridade empresarial: produção/monetização acima de perfeccionismo arquitetural.
- LLMs, AI Agents e sistemas agentic permanecem no núcleo do ATLAS.
- Nenhum serviço pago sem gate financeiro e autorização aplicável.
- Publicação pública permanece fail-closed até política/aprovação específica.
- O dono não deve coordenar asset por asset ou cena por cena em produção normal.

## Decisão estratégica de 19/08/2026

O piloto cinematográfico entrou em micro-orquestração humana por shots/cenas e passou a atrasar a chegada de conteúdo oficial ao mercado.

**Decisão:** congelar o piloto cinematográfico como P&D no estado atual. Não continuar manualmente `scene-005`, `scene-004`, `scene-001`, Ana ou outros assets apenas para fechar o piloto. Nada é descartado; o pipeline vira tecnologia reutilizável/vertical premium futura.

**Nova prioridade oficial:** `ATLAS_NARRATIVE_SERIES_FACTORY_V1`.

## Produto inicial — Narrative Series Factory

A fábrica deve receber uma premissa simples e produzir autonomamente:

`conceito → series bible → arco da temporada → episódios → cliffhangers → personagens canônicos → roteiro → beats/cenas → prompts → provider routing → mídia → voz → música → legendas → edição → QA → thumbnail → publicação → analytics → learning → próximo episódio`

### Regra central

**Não voltar à operação manual cena por cena no chat.** O episódio é a unidade de produção. Se internamente houver várias cenas/assets, o ATLAS coordena, recupera falhas e respeita orçamento/gates.

## Primeira série comercial

**Título de trabalho:** `O Milionário Disfarçado`

Premissa: Gabriel é um empresário muito rico que oculta a fortuna para descobrir se alguém pode amá-lo por quem ele é. Ele conhece Clara, que acredita que ele está em dificuldades financeiras. Quanto mais se aproximam, mais difícil fica revelar a verdade.

Personagens-base:
- Gabriel — milionário disfarçado.
- Clara — protagonista feminina.
- Henrique — rival interessado em Clara e hostil a Gabriel.
- Miguel — motorista/amigo que conhece o segredo.
- Helena — pessoa do passado capaz de revelar a identidade de Gabriel.

## Temporada-piloto

- Quantidade variável; **alvo inicial: ~5 episódios**.
- Pode ser menos ou mais conforme a história.
- **Duração-alvo: ~60–90 segundos por episódio.**
- Vertical para Shorts/Reels/TikTok.
- Todo episódio precisa de conflito, desenvolvimento, recompensa emocional e cliffhanger.
- Não alongar/comprimir só para cumprir contagem.

Arco provisório:
1. Gabriel conhece Clara; final revela carro/motorista de luxo e o segredo.
2. Clara consegue oportunidade para Gabriel; Henrique o humilha e desconfia dele.
3. Gabriel e Clara se aproximam; Helena o reconhece.
4. Gabriel resolve secretamente um problema financeiro de Clara; Henrique encontra evidência.
5. Clara confronta Gabriel: **“Quem é você de verdade?”** — cliffhanger de temporada.

## Narrative Monetization Engine

Ideia aprovada: monetizar a continuidade da história sem matar o crescimento inicial.

Hipótese inicial:
- EP. 1–3 gratuitos/públicos.
- EP. 4–5 em early access premium.
- Depois de uma janela, podem tornar-se públicos.
- Suportar assinatura, early access, passe/pagamento único por temporada e conteúdo bônus.

O ATLAS deve aprender por dados qual ponto de paywall maximiza crescimento + receita; não fixar `3 grátis + 2 pagos` como regra eterna.

Métricas: retenção, CTR, watch time, comentários, compartilhamentos, retorno ao próximo episódio, conversão premium e receita.

## Estado preservado do piloto cinematográfico

### Lucas canônico

`outputs\pipeline_v4\media\market-test-faith-human-001\canonical_character_visual_style_lock\lucas_r50_canonical_anchor.png`

SHA-256: `5B441FDE450392F6CEB352359A1B293E9D78574F701F490E7172348E08AC8924`

### scene-005

Estado: `CINEMATIC_SCENE005_SINGLE_ANCHOR_PREFLIGHT_READY`

Cobertura: `shot-032` a `shot-035`.

Planejado: máximo 1 novo asset, 5 s, 720:1280, até 60 créditos.

**Decisão atual: não fazer live credit check nem geração paga.** Piloto congelado.

Auditoria final do prompt persistido:
- `SCENE005_PROMPT_INTEGRITY_PASS`
- `PROMPT_SHA_MATCH=True`

### scene-006

Um anchor Runway Gen-4.5 já foi gerado e não deve ser regenerado.

Task ID: `e05eb45c-8674-4eac-9f25-5bd736d4e08a`

Arquivo: `outputs\pipeline_v4\media\market-test-faith-human-001\runway_gen45_production_provider\executions\e58b749650985fcaffbf\runway_gen45_5s.mp4`

SHA-256: `AF2720C19B37C372C30ECA26D9D5EC2BC26B71FFC9DE4F241CD6702F7FBF3F76`

- 5 s, 720x1280, 24 fps, sem áudio.
- QA local PASS.
- Gemini 2.5 retornou que não está disponível para novos usuários/projetos e orientou migrar para 3.6.
- Gemini 3.6 via REST v1 reconheceu o modelo e retornou `503 UNAVAILABLE / high demand`.
- Estado: **TRANSIENT_PROVIDER_HOLD**, não reprovação visual.
- Não fazer retries cegos agora.

### Créditos Runway

Último saldo **confirmado antes da geração da scene-006:** `391`.

A scene-006 tinha custo estimado/máximo de 60 e foi concluída, mas **não houve checagem pós-geração**. Portanto, **não declarar 331 como saldo confirmado**. Consultar saldo apenas quando futura decisão paga exigir.

## Infraestrutura existente e reutilizável

Já há componentes para runtime agentic, inteligência de mercado, pesquisa, roteiros, screenplay/storyboard, personagens/identidade, provider routing, Runway Gen-4.5 API, cost gates, QA local/multimodal, montagem determinística, narração, thumbnails, YouTube integration, upload privado, analytics e performance learning.

A Series Factory deve reutilizar isso, não reimplementar tudo do zero.

## Próximo estágio oficial

`ATLAS_NARRATIVE_SERIES_FACTORY_V1`

Primeira entrega integrada:
1. Series Bible contract.
2. Season Arc contract.
3. Episode Production contract.
4. Cliffhanger policy.
5. Narrative Monetization policy.
6. Autonomous episode controller.
7. Provider/cost gates reaproveitando o ATLAS existente.
8. Contrato do Episódio 1 de `O Milionário Disfarçado`.

### Critério de saída

Não ser apenas planejamento abstrato. O caminho iniciado pela V1 deve terminar no **primeiro episódio oficial completo, produzido pelo ATLAS como unidade, pronto para QA/publicação sem o proprietário coordenar cenas individualmente**.

## Restrições do próximo chat

- Não retomar `scene-005` como próximo passo.
- Não fazer live credit check da scene-005 agora.
- Não regenerar scene-006.
- Não tentar terminar o piloto manualmente antes do Narrative/Revenue MVP.
- Não usar `gemini-2.5-flash` como fallback neste projeto sem revalidação futura explícita.
- Não fazer retry cego de `gemini-3.6-flash` após 503.
- Não chamar Runway pago sem gate/autorização aplicável.
- Não transformar o usuário em orchestrator humano.
- Não retirar LLMs/agentes do núcleo operacional.
- Não abandonar analytics/performance learning.
- Não prometer receita em data fixa; validar com mercado real.

## Primeiro passo no novo chat

Reconhecer este handoff, confirmar o congelamento do piloto e iniciar a implementação de `ATLAS_NARRATIVE_SERIES_FACTORY_V1`, preservando o fluxo incremental ZIP + SHA + Ruff + pytest e a prioridade de chegar ao primeiro episódio oficial.
