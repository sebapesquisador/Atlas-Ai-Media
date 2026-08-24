# ATLAS AI MEDIA — Índice de Documentação

**Atualizado:** 17/08/2026

## Fonte oficial de verdade

Ordem de precedência para estado operacional:

1. `ATLAS_NEXT_CHAT_HANDOFF.md` — retomada imediata;
2. `ATLAS_PROJECT_STATE.md` — fatos e estado oficial;
3. `ATLAS_ARCHITECTURE.md` — arquitetura vigente;
4. `ATLAS_ROADMAP.md` — prioridades;
5. `ATLAS_MAINTENANCE_PLAN.md` — manutenção e limpeza;
6. `README.md` — visão geral.

## Histórico

- `CHANGELOG.md` — marcos históricos;
- `FINAL_ROOT_MAINTENANCE_NOTE.md` — resumo da manutenção da raiz;
- relatórios e manifests em `outputs\maintenance`;
- archives históricos;
- patch notes, relatórios antigos e coletores preservados.

Documentos históricos não devem sobrescrever o estado atual.

## Regra de atualização

Ao mudar qualquer um destes itens:

- arquitetura;
- provider principal;
- ponto de retomada;
- política de publicação;
- rota de produção;
- estado de manutenção;

atualizar imediatamente `ATLAS_PROJECT_STATE.md` e
`ATLAS_NEXT_CHAT_HANDOFF.md`.

## Regra para novos chats

Arquivo mínimo:

`ATLAS_NEXT_CHAT_HANDOFF.md`

Não é necessário carregar todo o histórico.

Adicionar `ATLAS_PROJECT_STATE.md` quando for útil revisar fatos mais amplos.

Usar ZIP de análise somente se o próximo passo depender de conteúdo real do
repositório.
