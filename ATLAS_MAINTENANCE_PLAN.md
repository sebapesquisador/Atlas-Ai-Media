# ATLAS AI MEDIA — Plano de Manutenção Segura

**Atualizado:** 17/08/2026  
**Estado:** ATIVO COMO POLÍTICA CONTÍNUA

## 1. Objetivo

Manter a raiz pequena, previsível e pronta para desenvolvimento.

Pacotes temporários usados na interação com o assistente não devem se
acumular na raiz.

## 2. Nunca remover automaticamente

Preservar:

- `atlas/`;
- `tests/`;
- `scripts/`;
- `outputs/` oficiais;
- `tools/` e modelos;
- `secrets/`;
- `.env`;
- `.github/`;
- `data/`;
- `pyproject.toml`;
- requisitos/configuração;
- documentação oficial;
- artefatos de publicação/analytics;
- anchors canônicos de personagem.

Secrets nunca devem ser incluídos em ZIP de análise.

## 3. Política para ZIP, PS1 e BAT

Arquivos temporários de fase:

- podem existir durante a execução;
- ao fechar a fase, devem ser removidos da raiz;
- preferir arquivamento em vez de exclusão;
- preservar SHA-256 quando movidos;
- a raiz não deve virar depósito de executores e pacotes.

Destino atual:

`archive\root_operational_artifacts\YYYY-MM-DD`

Categorias recomendadas:

- `update_packages_zip`;
- `analysis_diagnostics_zip`;
- `other_packages_zip`;
- `executors_bat`;
- `powershell_ps1`.

## 4. Limpeza concluída em 17/08/2026

Inventário inicial:

- 86 arquivos-alvo;
- 51 ZIP;
- 7 PS1;
- 28 BAT.

Aplicação:

- 86/86 arquivados;
- 0 exclusões;
- SHA-256 validado depois de cada movimento.

Destino:

`archive\root_operational_artifacts\2026-08-17`

Verificação final:

```text
ROOT_ZIP_COUNT = 0
ROOT_PS1_COUNT = 0
ROOT_BAT_COUNT = 0
```

## 5. Manutenção anterior de 12/08/2026

Permanece histórica e válida:

- consolidação documental;
- caches/artefatos temporários removidos;
- 148 arquivos históricos preservados;
- cópias redundantes de `client_secret*.json` removidas somente após
  confirmação de identidade com o segredo canônico;
- `secrets\youtube_client_secret.json` preservado;
- núcleo do projeto validado.

A limpeza de 17/08 é uma camada posterior, não substitui o histórico de 12/08.

## 6. Política de documentação

Ao fechar um marco estrutural, atualizar:

1. `ATLAS_PROJECT_STATE.md`;
2. `ATLAS_NEXT_CHAT_HANDOFF.md`;
3. `ATLAS_ROADMAP.md` quando prioridades mudarem;
4. `ATLAS_ARCHITECTURE.md` quando houver pivot arquitetural;
5. `CHANGELOG.md`;
6. `README.md` quando a direção do produto mudar.

O handoff deve permanecer curto e conter somente:

- estado atual;
- decisões vigentes;
- itens descartados;
- próximo passo único;
- arquivos canônicos;
- regras que não devem ser reabertas.

## 7. Troca de chat

Antes de mudar de chat:

- atualizar o handoff;
- verificar que o próximo passo está explícito;
- evitar anexar todo o histórico;
- enviar `ATLAS_NEXT_CHAT_HANDOFF.md`;
- enviar `ATLAS_PROJECT_STATE.md` somente se auditoria adicional for útil;
- usar ZIP de análise apenas quando a próxima etapa depender de arquivos reais.

## 8. Cadência recomendada

### Ao fechar uma fase grande

- arquivar ZIP/BAT/PS1 temporários;
- atualizar documentação;
- registrar changelog;
- validar raiz.

### Periodicamente

- `.pytest_cache`;
- `.ruff_cache`;
- `__pycache__`;
- egg-info regenerável;
- outputs temporários não canônicos;
- relatórios duplicados.

Qualquer limpeza recursiva deve usar inventário antes de executar.

## 9. Regra de segurança

Nunca executar scripts antigos de limpeza às cegas.

Toda manutenção consequencial deve:

1. inventariar;
2. classificar;
3. preservar o que pode ter valor;
4. executar com escopo explícito;
5. validar;
6. registrar manifesto.


<!-- ATLAS_MAINTENANCE_UPDATE_2026_08_19 -->
## Regra de manutenÃ§Ã£o â€” 19/08/2026
Impedir regressÃ£o para micro-orquestraÃ§Ã£o humana; tratar episÃ³dio como unidade; preservar fail-closed de custo/publicaÃ§Ã£o/retry; reutilizar provider routing, QA, publishing e analytics; piloto cinematogrÃ¡fico nÃ£o deve bloquear o Narrative Revenue MVP; Gemini 2.5 nÃ£o deve ser fallback ativo sem revalidaÃ§Ã£o; 503 nÃ£o deve gerar loop cego de retry.
<!-- /ATLAS_MAINTENANCE_UPDATE_2026_08_19 -->

