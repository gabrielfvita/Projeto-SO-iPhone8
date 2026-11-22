# Projeto de Sistemas Operacionais — Latência ao toque no iPhone 8

Experimento sobre a resposta visual ao toque em um iPhone 8 (iOS 15.6), em diferentes cenários de carga de processamento. Projeto acadêmico da Universidade Presbiteriana Mackenzie.

## Materiais

- `Relatorio_Projeto_SO.pdf`: relatório final.
- `scripts/carga_cpu.py`: script executado no iPhone para a frente de Intensidade e Sobrecarga.
- `scripts/benchmark_multitarefas.py`: script executado no iPhone para a frente de Quantidade de Tarefas.
- `aplicacao-web/experimento_toque.html`: HTML original utilizado no Safari do iPhone 8 para as medições.
- `graficos/index.html`: visualização final com valores individuais em quadros.
- `dados/medicoes_do_grafico.csv`: dados utilizados para montagem dos gráficos em HTML.
- `evidencias/`: videos dos experimentos gravados em 240fps em camera lenta.

## Execução dos scripts

No terminal do iPhone com Python 3.9:

```bash
python3 ~/carga_cpu.py leve
python3 ~/carga_cpu.py media
python3 ~/carga_cpu.py pesada

python3 ~/benchmark_multitarefas.py leve
python3 ~/benchmark_multitarefas.py medio
python3 ~/benchmark_multitarefas.py pesado
```

O `carga_cpu.py` usa 12 processos e intensidade configurada de 20%, 60% ou 100%; o `benchmark_multitarefas.py` executa respectivamente 2, 3 ou 6 tarefas (hash, compressão e disco). Ambos incluem espera inicial de 5 segundos e duração nominal de 120 segundos.

### Frente de duração (Sobrecarga)

Foi utilizado **o mesmo** `carga_cpu.py`, executando `python3 ~/carga_cpu.py pesada`, e a execução foi interrompida manualmente ao atingir os intervalos estudados (10, 30 e 60 segundos).

## Medição e gráficos

O HTML da aplicação permite interação visual dos graficos com os dados reais obtidos durante o experimento em cada uma das frentes. A análise de latência relatada no trabalho foi feita pela contagem de quadros em vídeos gravados a 240 FPS (1 quadro ≈ 4,1667 ms).

Visualização online: https://graceful-fox-833bd9.netlify.app/
