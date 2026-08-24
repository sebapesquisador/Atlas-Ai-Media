# ATLAS AI MEDIA — Arquitetura Oficial

**Atualizado:** 17/08/2026

## 1. Princípio central

O ATLAS é uma plataforma agentic de inteligência, produção e aprendizagem de
mídia.

O ATLAS não precisa possuir internamente todos os modelos de geração.
A arquitetura deve usar o melhor motor disponível para cada etapa, mantendo
a inteligência, governança, QA, custo, publicação e learning sob controle do
ATLAS.

Pipeline-alvo:

`Market Intelligence → Opportunity → Research → Script → Storyboard →
Shot/Prompt Specs → Visual Provider → QA → Assembly → Thumbnail →
Private Publish → Analytics → Learning`

## 2. Separação Production x R&D

### Production

Tudo que precisa convergir para conteúdo publicável.

Regras:

- qualidade de saída é o critério principal;
- poucos gates humanos estratégicos;
- sem loops asset por asset;
- provedores externos podem ser usados;
- falha experimental não pode bloquear produção.

### R&D

Subsistemas que ainda não provaram qualidade comercial.

Atualmente:

`LOCAL_CHARACTER_GENERATION = R&D_ONLY`

Inclui Z-Image, SD1.5/IP-Adapter e novas provas locais de identidade.

## 3. Camadas

### Intelligence

Descoberta de mercado, ranking, risco, potencial comercial e escolha de
oportunidades.

### Research & Editorial

Pesquisa, evidências, roteiro, Character Bible, screenplay e consistência.

### Agentic Runtime

Coordenação, decisões, handoffs, memória, recuperação e políticas.

### Production Orchestration

Storyboard, shot specs, prompts, seleção de provider/modelo, orçamento,
quality gates, mídia e montagem.

### Visual Engine

Camada substituível.

Pode usar:

- provedor externo;
- plataforma agregadora;
- modelo local, se um dia provar qualidade suficiente.

O próximo candidato de produção é `nim.video`, inicialmente em uso manual.

### Publishing

Upload privado, aprovações, publicação controlada e segurança.

### Analytics & Learning

Dados reais, performance learning e decisão do próximo conteúdo.

## 4. Format-first

O formato é decidido antes de escolher a técnica visual.

Exemplos:

- `FAITH_HUMAN_STORIES` → narrativa cinematográfica;
- `FAITH_BIBLE` → narrativa/documentário cinematográfico;
- `COMMERCIAL_EDUCATION` → explainer;
- `AMBIENT_LONG_FORM` → ambient long form.

A técnica visual deve se adaptar ao formato, não o contrário.

## 5. Character continuity

A identidade de personagem é um requisito de produção, mas a geração local
não é mais requisito arquitetural.

Para o proof atual:

- Lucas usa `lucas_r50_canonical_anchor.png`;
- Ricardo usa `ricardo_canonical.png`;
- um provider externo deve provar consistência entre múltiplos planos;
- nenhum batch grande é autorizado antes de uma prova curta aprovada.

## 6. Provider abstraction

O ATLAS deve tratar geração visual por contrato, não por fornecedor fixo.

Contrato conceitual:

`VisualGenerationRequest`

- shot intent;
- character references;
- environment/style constraints;
- duration/aspect ratio;
- motion requirements;
- audio requirements quando aplicável;
- cost ceiling;
- provider/model preferences.

Resposta:

`VisualGenerationResult`

- asset;
- provider/model;
- parameters;
- cost;
- provenance;
- quality evidence;
- retry eligibility.

A integração só deve ser construída depois que o provider provar qualidade
manualmente.

## 7. Gates

Gates necessários:

- market/editorial;
- cost;
- provider readiness;
- character identity/continuity;
- scene semantics;
- motion/anatomy;
- audiovisual quality;
- publication approval;
- analytics learning eligibility.

Regra de convergência:

- no máximo poucas tentativas bem definidas;
- evitar micro-repair loops;
- trocar modelo/provider/formato quando a rota não converge.

## 8. Deterministic-first

Elementos determinísticos continuam importantes para:

- montagem;
- cortes;
- timing;
- legendas;
- gráficos;
- overlays;
- áudio;
- normalização;
- export;
- QA técnico.

Mas edição determinística não deve substituir fotografia/cinema quando o
produto exige cenas humanas realistas.

## 9. Automação-alvo

Depois de aprovar o `NIM_PROOF_OF_PRODUCTION`:

1. selecionar história;
2. produzir roteiro e Character Bible;
3. compilar storyboard/shot specs;
4. gerar visual via provider;
5. validar identidade e semântica;
6. permitir uma recuperação controlada;
7. montar áudio/vídeo;
8. criar thumbnail;
9. upload privado;
10. revisão humana do master;
11. publicação conforme política;
12. analytics e learning.

## 10. Papel humano

Intervenção humana deve ocorrer em:

- prova inicial de um novo provider/modelo;
- autorização de gasto;
- revisão do master;
- publicação pública enquanto controlada;
- exceções de QA.

Não deve existir aprovação humana de dezenas de assets em produção normal.
