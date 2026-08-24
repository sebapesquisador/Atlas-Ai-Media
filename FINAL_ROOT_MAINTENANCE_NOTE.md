# ATLAS Final Root Maintenance

**Atualizado:** 17/08/2026

A raiz operacional foi limpa novamente após o ciclo cinematográfico.

Resultado final desta manutenção:

- 86/86 arquivos `.zip`, `.ps1` e `.bat` arquivados;
- 0 arquivos excluídos;
- SHA-256 validado após cada movimento;
- destino:
  `archive\root_operational_artifacts\2026-08-17`;
- verificação final:
  - ZIP na raiz: 0;
  - PS1 na raiz: 0;
  - BAT na raiz: 0.

Manifestos:

`archive\root_operational_artifacts\2026-08-17\ATLAS_ROOT_CLEANUP_MANIFEST_V1.json`

`archive\root_operational_artifacts\2026-08-17\ATLAS_ROOT_CLEANUP_MANIFEST_V1.txt`

A manutenção de 12/08 permanece preservada como histórico anterior.

Política vigente:

- packages/executors temporários não devem acumular na raiz;
- ao fechar uma fase grande, arquivar os temporários;
- atualizar os documentos canônicos;
- não apagar `outputs`, `tools`, `secrets`, código, testes ou dados oficiais
  sem inventário e decisão explícita.
